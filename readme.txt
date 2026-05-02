Freight train tracker

Semi-real time freight train predictor of freight trains passing through Slovenia. 

Data sources:
RFC7 - Western Balkans (Pre-arranged-train-paths-for-Timetable-2026-2027)
RFC5 - Baltic-Adriatic (CATALOGUE RFC BA DEF_PaPsTT27)
RFC6 - Mediterranean (mediterranean-rfc-2026-pap-offer)

Accessed on 10.4.2026 from https://cip.rne.eu/topology/interactive-map?welcome=true

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

Status:
Map and approximate positions of train tracks for the European freight train corridors passing through Slovenia

To do (work in progress):
More accurate train tracks fixed on their real positions
Specifications of the cargo, length and weight of the trains
=======
Freight train tracker

Semi-real time freight train predictor of freight trains passing through Slovenia. 

Data sources:
RFC7 - Western Balkans (Pre-arranged-train-paths-for-Timetable-2026-2027)
RFC5 - Baltic-Adriatic (CATALOGUE RFC BA DEF_PaPsTT27)
RFC6 - Mediterranean (mediterranean-rfc-2026-pap-offer)

Accessed on 10.4.2026 from https://cip.rne.eu/topology/interactive-map?welcome=true

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

Status:
Map and approximate positions of train tracks for the European freight train corridors passing through Slovenia

To do (work in progress):
More accurate train tracks fixed on their real positions
Specifications of the cargo, length and weight of the trains

