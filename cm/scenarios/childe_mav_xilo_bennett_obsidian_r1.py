from utils.general import find, true
from constants import STATS_ZEROED
from scenarios.childe_mav_xilo_bennett_obsidian import characters as characters_, buffs as buffs_, enemy as enemy_
import copy

tmp_characters = copy.deepcopy(characters_)
mauvika = find("Mauvika", tmp_characters)
if mauvika:
    mauvika["weapon"] = {
        "name": "A Thousand Blazing Suns",
        "base_atk": 741,
        "cr": 0.11,
    }
characters = tmp_characters

tmp_buffs = copy.deepcopy(buffs_)
serpent_spine = find("Serpent Spine", tmp_buffs["Mauvika"])
if serpent_spine:
    tmp_buffs["Mauvika"].remove(serpent_spine)
    tmp_buffs["Mauvika"].append({
        "name": "A Thousand Blazing Suns",
                "applies to": {"all": true},
                "effect": {"atk": 0.28 * 1.75, "cd": 0.2 * 1.75}
    })
buffs = tmp_buffs

enemy = copy.deepcopy(enemy_)
