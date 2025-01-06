from scenarios.childe_mav_xilo_bennett_obsidian import characters as characters_, buffs as buffs_, enemy as enemy_
from utils.general import find, true
import copy

tmp_characters = copy.deepcopy(characters_)
mauvika = find("Mauvika", tmp_characters)
if mauvika:
    mauvika["artifacts"] = {
        "name": "Scroll of Cinder City",
        "flat_atk": 311 + 82.66,
        "atk": 0.2973,
        "cr": 0.3966 + 0.311 - 0.1,
        "cd": 0.7926 + 0.2,
        "em": 187 + 99.07,
        "dmg": 0.466,
        "er": 0
    }
characters = tmp_characters

tmp_buffs = copy.deepcopy(buffs_)
obsidian_codex = find("Obsidian Codex", tmp_buffs["Mauvika"])
if obsidian_codex:
    tmp_buffs["Mauvika"].remove(obsidian_codex)
    tmp_buffs["Mauvika"].append({
        "name": "Archaic Petra",
        "applies to": {"all": true},
        "effect": {"dmg": 0.35}
    })
buffs = tmp_buffs

enemy = copy.deepcopy(enemy_)
