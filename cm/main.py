from typing import Any
import argparse
from utils.general import find, true, count
from utils.reactions import amp_multiplier
from utils.formatting import result_string
from utils.validator import ExtendedValidator
import importlib
from jsonschema import validate
from schemas import character_schema, buffs_schema, enemy_schema
from constants import TALENTS
import copy

def apply_buff(buff, talent_type, i_rotation, i_instance, instance) -> None:
    for stat in buff["effect"]:
        if (
            (
                "all" in buff["applies to"] and
                buff["applies to"]["all"](i_rotation, i_instance)
            ) or (
                buff["applies to"].get(talent_type) and
                buff["applies to"][talent_type](i_rotation, i_instance)
            )
        ):
            instance[stat] += buff["effect"][stat]

def damage_formula(
    base_atk: int = 0,
    atk: float = 0,
    flat_atk: int = 0,
    base_def: int = 0,
    def_: float = 0,
    flat_def: int = 0,
    base_hp: int = 0,
    hp: float = 0,
    flat_hp: int = 0,
    mvs: list[dict[str, Any]] = [],
    dmg: float = 0,
    cr: float = 0,
    cd: float = 0,
    amp_multiplier: float = 0,
    verbose: bool = False,
):
    base_dmg = []
    for mv in mvs:
        stat_multiplier: float
        if mv["scales on"] == "atk":
            stat_multiplier = (base_atk * (1 + atk) + flat_atk)
        if mv["scales on"] == "def":
            stat_multiplier = (base_def * (1 + def_) + flat_def)
        if mv["scales on"] == "hp":
            stat_multiplier = (base_hp * (1 + hp) + flat_hp)

        base_dmg.append(mv["mv"] * stat_multiplier)

    damage_terms = []
    for mv_x_stat in base_dmg:
        damage_terms.append(
            mv_x_stat *
            (1 + dmg) * (1 + cr * cd) * amp_multiplier
        )

    if verbose:
        print("  atk:           ", (base_atk * (1 + atk) + flat_atk))
        for mv in mvs:
            print("  mv:            ", mv["mv"])
        print("  dmg:           ", (1 + dmg))
        print("  cr:            ", cr)
        print("  cd:            ", cd)
        print("  amp_multiplier:", amp_multiplier)
        print("  damage:        ", sum(damage_terms))

    return sum(damage_terms)


def setup(character_name, scenario, verbose: bool = False) -> dict[str, Any]:
    try:
        scenario_ = importlib.import_module(f"scenarios.{scenario}")
    except:
        raise Exception("Unable to load scenario")

    characters: list[dict[str, Any]] = scenario_.characters
    buffs: dict[str, Any] = scenario_.buffs
    print(buffs)
    enemy: dict[str, Any] = scenario_.enemy

    for character_ in characters:
        ExtendedValidator(character_schema).validate(character_)

    for character_buffs in buffs.values():
        for buff in character_buffs:
            ExtendedValidator(buffs_schema).validate(buff)

    validate(instance=enemy, schema=enemy_schema)

    setup_ = {
        "characters": characters,
        "buffs": buffs[character_name],
        "enemy": enemy
    }

    if verbose:
        print("##### Characters #####")
        print(setup_["characters"])
        print("##### Buffs #####")
        print(setup_["buffs"])
        print("##### Enemy #####")
        print(setup_["enemy"])

    return setup_


def calculate_talent_dmg(
    talent_type: str = "",
    character: dict[str, Any] = {},
    stats: dict[str, Any] = {},
    buffs: dict[str, Any] = {},
    enemy: dict[str, Any] = {},
    rotations: int = 1,
    verbose: bool = False
) -> float:
    enemy_multiplier = enemy["res"] * enemy["def"]
    character_talent = character[talent_type]

    total_dmg = []
    for i_rotation in range(rotations):
        instances = []
        for instance in character_talent["instances"]:
            for i in range(instance["count"](i_rotation)):
                instances += [{
                        "mvs": character_talent["mvs"],
                        "reaction": instance["reaction"],
                        **stats
                    }]

        rotation_dmg = []
        for i_instance, instance in enumerate(instances):
            for buff in buffs:
                apply_buff(buff, talent_type, i_rotation, i_instance, instance)
            
            if verbose:
                print(f"\n=== {talent_type.capitalize()} rotation {i_rotation} instance {i_instance} ===")

            damage = damage_formula(
                verbose=verbose,
                base_atk=instance["base_atk"],
                atk=instance["atk"],
                flat_atk=instance["flat_atk"],
                mvs=instance["mvs"],
                dmg=instance["dmg"],
                cr=instance["cr"],
                cd=instance["cd"],
                amp_multiplier=amp_multiplier(
                    instance["reaction"], instance["em"])
            ) * enemy_multiplier

            if verbose:
                print("  real damage:   ", damage)

            rotation_dmg.append(damage)

        total_dmg.append(sum(rotation_dmg))

    total_talent_dmg = sum(total_dmg)

    return total_talent_dmg

def calculate_dmg(
    character_name: str = "",
    characters: list[dict[str, Any]] = [],
    buffs: dict[str, Any] = {},
    enemy: dict[str, Any] = {},
    rotations: int = 1,
    verbose: bool = False
) -> dict[str, float]:
    character = find(character_name, characters)
    if not character:
        raise Exception("No character defined")

    stats = {}
    for stat in character["base_stats"].keys():
        stats[stat] = character["base_stats"][stat] + \
            character["artifacts"].get(
                stat, 0) + character["weapon"].get(stat, 0)

    dmg = {}
    for talent_type in list(filter(lambda x : x in character, TALENTS)):
        dmg[talent_type] = calculate_talent_dmg(
            talent_type=talent_type,
            character=character,
            stats=stats,
            buffs=buffs,
            enemy=enemy,
            rotations=rotations,
            verbose=verbose
        )

    dmg["total"] = sum(dmg.values())
    
    return dmg


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action='store_true')
    parser.add_argument("-c", "--character", type=str, required=True)
    parser.add_argument("-s", "--scenario", type=str, required=True)
    parser.add_argument("-r", "--rotations", type=int)
    args = parser.parse_args()
    print("Verbose:", args.verbose)
    verbose = args.verbose
    print("Character:", args.character)
    character_name = args.character
    print("Scenario:", args.scenario)
    scenario = args.scenario
    print("Rotations:", args.rotations)
    rotations = args.rotations if args.rotations else 1
    print("\n")

    setup_ = setup(character_name, scenario, verbose=verbose)
    characters = setup_["characters"]
    buffs = setup_["buffs"]
    enemy = setup_["enemy"]

    dmg = calculate_dmg(
        character_name=character_name,
        characters=characters,
        buffs=buffs,
        enemy=enemy,
        rotations=rotations,
        verbose=verbose
    )

    print("\n----------------------------------------\n")

    max_characters = max([len(x) for x in dmg.keys()])
    for talent_type, value in dmg.items():
        print(result_string(f"{talent_type.capitalize()}:{' ' * (max_characters - len(talent_type))}", value))


if __name__ == "__main__":
    main()
