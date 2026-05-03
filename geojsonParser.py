#geojson loader
from geojsonLoader import get_geojson
import json
data = get_geojson()

coordinates_list = []
for feature in data['features']:
    ref = feature['properties'].get('ref') #ce j
    coords = feature['geometry'].get('coordinates')
    if ref == '10':
        coordinates_list.append(coords)
output = {
    'type': 'Feature',
    'properties': {'ref': '10'},
    'geometry': {
        'type': 'LineString',
        'coordinates': coordinates_list
    }
}
with open('ref10.json', 'w') as f:
    json.dump(output,f,indent=2)

#tu moram ugotovit zdej kako parsat v geojson file oz json po ref numberjih v koordinatah? 
