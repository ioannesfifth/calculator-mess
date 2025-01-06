from jsonschema import validate
from tests.sample_data import characters, buffs, enemy
from schemas import character_schema, buffs_schema, enemy_schema
from utils.validator import ExtendedValidator

def test_character_schema():
    for character in characters:
        ExtendedValidator(character_schema).validate(character)

def test_buff_schema():
    for character_buffs in buffs.values():
        for buff in character_buffs:
            ExtendedValidator(buffs_schema).validate(buff)

def test_enemy_schema():
    ExtendedValidator(enemy_schema).validate(enemy)
