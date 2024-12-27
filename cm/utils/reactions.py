from constants import REACTION_MULTIPLIER

def em_amp_bonus(
    em: int
) -> float:
    return 2.78 * (em / (em + 1400))

def amp_multiplier(
    reaction: str,
    em: int,
    reaction_bonus: float = 0
) -> float:
    if reaction == "none":
        return 1
    reaction_multiplier = REACTION_MULTIPLIER[reaction]
    return reaction_multiplier * (1 + em_amp_bonus(em)) * (1 + reaction_bonus)