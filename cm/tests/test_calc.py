from main import calculate_dmg
from tests.sample_data import characters, buffs, enemy

def test_calc():
    dmg = calculate_dmg(
        character="Mauvika",
        characters=characters,
        buffs=buffs["Mauvika"],
        enemy=enemy
    )

    assert round(dmg["q_dmg"]) == 295_244
    assert round(dmg["e_dmg"]) == 101_318
    assert round(dmg["total_dmg"]) == 396_562