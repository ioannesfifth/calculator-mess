from jsonschema import validate
from tests.sample_data import characters, buffs, enemy
from schemas import character_schema, buffs_schema, enemy_schema

def test_character_schema():
    for character in characters:
        validate(instance=character, schema=character_schema)

def test_buff_schema():
    for character_buffs in buffs.values():
        for buff in character_buffs:
            validate(instance=buff, schema=buffs_schema)

def test_enemy_schema():
    validate(instance=enemy, schema=enemy_schema)
