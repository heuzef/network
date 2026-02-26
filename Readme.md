# Diagrams

## Installation

````
dnf install -y python3 python3-pip graphviz inkscape
pip3 install -r requirements.txt
````

## Mise en service

### Exemple

**network.py**
````
from diagrams import Diagram, Cluster, Edge
from diagrams.generic.network import Firewall
from diagrams.custom import Custom

with Diagram("Network", show=False, filename="network", direction="TB"):

	# Custom icons
	heuzef = Custom("Heuzef", "./icons/heuzef.png")

	# Import icons
	firewall1 = Firewall("Pare-feu 1")
	firewall2 = Firewall("Pare-feu 2")

	firewall1 >> firewall2 >> heuzef
````

### Générer le diagramme

``python3 network.py``

## Icon-Collection
* https://diagrams.mingrammer.com
* https://github.com/mingrammer/diagrams
* https://code.benco.io/icon-collection/azure-icons

### Installation
``git clone https://github.com/benc-uk/icon-collection.git``

### Récupérer et convertir une image de la collection avec Inkscape

``inkscape -w 1024 -h 1024 icon-collection/azure-patterns/server.svg -o icons/server.png``

### Récupérer une icone

# https://dashboardicons.com
``cd icons && wget https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/png/ICON_NAME.png``
