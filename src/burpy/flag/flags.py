from dataclasses import dataclass


@dataclass
class Flag:
    help: str
    long: str
    short: str = ""
    is_bool: bool = False
    is_special: bool = False
