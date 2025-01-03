from utils.general import find
from utils.buffs import fantastic_voyage_buff
from utils.enemy import res_multiplier, def_multiplier
from constants import STATS_ZEROED

fighting_spirit = 192
rots = 3

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
            "flat_atk": 311 + 82.66,
            "atk": 0.2973,
            "cr": 0.3966,
            "cd": 0.662 + 0.7926,
            "em": 187 + 99.07,
            "dmg": 0.466,
            "er": 0
        },
        "weapon": {
            "name": "A Thousand Blazing Suns",
            "base_atk": 741,
            "cr": 0.11,
        },
        "q": {
            "mvs": [
                {"mv": 8.0064 + 0.0288 * fighting_spirit, "scales on": "atk"}
            ],
            "instances": [
                {
                    "count": 1 * (rots - 1),
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
                    "count": 5 * rots,
                    "reaction": "vaped"
                },
                {
                    "count": 1 * rots,
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
        "q": {
            "mvs": [
                {
                    "mv": 1.39,
                    "scales on": "atk"
                }
            ]
        },
    },
]

buffs = {
    "Mauvika": [
        {
            "name": "Fantasic Voyage",
            "applies to": "q",
            "effect": fantastic_voyage_buff(find("Bennett", characters))
        },
        {
            "name": "Scroll of Cinder City",
            "applies to": "all",
            "effect": {"dmg": 0.4}
        },
        {
            "name": "Obsidian Codex",
            "applies to": "q",
            "effect": {"cr": 0.4, "dmg": 0.15}
        },
        {
            "name": "Mauvika's A1",
            "applies to": "q",
            "effect": {"atk": 0.3}
        },
        # Not sure?
        {
            "name": "Mauvika's A4",
            "applies to": "q",
            "effect": {"dmg": 0.002*fighting_spirit}
        },
        {
            "name": "Noblesse Oblige",
            "applies to": "all",
            "effect": {"atk": 0.2}
        },
        {
            "name": "Bennett C6",
            "applies to": "q",
            "effect": {"dmg": 0.15}
        },
        {
            "name": "A Thousand Blazing Suns",
            "applies to": "all",
            "effect": {"atk": 0.28 * 1.75, "cd": 0.2 * 1.75}
        }
    ]
}

enemy = {
    "name": "Masanori",
    "res": res_multiplier(0.36),
    "def": def_multiplier()
}
