from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from datetime import datetime
today = datetime.today()

with Diagram("Carte reseau de Heuzef - %s" % today.strftime('%d/%m/%Y %H:%M') , show=False, filename="network", outformat=["png", "svg", "pdf"], direction="TB"):

	# Custom icons
	internet = Custom("Internet", "icons/internet.png")
	router = Custom("Routeur Free \n 192.168.0.1", "icons/router.png")
	ezy = Custom("Elocky EZY", "icons/cloud-keys.png")
	elocky = Custom("Serveur Elocky", "icons/server-cloud.png")
	wifi_free = Custom("Wi-Fi Free \n heuzef-cognac  \n  192.168.0.0/24", "icons/wifi.png")
	devices = Custom("Peripheriques", "icons/devices.png")
	aura = Custom("Aura", "icons/clock.png")
	withings = Custom("Serveur Withings", "icons/server-cloud.png")
	dyadpro = Custom("Dyad Pro", "icons/roborock.png")
	roborock = Custom("Serveur Roborock", "icons/server-cloud.png")
	imprimante = Custom("imprimante.heuzef.com", "icons/print.png")
	firewall = Custom("firewall.heuzef.com \n 192.168.0.2 \n OpenVPN 10.100.0.0/24", "icons/firewall.png")

	# Clusters
	with Cluster("[WIP] Zone GUEST \n VLAN 20 \n DHCP : 192.168.10.???-???"):
		GUEST = Custom("192.168.20.0/24", "icons/networking.png")
		wifi_guest = Custom("[WIP] \n Wi-Fi invite \n 192.168.20.0/24", "icons/wifi.png")

	with Cluster("Zone HOME \n VLAN 10 \n DHCP : 192.168.10.1-99"):
		HOME = Custom("192.168.10.0/24", "icons/networking.png")
		pve = Custom("pve.heuzef.com \n 192.168.10.100", "icons/server.png")
		pgmr = Custom("pgmr.heuzef.com \n 192.168.10.101", "icons/computer.png")
		files = Custom("files.heuzef.com \n 192.168.10.110", "icons/files.png")
		bmc = Custom("bmc.heuzef.com \n 192.168.10.111", "icons/controls.png")
		media = Custom("media.heuzef.com \n 192.168.10.112", "icons/media-services.png")
		cao = Custom("[VM STOPPED] \n cao.heuzef.com \n 192.168.10.113", "icons/status-stopped.png")
		backup = Custom("[VM] \n backup.heuzef.com \n 192.168.10.114", "icons/backup.png")
		wintest = Custom("[VM] \n wintest.heuzef.com \n 192.168.10.149", "icons/server.png")
		hongli = Custom("[VM] \n hongli.heuzef.com \n 192.168.10.150", "icons/vm.png")
		switch = Custom("switch.heuzef.com \n 192.168.10.201", "icons/switch.png")
		octoprint = Custom("octoprint.heuzef.com \n 192.168.10.203", "icons/octoprint.png")

	with Cluster("Zone DMZ \n VLAN 100 \n DHCP : 192.168.10.1-99"):
		DMZ = Custom("192.168.100.0/24", "icons/networking.png")
		web = Custom("[VM STOPPED] \n web.heuzef.com \n 192.168.100.101", "icons/status-stopped.png")
		password = Custom("[VM] \n password.heuzef.com \n 192.168.100.102", "icons/lesspass.png")
		heuzef_link = Custom("[VM] \n heuzef.link \n 192.168.100.103", "icons/lstu.png")
		git = Custom("[VM] \n git.heuzef.com \n 192.168.100.104", "icons/gitea.png")
		www = Custom("[VM] \n www.heuzef.com \n 192.168.100.105", "icons/web.png")
		track = Custom("[VM STOPPED] \n track.heuzef.com \n 192.168.100.106", "icons/status-stopped.png")
		matrix = Custom("[VM] \n matrix.heuzef.com \n 192.168.100.107", "icons/matrix.png")
		coffre = Custom("[VM] \n coffre.heuzef.com \n 192.168.100.108", "icons/bitwarden.png")
		proxy = Custom("[VM] \n proxy.heuzef.com \n 192.168.100.110", "icons/networking-app-gw.png")
		kaladrius = Custom("[VM] \n kaladrius.fr \n 192.168.100.150", "icons/server.png")
		ftb = Custom("[VM] \n ftb.heuzef.com \n 192.168.100.151", "icons/ftb.png")
		lemurier_immo = Custom("[VM] \n lemurier.immo \n 192.168.100.152", "icons/web.png")
		elvon_party = Custom("[VM STOPPED] \n elvon.party \n 192.168.100.153", "icons/status-stopped.png")
		sopsy_fr = Custom("[VM STOPPED] \n sopsy.fr \n 192.168.100.154", "icons/status-stopped.png")
		dontstarve = Custom("[VM STOPPED] \n dontstarve \n 192.168.100.155", "icons/status-stopped.png")
		zomboid = Custom("[VM STOPPED] \n zomboid \n 192.168.100.156", "icons/status-stopped.png")
		couvreur_cognac_fr = Custom("[VM] \n couvreur-cognac.fr \n 192.168.100.157", "icons/web.png")
		linux_cognac_fr = Custom("[VM STOPPED] \n linux-cognac.fr \n 192.168.100.158", "icons/status-stopped.png")
		cognhacker_net = Custom("[VM] \n cognhacker.net \n 192.168.100.159", "icons/cognhacker.png")

	with Cluster("SPARE"):
		brix = Custom("brix.heuzef.com \n 192.168.10.102", "icons/cpu.png")
		mini_switch = Custom("Mini-switch", "icons/switch.png")

	# Links
	internet >> Edge(color="red", label="FTTH", style="bold") >> router >> Edge(color="red", style="bold") >> firewall
	router >> Edge(color="blue", style="dotted") >> wifi_free
	wifi_free << Edge(color="blue", style="dotted") << devices
	wifi_free << Edge(color="blue", style="dotted") << imprimante
	wifi_free << Edge(color="purple", style="dotted") << aura << Edge(color="purple") << withings
	wifi_free << Edge(color="purple", style="dotted") << dyadpro << Edge(color="purple") << roborock
	router >> Edge(color="purple") >> ezy << Edge(color="purple", label="VPN over HTTPS") << elocky

	firewall >> Edge(style="dotted") >> GUEST
	firewall >> HOME
	firewall >> DMZ

	GUEST >> Edge(color="blue", style="dotted") >> wifi_guest

	HOME - pve
	HOME - pgmr
	HOME - files - Edge(color="orange") - proxy
	HOME - media
	HOME - cao
	HOME - backup
	HOME - bmc
	HOME - wintest
	HOME - hongli
	HOME - switch
	HOME - octoprint

	DMZ - web
	DMZ - password
	DMZ - heuzef_link
	DMZ - git
	DMZ - www
	DMZ - proxy
	DMZ - track
	DMZ - matrix
	DMZ - coffre
	DMZ - kaladrius
	DMZ - ftb
	DMZ - lemurier_immo
	DMZ - elvon_party
	DMZ - sopsy_fr
	DMZ - dontstarve
	DMZ - zomboid
	DMZ - couvreur_cognac_fr
	DMZ - linux_cognac_fr
	DMZ - cognhacker_net 
