from scenarios.childe_xl_kaz_bennett import characters as characters_, buffs as buffs_, enemy as enemy_
from utils.general import find, true
from constants import STATS_ZEROED
import copy

tmp_characters = copy.deepcopy(characters_)
kazuha = find("Kazuha", tmp_characters)
if kazuha:
    tmp_characters.remove(kazuha)
    tmp_characters.append({
        "name": "Sucrose",
        "base_stats": {
            **STATS_ZEROED
        },
        "artifacts": {
            "name": "Viridescent Veneer",
            "em": 600
        },
        "weapon": {"name": "Thrilling Tales"},
    })
characters = tmp_characters

tmp_buffs = copy.deepcopy(buffs_)
poetics_of_fuubutsu = find("Poetics of Fuubutsu", tmp_buffs["Xiangling"])
if poetics_of_fuubutsu:
    tmp_buffs["Xiangling"].remove(poetics_of_fuubutsu)
    tmp_buffs["Xiangling"].append({
        "name": "Thrilling Tales",
        "applies to": {"q": true},
        "effect": {"atk": 0.48}
    })
    tmp_buffs["Xiangling"].append({
        "name": "Sucrose A1 + A4",
        "applies to": {"all": true},
        "effect": {"em": 0.2 * 600 + 50}
    })
buffs = tmp_buffs

enemy = copy.deepcopy(enemy_)
