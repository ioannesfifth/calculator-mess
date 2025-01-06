from utils.general import find, true, count, count, true
from utils.buffs import fantastic_voyage_buff, poetics_of_fuubutsu_buff, catch_buff, emblem_of_severed_fate_buff
from utils.enemy import res_multiplier, def_multiplier
from constants import STATS_ZEROED

characters = [
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
                    "count": count(8),
                    "reaction": "vaped"
                },
                {
                    "count": count(4),
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
                    "count": count(3),
                    "reaction": "vaped"
                },
                {
                    "count": count(3),
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
            "em": 685
        },
        "weapon": {"name": "Favonius Sword"},
    }
]

buffs = {
    "Xiangling": [
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
            "name": "Noblesse Oblige",
            "applies to": {"all": true},
            "effect": {"atk": 0.2}
        },
        {
            "name": "Bennett C6",
            "applies to": {"all": true},
            "effect": {"dmg": 0.15}
        },
        {
            "name": "The Catch passive",
            "applies to": {"q": true},
            "effect": catch_buff()
        },
        {
            "name": "Emblem of Severed Fate",
            "applies to": {"q": true},
            "effect": emblem_of_severed_fate_buff(find("Xiangling", characters))
        },
    ]
}

res = res_multiplier(0.4)
def_ = def_multiplier()
enemy = {
    "name": "Masanori",
    "res": res,
    "def": def_
}
