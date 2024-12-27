substat_possibilities = {
    "flat_hp": [209.13, 239.00, 268.88, 298.75],
    "flat_atk": [13.62, 15.56, 17.51, 19.45],
    "flat_def": [16.20, 18.52, 20.83, 23.15],
    "hp": [00.408, 00.466, 0.0525, 0.0583],
    "atk": [0.0408, 0.0466, 0.0525, 0.0583],
    "def": [0.0510, 0.0583, 0.0656, 0.0729],
    "em": [16.32, 18.65, 20.98, 23.31],
    "er": [0.0453, 0.0518, 0.0583, 0.0648],
    "cr": [0.0272, 0.0311, 0.0350, 0.0389],
    "cd": [0.0544, 0.0622, 0.0699, 0.0777]
}

avg_substat = {}
for possibility in substat_possibilities:
    possibility_list = substat_possibilities[possibility]
    avg_substat[possibility] = sum(possibility_list)/len(possibility_list)

print(avg_substat)

DEFAULT_ROLLS = 40


def get_crit_rolls(cv):
    return round(((cv - 62.2) / 100) / avg_substat["cd"])


def get_er_rolls(er):
    return round(((er - 100) / 100) / avg_substat["er"])


def get_remaining_rolls(weights, available_rolls):
    defined_weights = filter(lambda x: x[1] != None, weights.items())
    defined_sum = sum(map(lambda x: x[1], defined_weights))
    print(defined_sum)
    if defined_sum >= 1:
        raise Exception("Defined substat weights sum to 1 or greater")

    n_none = len(list(filter(lambda x: x[1] == None, weights.items())))
    none_weight = (1 - defined_sum) / n_none
    print(none_weight)

    rolls = {}
    for stat in weights:
        weight = weights[stat]
        if weight:
            rolls[stat] = round(weight * available_rolls)
        elif weight == None:
            rolls[stat] = round(none_weight * available_rolls)
        else:
            raise Exception("Unexpected weight")

    return rolls


def get_stats(rolls):
    stats = {}
    for roll in rolls:
        stats[roll] = rolls[roll] * avg_substat[roll]

    return stats
