from typing import Any

def find(name: str, list: list[Any]) -> dict[str, Any]:
    for element in list:
        if name == element["name"]:
            return element
