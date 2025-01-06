from typing import Any, Optional, Callable

def find(name: str, list: list[Any]) -> Optional[dict[str, Any]]:
    for element in list:
        if name == element["name"]:
            return element
        
    return None

def count(count_: int) -> Callable:
    return lambda i_rotation : count_

def true(*args) -> bool:
    _ = args
    return True