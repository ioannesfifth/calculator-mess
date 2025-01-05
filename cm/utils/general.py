from typing import Any, Optional

def find(name: str, list: list[Any]) -> Optional[dict[str, Any]]:
    for element in list:
        if name == element["name"]:
            return element
        
    return None
