class BCOLORS:
    HEADER = '\033[31m'
    TEXT = '\033[33m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

REACTION_MULTIPLIER = {
    "vaped": 1.5,
}

STATS = [
    "base_atk",
    "flat_atk",
    "atk",
    "flat_def",
    "def",
    "flat_hp",
    "hp",
    "em",
    "er",
    "cr",
    "cd",
    "dmg",
    "anemo_dmg",
    "cryo_dmg",
    "dendro_dmg",
    "electro_dmg",
    "hydro_dmg",
    "pyro_dmg",
    "physical_dmg",
]

STATS_ZEROED = {key: 0 for key in STATS}