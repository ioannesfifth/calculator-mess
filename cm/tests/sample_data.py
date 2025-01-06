from utils.general import find, true, count, count, true
from utils.buffs import fantastic_voyage_buff, poetics_of_fuubutsu_buff
from utils.enemy import res_multiplier, def_multiplier
from constants import STATS_ZEROED

fighting_spirit = 100

characters = [
    {
        "name": "Mauvika",
        "base_stats": {
            **STATS_ZEROED,
            "base_atk": 359,
            "flat_atk": 0,
            "atk": 0,
            "cr": 0.05,
            "cd": 0.884,
            "em": 0,
            "dmg": 0,
        },
        "artifacts": {
            "name": "Obsidian Codex",
            "flat_atk": 311,
            "atk": 0.3,
            "cr": 0.5,
            "cd": 1.2,
            "em": 187 + 20,
            "dmg": 0.466,
            "er": 0
        },
        "weapon": {
            "name": "Redhorn",
            "base_atk": 542,
            "cd": 0.882,
        },
        "q": {
            "mvs": [
                {"mv": 8.0064 + 0.0288 * fighting_spirit, "scales on": "atk"}
            ],
            "instances": [
                {
                    "count": count(1),
                    "reaction": "vaped"
                }
            ]
        },
        "e": {
            "mvs": [
                {"mv": 2.304, "scales on": "atk"}
            ],
            "instances": [
                {
                    "count": count(5),
                    "reaction": "vaped"
                },
                {
                    "count": count(1),
                    "reaction": "none"
                }
            ]
        }
    },
    {
        "name": "Bennett",
        "base_stats": {
            **STATS_ZEROED,
            "base_atk": 191,
        },
        "artifacts": {"name": "Noblesse Oblige"},
        "weapon": {
            "name": "Skyward Blade",
            "base_atk": 608,
        },
    },
    {
        "name": "Kazuha",
        "base_stats": {
            **STATS_ZEROED,
            "em": 115,
        },
        "artifacts": {
            "name": "Viridescent Veneer",
            "em": 660
        },
        "weapon": {"name": "Favonius Sword"},
    }
]

buffs = {
    "Mauvika": [
        {
            "name": "Fantasic Voyage",
            "applies to": {"q": true},
            "effect": fantastic_voyage_buff(find("Bennett", characters))
        },
        {
            "name": "Poetics of Fuubutsu",
            "applies to": {"all": true},
            "effect": poetics_of_fuubutsu_buff(find("Kazuha", characters))
        },
        {
            "name": "Obsidian Codex",
            "applies to": {"q": true},
            "effect": {"cr": 0.4, "dmg": 0.15}
        },
        {
            "name": "Mauvika's A1",
            "applies to": {"q": true},
            "effect": {"atk": 0.3}
        },
        {
            "name": "Mauvika's A4",
            "applies to": {"q": true},
            "effect": {"dmg": 0.22}
        },
    ]
}

enemy = {
    "name": "Masanori",
    "res": res_multiplier(0.4),
    "def": def_multiplier()
}
