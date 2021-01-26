# Routing_App

A-Level Computer Science Coursework at Highdown School and Sixth Form Centre.
Contributors: Ani Hazarika

Full project Documentation:
https://1drv.ms/w/s!AsF1AkNcMI9Ngbw35KRRjgC33crtgA?e=33TKju

A Python Project creating a Route Finding Desktop Application in North Reading, Berkshire.

The aim of this project is to research path finding algorithms and use them to help people navigate safely through towns and cities such as Reading, in addition to plotting the shortest route between a given start and end point. The application will also offer routes that avoid high risk areas based on crime statistics from Thames Valley Police.

The information will be visually represented to the user clearly by highlighting the roads in the route on the map shown. This project will mainly focus on the routing algorithms. As there are many that can be used, this project will have a small investigation comparing these different algorithms to see which will be most suitable for the final product. 


## Flow of the Whole System
Is Start Button Pressed? --> Input: Start_Address --> Get geocode and validate --> Input: End_Address --> Get geocode and validate --> Find nearest nodes --> Calculate shortest route --> Show route on interactive map 

## Downloading and Cleaning the Network
The map is taken from the OpenStreetMap API. The roads are represented as a network and is downloaded from https://www.openstreetmap.org/export and saved as map.osm.
Using the method provided by Network.to_dict_of_dicts(), the network can be represented as an adjacency dictionary, and then saved in a json file, graph.json. This dictionary is then cleaned by removing all teh irrelevant tags.

## Shortest Route Algorithms
In this project, four shortest path algorithms are tested: Bellman-Ford, Dijkstra, Dijkstra with a Priority Queue and A* algorithms. These algorithms were tested against each other with 3 different tests.

Algorithm | Test | Time/seconds
----------|------|-------------
Bellman-Ford | 1 | 55.583199977874756
""	| 2 | 63.00259971618652
""	| 3 | 61.93179988861084
Dijkstra | 1 | 3.0137999057769775
""	| 2 | 2.9951999187469482
""	| 3 | 3.0576000213623047
Dijkstra with Priority Queue | 1 | 0.015599966049194336
""	| 2 | 0.031199932098388672
""	| 3 | 0.015600204467773438
A*	| 1 | 0.031200170516967773
""	| 2 | 0.015599966049194336
""	| 3 | 0.015599966049194336

It is obvious from these that Dijkstra with PQ and A* algorithms perform the best. An addition more intensive test was performed on these two in order to find which is best between them.
Algorithm | Time
----------|-----
A* | 3.4529454708099365
Dijkstra with PQ | 5.2339630126953125

From this A* algorithm was the clear winner and so is what is used in this project.


## Interactive Map
The Folium library includes an interactive map as a Leaflet.js map. When this is combined with PyQT, the map can be opened in a GUI. When the shortest route has been calculated, this route will be placed on a Leaflet.js map and saved to a webpage via Folium. Then this webpage is displayed on a GUI with PyQT.


## User Interface
The user interface is also implemented using PyQT. There are two inputs which allow teh user to select a source and destination address. These inputs have accompanying drop down menus with autocomplete suggestions based on what is already typed into the textbox. Then below there is button to start the route finding calculation and also a quit button to exit the application. In addition there is a checkbox that allows the user to avoid high crime areas.


## Finding the Nearest Node
The address typed in by the user has a specific geo-coordinate. However these may not be included in the geo-coordinates of the nodes of the network. So the nearest node to the address will have to be found. The library scipy includes a very efficient algorithm using KDTrees to achieve this in O (log n) time.


## LocationIQ API
The user can input addresses into the two inputs of the GUI. A dropdown menu showing autocomplete suggestions. These suggestions are found using the LocationIQ API. After the user has selected their addresses and chosen to commence the calculation, the geo-coordinates of the inputted addresses are also found using the LocationIQ API. The geo-coordinates are then validated.


## Avoiding High Crime Areas
Local crime data was donwloaded from http://www.ukcrimestats.com/Police_Force/Thames_Valley_Police. If the avoid high crime tickbox was checked, then a choropleth interactive map was displayed with darker areas showing areas of higher crime rates. Then the shortest route is shown which actively avoids the darker areas of the map.
