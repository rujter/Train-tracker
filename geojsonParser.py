#geojson loader
from geojsonLoader import get_geojson
import json
data = get_geojson()

count = 0

#/////////////////MAKING A LIST WITH ONLY COORDINATES/////////////////

coordinates_list = []
for feature in data['features']:
    coords = feature['geometry'].get('coordinates')
    coordinates_list.append(coords)

print(coordinates_list)
#/////////////////MAKING A DICTIONARY OF THE TO-FROM NODES/////////////////

def round_point(p):
    return (round(p[0], 7), round(p[1], 7))

connections = {}

for a in range(len(coordinates_list)):
    start_a = round_point(coordinates_list[a][-1]) #takes last array of the array of arrays and passes into func

    for b in range(len(coordinates_list)): 
        end_b = round_point(coordinates_list[b][0]) #takes first array of the array of arrays and passes into func

        if a == b:
            continue

        if start_a == end_b:
            connections[a] = b #if longs match, make an entry in the dictionary that they are connected

#print(connections)

#/////////////////INPUT THE START NODE LATITUDE FOR LOOKUP NUMBER/////////////////

start = 0
startlat = round(0, 7) #INSTEAD OF 0 INPUT THE LATITUDE (starts with 45 or 46)
for i in range(len(coordinates_list)):
    if startlat == round(coordinates_list[i][0][1],7): #rounding to 7 because its a float, would break otherwise
        start = i
        break
print(start, coordinates_list[start][0][1]) #print the coordinate to see if we got the right one

#/////////////////WE ORDER THE TO-FROM VALUES, WITH THE ONE THAT IS A TO NODE AS THE FIRST/////////////////

ordered = [start]

current = start
while current in connections:
    current = connections[current]
    ordered.append(current)

#/////////////////OUTPUT FOR GEOJSON FORMAT/////////////////

output = {
    'type': 'Feature',
    'properties': {'ref': '10'},
    'geometry': {
        'type': 'MultiLineString',
        'coordinates': [coordinates_list[i] for i in ordered]
    }
}

#/////////////////MAKING A NEW FILE/////////////////

with open('ref50.1.json', 'w') as f: #ENTER HERE THE NAME OF THE NEW JSON FILE, IT HAS TO BE THE SAME AS THE TOP INPUT
    json.dump(output,f,indent=2)
