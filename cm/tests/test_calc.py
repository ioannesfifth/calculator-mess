from main import calculate_dmg

def test_calc():
    from tests.sample_data import characters, buffs, enemy

    dmg = calculate_dmg(
        character_name="Mauvika",
        characters=characters,
        buffs=buffs["Mauvika"],
        enemy=enemy
    )

    assert round(dmg["q"]) == 295_244
    assert round(dmg["e"]) == 101_318
    assert round(dmg["total"]) == 396_562

def test_childe_xl_kaz_bennett():
    from scenarios.childe_xl_kaz_bennett import characters, buffs, enemy

    dmg = calculate_dmg(
        character_name="Xiangling",
        characters=characters,
        buffs=buffs["Xiangling"],
        enemy=enemy,
        rotations=3
    )

    assert round(dmg["q"]) == 1_269_666
    assert round(dmg["e"]) == 193_175
    assert round(dmg["total"]) == 1_462_841

def test_childe_xl_sucrose_bennett():
    from scenarios.childe_xl_sucrose_bennett import characters, buffs, enemy

    dmg = calculate_dmg(
        character_name="Xiangling",
        characters=characters,
        buffs=buffs["Xiangling"],
        enemy=enemy,
        rotations=1
    )

    assert round(dmg["q"]) == 481_106
    assert round(dmg["e"]) == 60_295
    assert round(dmg["total"]) == 541_401

def test_childe_mav_xilo_bennett_obsidian():
    from scenarios.childe_mav_xilo_bennett_obsidian import characters, buffs, enemy

    dmg = calculate_dmg(
        character_name="Mauvika",
        characters=characters,
        buffs=buffs["Mauvika"],
        enemy=enemy,
        rotations=3
    )

    assert round(dmg["q"]) == 1_129_872
    assert round(dmg["e"]) == 454_100
    assert round(dmg["total"]) == 1_583_973

def test_childe_mav_xilo_bennett_obsidian_r1():
    from scenarios.childe_mav_xilo_bennett_obsidian_r1 import characters, buffs, enemy

    dmg = calculate_dmg(
        character_name="Mauvika",
        characters=characters,
        buffs=buffs["Mauvika"],
        enemy=enemy,
        rotations=3
    )

    assert round(dmg["q"]) == 1_220_377
    assert round(dmg["e"]) == 521_575
    assert round(dmg["total"]) == 1_741_952

def test_childe_mav_xilo_bennett_scroll():
    from scenarios.childe_mav_xilo_bennett_scroll import characters, buffs, enemy

    dmg = calculate_dmg(
        character_name="Mauvika",
        characters=characters,
        buffs=buffs["Mauvika"],
        enemy=enemy,
        rotations=3,
        verbose=True
    )

    assert round(dmg["q"]) == 913_934
    assert round(dmg["e"]) == 469_855
    assert round(dmg["total"]) == 1_383_789