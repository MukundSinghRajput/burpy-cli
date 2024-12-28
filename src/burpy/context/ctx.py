from typing import Dict, Any


class Context:
    def __init__(self):
        self.flags: Dict[str, Any] = {}

    def set_flag(self, flag_name: str, value: Any):
        self.flags[flag_name] = value

    def get_flag(self, flag_name: str, default=None):
        return self.flags.get(flag_name, default)
