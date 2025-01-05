def get_character_stat(character, property, stat):
    return character[property].get(stat, 0) if character[property] else 0

def fantastic_voyage_buff(bennett):
    return {
        "flat_atk": 1.39 *
        (
            bennett["base_stats"]["base_atk"] +
            bennett["weapon"]["base_atk"]
        )
    }

def catch_buff():
    return {
        "dmg": 0.32,
        "cr": 0.12
    }

def emblem_of_severed_fate_buff(character):
    return {
        "dmg": 0.25 * (
            1 +
            get_character_stat(character, "base_stats", "er") +
            get_character_stat(character, "artifacts", "er") +
            get_character_stat(character, "weapon", "er")
            + 0.2
        )
    }

def poetics_of_fuubutsu_buff(kazuha):
    return {
        "dmg": 0.04 * (
            get_character_stat(kazuha, "base_stats", "em") +
            get_character_stat(kazuha, "artifacts", "em") +
            get_character_stat(kazuha, "weapon", "em")
        ) / 100
    }

def true(rotations: int) -> bool:
    return True 