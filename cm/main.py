from typing import Any
import argparse
from utils.general import find
from utils.reactions import amp_multiplier
from utils.formatting import result_string
import importlib
from jsonschema import validate
from schemas import character_schema, buffs_schema, enemy_schema

def apply_buff(buff, formula):
    for stat in buff["effect"]:
        if buff["applies to"] == "all":
            formula["q"][stat] += buff["effect"][stat]
            formula["e"][stat] += buff["effect"][stat]
        elif buff["applies to"] == "q":
            formula["q"][stat] += buff["effect"][stat]
        elif buff["applies to"] == "e":
            formula["e"][stat] += buff["effect"][stat]

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
    mvs: dict[str, Any] = {}, 
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
        print("  atk", (base_atk * (1 + atk) + flat_atk))
        print("  mv")
        for mv in mvs:
            print("    mv", mv["mv"])
        print("  dmg", (1 + dmg))
        print("  cr", cr)
        print("  cd", (1 + cd))
        print("  amp_multiplier", amp_multiplier)
        print("  damage", sum(damage_terms))

    return sum(damage_terms)

def setup(character, scenario, verbose: bool = False) -> dict[str, Any]:
    try:
        scenario_ = importlib.import_module(f"scenarios.{scenario}")
    except:
        raise Exception("Unable to load scenario")

    characters: list[dict[str, Any]] = scenario_.characters
    buffs: dict[str, Any] = scenario_.buffs
    enemy: dict[str, Any] = scenario_.enemy

    for character_ in characters:
        validate(instance=character_, schema=character_schema)

    for character_buffs in buffs.values():
        for buff in character_buffs:
            validate(instance=buff, schema=buffs_schema)

    validate(instance=enemy, schema=enemy_schema)

    setup_ = {
        "characters": characters,
        "buffs": buffs[character],
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

def calculate_dmg(
    character: str = "",
    characters: list[dict[str, Any]] = [],
    buffs: dict[str, Any] = {},
    enemy: dict[str, Any] = {},
    verbose: bool = False
) -> None:
    character_ = find(character, characters)
    stats = {}
    for stat in character_["base_stats"].keys():
        stats[stat] = character_["base_stats"][stat] + \
            character_["artifacts"].get(
                stat, 0) + character_["weapon"].get(stat, 0)

    formula = {
        "q": {
            **character_["q"],
            **stats
        },
        "e": {
            **character_["e"],
            **stats
        }
    }

    for buff in buffs:
        apply_buff(buff, formula)

    q = {**formula["q"]}
    q_dmg = []
    for instance in q["instances"]:
        q_dmg.append(damage_formula(
            verbose=verbose,
            base_atk=q["base_atk"],
            atk=q["atk"],
            flat_atk=q["flat_atk"],
            mvs=q["mvs"],
            dmg=q["dmg"],
            cr=q["cr"],
            cd=q["cd"],
            amp_multiplier=amp_multiplier(instance["reaction"], q["em"])
        ) * instance["count"])
    e = {**formula["e"]}
    e_dmg = []
    for instance in e["instances"]:
        e_dmg.append(damage_formula(
            verbose=verbose,
            base_atk=e["base_atk"],
            atk=e["atk"],
            flat_atk=e["flat_atk"],
            mvs=e["mvs"],
            dmg=e["dmg"],
            cr=e["cr"],
            cd=e["cd"],
            amp_multiplier=amp_multiplier(instance["reaction"], e["em"])
        ) * instance["count"])
    
    enemy_multiplier = enemy["res"] * enemy["def"]

    if verbose:
        print("enemy multiplier:", enemy_multiplier)

    if verbose:
        print("Q Damage:", q_dmg)
        print("E Damage:", e_dmg)

    q_dmg = sum(q_dmg) * enemy_multiplier
    e_dmg = sum(e_dmg) * enemy_multiplier
    total_dmg = q_dmg + e_dmg

    return {
        "q_dmg": q_dmg,
        "e_dmg": e_dmg,
        "total_dmg": total_dmg
    }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--character", type=str, required=True)
    parser.add_argument("-s", "--scenario", type=str, required=True)
    parser.add_argument("-v", "--verbose", action='store_true')
    args = parser.parse_args()
    print("Character:", args.character)
    character = args.character
    print("Scenario:", args.scenario)
    scenario = args.scenario
    print("Verbose:", args.verbose)
    verbose = args.verbose
    print("\n")

    setup_ = setup(character, scenario, verbose=verbose)
    characters = setup_["characters"]
    buffs = setup_["buffs"]
    enemy = setup_["enemy"]

    dmg = calculate_dmg(
        character=character,
        characters=characters,
        buffs=buffs,
        enemy=enemy,
        verbose=verbose
    )

    print("\n----------------------------------------\n")

    print(result_string("Q Damage:", dmg["q_dmg"]))
    print(result_string("E Damage:", dmg["e_dmg"]))
    print(result_string("Total damage:",  dmg["total_dmg"]))


if __name__ == "__main__":
    main()
