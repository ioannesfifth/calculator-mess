from typing import Any
from constants import STATS, TALENTS

talents = TALENTS + ["all"]

stats_properties = {}
for stat in STATS:
    stats_properties[stat] = {"type": "number"}

instance_schema = {
    "type": "object",
    "properties": {
        "count": {"type": "function"},
        "reaction": {"type": "string"}
    },
    "required": [
        "count", "reaction"
    ],
    "additionalProperties": False
}

instances_schema = {
    "type": "array",
    "items": instance_schema
}

mv_schema = {
    "type": "object",
    "properties": {
        "mv": {"type": "number"},
        "scales on": {"type": "string"}
    },
    "required": [
        "mv", "scales on"
    ],
    "additionalProperties": False
}

mvs_schema = {
    "type": "array",
    "items": mv_schema
}

talent_schema = {
    "type": "object",
    "properties": {
        "mvs": mvs_schema,
        "instances": instances_schema
    },
    "additionalProperties": False
}

stats_schema = {
    "type": "object",
    "properties": stats_properties,
    "additionalProperties": False
}

artifacts_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        **stats_properties
    },
    "required": [
        "name"
    ],
    "additionalProperties": False
}

weapon_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        **stats_properties
    },
    "required": [
        "name"
    ],
    "additionalProperties": False
}

talent_schemas = {}
for talent in talents:
    talent_schemas[talent] = talent_schema

character_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "base_stats": {
            **stats_schema,
            "required": STATS
        },
        "artifacts": artifacts_schema,
        "weapon": weapon_schema,
        **talent_schemas
    },
    "required": [
        "name", "base_stats", "artifacts", "weapon",
    ],
    "additionalProperties": False
}

applies_to_schemas: dict[str, Any] = {}
for talent in talents:
    applies_to_schemas[talent] = {"type": "function"}
buffs_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "applies to": {
            "type": "object",
            "properties": {
                **applies_to_schemas
            }
        },
        "effect": stats_schema
    },
    "required": [
        "name", "applies to", "effect"
    ],
}

enemy_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "res": {"type": "number"},
        "def": {"type": "number"}
    },
    "required": [
        "name", "res", "def",
    ],
}