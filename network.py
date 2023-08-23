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
	firewall = Custom("firewall.heuzef.com \n 192.168.0.2 \n OpenVPN 10.100.0.0/24", "icons/firewall.png")

	# Clusters
	with Cluster("Zone HOME \n VLAN 10 \n DHCP : 192.168.10.1-99"):
		HOME = Custom("192.168.10.0/24", "icons/networking.png")
		pve = Custom("pve.heuzef.com \n 192.168.10.100", "icons/server.png")
		pgmr = Custom("pgmr.heuzef.com \n 192.168.10.101", "icons/computer.png")
		bmc = Custom("bmc.heuzef.com \n 192.168.10.111", "icons/controls.png")
		media = Custom("media.heuzef.com \n 192.168.10.112", "icons/media-services.png")
		cao = Custom("[VM STOPPED] \n cao.heuzef.com \n 192.168.10.113", "icons/status-stopped.png")
		backup = Custom("[VM] \n backup.heuzef.com \n 192.168.10.114", "icons/borg.png")
		wintest = Custom("[VM] \n wintest.heuzef.com \n 192.168.10.149", "icons/server.png")
		hongli = Custom("[VM STOPPED] \n hongli.heuzef.com \n 192.168.10.150", "icons/status-stopped.png")
		switch = Custom("switch.heuzef.com \n 192.168.10.201", "icons/switch.png")
		octoprint = Custom("octoprint.heuzef.com \n 192.168.10.203", "icons/octoprint.png")
		devices = Custom("Peripheriques", "icons/devices.png")
		imprimante = Custom("imprimante.heuzef.com \n 192.168.10.202 \n ", "icons/print.png")
		brix = Custom("brix.heuzef.com \n 192.168.10.102", "icons/cpu.png")
		aura = Custom("aura.heuzef.com \n 192.168.10.209", "icons/clock.png")
		# dyadpro = Custom("Dyad Pro", "icons/roborock.png")
		files = Custom("files.heuzef.com \n 192.168.10.110", "icons/files.png")
		wifi = Custom("Console Unifi \n 192.168.10.200/24", "icons/wifi.png")

	with Cluster("Zone DMZ \n VLAN 100 \n DHCP : 192.168.100.1-99"):
		DMZ = Custom("192.168.100.0/24", "icons/networking.png")
		heuzef_link = Custom("[VM] \n heuzef.link \n 192.168.100.103", "icons/shlink.png")
		git = Custom("[VM] \n git.heuzef.com \n 192.168.100.104", "icons/gitea.png")
		www = Custom("[VM] \n www.heuzef.com \n 192.168.100.105", "icons/web.png")
		coffre = Custom("[VM] \n coffre.heuzef.com \n 192.168.100.108", "icons/bitwarden.png")
		proxy = Custom("[VM] \n proxy.heuzef.com \n 192.168.100.110", "icons/networking-app-gw.png")
		kaladrius = Custom("[VM] \n kaladrius.fr \n 192.168.100.150", "icons/server.png")
		ftb = Custom("[VM] \n ftb.heuzef.com \n 192.168.100.151", "icons/ftb.png")
		lemurier_immo = Custom("[VM] \n lemurier.immo \n 192.168.100.152", "icons/web.png")
		couvreur_cognac_fr = Custom("[VM] \n couvreur-cognac.fr \n 192.168.100.157", "icons/web.png")
		cognhacker_net = Custom("[VM] \n cognhacker.net \n 192.168.100.159", "icons/cognhacker.png")
		beboop_boo = Custom("[VM] \n beboop.boo \n 192.168.100.160", "icons/web.png")

	# with Cluster("SPARE"):

	# Links
	internet >> Edge(color="red", label="FTTH", style="bold") >> router >> Edge(color="red", style="bold") >> firewall
	router >> Edge(color="blue", style="dotted")
	router >> Edge(color="purple") >> ezy << Edge(color="purple", label="VPN over HTTPS") << elocky
	wifi << Edge(color="blue", style="dotted") << devices
	wifi << Edge(color="blue", style="dotted") << imprimante
	wifi << Edge(color="blue", style="dotted") << brix
	wifi << Edge(color="blue", style="dotted") << aura
	# wifi << Edge(color="blue", style="dotted") << dyadpro

	firewall >> Edge(style="dotted")
	firewall >> HOME
	firewall >> DMZ

	HOME - pve
	HOME - wifi
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

	DMZ - heuzef_link
	DMZ - git
	DMZ - www
	DMZ - proxy
	DMZ - coffre
	DMZ - kaladrius
	DMZ - ftb
	DMZ - lemurier_immo
	DMZ - couvreur_cognac_fr
	DMZ - cognhacker_net
	DMZ - beboop_boo
