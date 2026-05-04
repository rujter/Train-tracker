import json
from pathlib import Path


_GEOJSON = None

def get_geojson():
    global _GEOJSON
    if _GEOJSON is None:
        path = Path(__file__).parent / "ref50.geojson"
        with open(path, encoding="utf-8") as f:
            _GEOJSON = json.load(f)
    return _GEOJSON