import json
from pathlib import Path

_PAPS = None

def get_paps():
    global _PAPS
    if _PAPS is None:
        path = Path(__file__).parent / "paps.json"
        with open(path, encoding="utf-8") as f:
            _PAPS = json.load(f)
    return _PAPS