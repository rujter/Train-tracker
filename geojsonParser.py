#geojson loader
from geojsonLoader import get_geojson
import json
data = get_geojson()

count = 0

#ADDING SEGMENTS WITH THE SAME REFERENCE NUMBER INTO ONE LIST
coordinates_list = []
for feature in data['features']:
    ref = feature['properties'].get('ref') #ce j
    coords = feature['geometry'].get('coordinates')
    if ref == '10': #ENTER HERE THE REFERENCE NUMBER YOU WANT TO PARSE
        coordinates_list.append(coords)


#MAKING A DICTIONARY OF THE TO-FROM NODES
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

#WE FIND THE NODE THAT IS A FROM NODE, BUT NOT A TO NODE
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


#WE ORDER THE TO-FROM VALUES, WITH THE ONE THAT IS A TO NODE AS THE FIRST
ordered = [start]
current = start
while current in connections:
    current = connections[current]
    ordered.append(current)

#OUTPUT FOR GEOJSON FORMAT
output = {
    'type': 'Feature',
    'properties': {'ref': '10'},
    'geometry': {
        'type': 'MultiLineString',
        'coordinates': [coordinates_list[i] for i in ordered]
    }
}

#MAKING A NEW FILE
with open('ref10.json', 'w') as f: #ENTER HERE THE NAME OF THE NEW JSON FILE, IT HAS TO BE THE SAME AS THE TOP INPUT
    json.dump(output,f,indent=2)
