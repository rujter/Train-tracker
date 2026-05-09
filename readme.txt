Freight train tracker

Semi-real time freight train predictor of freight trains passing through Slovenia. 

Data sources:
RFC7 - Western Balkans (Pre-arranged-train-paths-for-Timetable-2026-2027)
RFC5 - Baltic-Adriatic (CATALOGUE RFC BA DEF_PaPsTT27)
RFC6 - Mediterranean (mediterranean-rfc-2026-pap-offer)

Accessed on 10.4.2026 from https://cip.rne.eu/topology/interactive-map?welcome=true

Train positions are based on data pulled from OverpassAPI using Overpass turbo

- Train positions are based on PaPs (Pre-Arranged Paths) because no open access freight train position data exists for the public.
- Each PaP defines a fixed route, timetable and set of running days for a train crossing one or more countries. They are published annually as 
part of the network timetable and represent the planned schedule

Program:
Python + PyQt6 for desktop window
JS + Leaflet.js (map)
Json (PaP train data)

Setup
Works on python 3.9 onwards
pip install PyQt6 PyQt6-WebEngine
Navigate to the source directory
run python main.py

Extras:
I included the geojsonLoader.py and geojsonParser.py. While downloading OverpassAPI railway data it sometimes happens that, mimicking real life, we get parallel railways, one going each way. Should we want to chain them in a straight line for the train location predictor to work, we have to order their coordinates in a straight line, because the coordinates pulled from OverpassAPI aren't ordered. But during the ordering process it sometimes happens that the parser takes the other railways coordinates and orders them as the railway we want. This is why we have to add the start latitude in the code manually, so it chains the right side of the railway together.

I also included geojson files including sorted coordinates of the main slovenian freight corridors

To do (work in progress):
More accurate train tracks fixed on their real positions
Specifications of the cargo, length and weight of the trains