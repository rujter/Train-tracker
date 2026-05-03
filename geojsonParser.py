#geojson loader
from geojsonLoader import get_geojson
import json
data = get_geojson()

count = 0

#ugotovi segmente in jih da v en list
coordinates_list = []
for feature in data['features']:
    ref = feature['properties'].get('ref') #ce j
    coords = feature['geometry'].get('coordinates')
    if ref == '10':
        coordinates_list.append(coords)


#naredi dict z connectioni
def round_point(p):
    return (round(p[0], 7), round(p[1], 7))

connections = {}

for a in range(len(coordinates_list)):
    start_a = round_point(coordinates_list[a][-1])

    for b in range(len(coordinates_list)):
        end_b = round_point(coordinates_list[b][0])

        if a == b:
            continue

        if start_a == end_b:
            connections[a] = b

print(connections)


#zdej moram najt val, ki je kot key ma nikoli kot val

start = 0

fromL = list(connections.keys())
toL = list(connections.values())

for i in range(len(fromL)):
    isStart = True
    for j in range(len(toL)):

        if fromL[i] == toL[j]:
            isStart = False
            break
    
    if isStart == True:
        start= fromL[i]
        break 
        #key je ta first val ta drug

#zdej je start ta ki je key, ni pa val

#moramo orderat koncno
ordered = [start]
current = start
while current in connections:
    current = connections[current]
    ordered.append(current)


output = {
    'type': 'Feature',
    'properties': {'ref': '10'},
    'geometry': {
        'type': 'MultiLineString',
        'coordinates': [coordinates_list[i] for i in ordered]
    }
}

with open('ref10.json', 'w') as f:
    json.dump(output,f,indent=2)
