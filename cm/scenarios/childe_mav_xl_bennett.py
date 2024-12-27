from utils.general import find
from utils.buffs import fantastic_voyage_buff, catch_buff, emblem_of_severed_fate_buff
from utils.enemy import res_multiplier, def_multiplier
from constants import STATS_ZEROED

fighting_spirit = 110

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
            "dmg": 0
        },
        "artifacts": {
            "name": "Scroll of Cinder City",
            "flat_atk": 311 + 82.66,
            "atk": 0.2973,
            "cr": 0.3966 + 0.311 - 0.1,
            "cd": 0.7926 + 0.2,
            "em": 187 + 99.07,
            "dmg": 0.466,
            "er": 0
        },
        "weapon": {
            "name": "Serpent Spine",
            "base_atk": 510,
            "cd": 0.276,
        },
        "q": {
            "mvs": [
                {"mv": 8.0064 + 0.0288 * fighting_spirit, "scales on": "atk"}
            ],
            "instances": [
                {
                    "count": 1,
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
                    "count": 3,
                    "reaction": "vaped"
                },
                {
                    "count": 3,
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
            "name": "Aquila Favonia",
            "base_atk": 674,
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
    {
        "name": "Xiangling",
        "base_stats": {
            **STATS_ZEROED,
            "base_atk": 225,
            "flat_atk": 0,
            "atk": 0,
            "cr": 0.05,
            "cd": 0.5,
            "em": 96,
            "dmg": 0
        },
        "artifacts": {
            "name": "Emblem of Severed Fate",
            "flat_atk": 311 + 66.14,
            "atk": 0.466 + 0.2477,
            "cr": 0.33 + 0.311,
            "cd": 0.7265,
            "em": 79.26,
            "dmg": 0.466,
            "er": 0.3303
        },
        "weapon": {
            "name": "The Catch",
            "base_atk": 510,
            "er": 0.459
        },
        "q": {
            "mvs": [
                {"mv": 2.38, "scales on": "atk"}
            ],
            "instances": [
                {
                    "count": 8,
                    "reaction": "vaped"
                },
                {
                    "count": 4,
                    "reaction": "none"
                },
            ]
        },
        "e": {
            "mvs": [
                {"mv": 2, "scales on": "atk"}
            ],
            "instances": [
                {
                    "count": 3,
                    "reaction": "vaped"
                },
                {
                    "count": 3,
                    "reaction": "none"
                }
            ]
        }
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
            "name": "Mauvika's A1",
            "applies to": "q",
            "effect": {"atk": 0.3}
        },
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
            "name": "Serpent Spine",
            "applies to": "all",
            "effect": {"dmg": 0.5}
        },
    ],
    "Xiangling": [
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
            "name": "Noblesse Oblige",
            "applies to": "all",
            "effect": {"atk": 0.2}
        },
        {
            "name": "Bennett C6",
            "applies to": "all",
            "effect": {"dmg": 0.15}
        },
        {
            "name": "The Catch passive",
            "applies to": "q",
            "effect": catch_buff()
        },
        {
            "name": "Emblem of Severed Fate",
            "applies to": "q",
            "effect": emblem_of_severed_fate_buff(find("Xiangling", characters))
        },
    ]
}

enemy = {
    "name": "Masanori",
    "res": res_multiplier(0),
    "def": def_multiplier()
}
