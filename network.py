from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from datetime import datetime
today = datetime.today()

with Diagram("Carte reseau de Heuzef - %s" % today.strftime('%d/%m/%Y %H:%M'), show=False, filename="network", outformat=["png", "svg", "pdf"], direction="TB"):

	# Custom icons
	internet = Custom("Internet", "icons/internet.png")
	router = Custom("Routeur Free \n 192.168.0.1", "icons/router.png")

	# Clusters
	with Cluster("Zone LAN \n DHCP : 192.168.0.10-99"):
		bmc = Custom("BMC \n 192.168.0.2", "icons/controls.png")
		pve = Custom("PVE \n 192.168.0.100", "icons/server.png")
		pgmr = Custom("PGMR \n 192.168.0.X", "icons/computer.png")
		proxy = Custom("[VM] \n proxy \n 192.168.0.101", "icons/networking-app-gw.png")
		media = Custom("[VM] media \n 192.168.0.111", "icons/media-services.png")
		backup = Custom("[VM] \n backup.heuzef.com \n 192.168.10.114", "icons/borg.png")
		switch = Custom("Switch \n 192.168.0.239", "icons/switch.png")
		mk4 = Custom("mk4.heuzef.com \n 192.168.0.204", "icons/prusa.png")
		devices = Custom("Peripheriques \n Range DHCP", "icons/devices.png")
		imprimante = Custom("imprimante.heuzef.com \n 192.168.0.201 \n ", "icons/print.png")
		brix = Custom("Brix \n 192.168.0.202", "icons/cpu.png")
		aura = Custom("Aura \n 192.168.0.203", "icons/clock.png")
		files = Custom("[VM] files \n 192.168.0.110", "icons/files.png")
		wifi = Custom("Wi-Fi \n 192.168.0.200/24", "icons/wifi.png")
		heuzef_link = Custom("[VM] \n heuzef.link \n 192.168.0.X", "icons/shlink.png")
		git = Custom("[VM] \n git.heuzef.com \n 192.168.0.X", "icons/gitea.png")
		www = Custom("[VM] \n www.heuzef.com \n 192.168.0.X", "icons/web.png")
		coffre = Custom("[VM] \n coffre.heuzef.com \n 192.168.0.X", "icons/bitwarden.png")
		kaladrius = Custom("[VM] \n kaladrius.fr \n 192.168.0.X", "icons/server.png")
		ftb = Custom("[VM] \n ftb.heuzef.com \n 192.168.0.X", "icons/ftb.png")
		lemurier_immo = Custom("[VM] \n lemurier.immo \n 192.168.0.X", "icons/web.png")
		couvreur_cognac_fr = Custom("[VM] \n couvreur-cognac.fr \n 192.168.0.X", "icons/web.png")
		cognhacker_net = Custom("[VM] \n cognhacker.net \n 192.168.0.X", "icons/cognhacker.png")
		beboop_boo = Custom("[VM] \n beboop.boo \n 192.168.0.X", "icons/web.png")

	# with Cluster("SPARE"):

	# Links
	internet >> Edge(color="red", label="FTTH", style="bold") >> router >> Edge(color="red", style="bold") >> proxy
	wifi << Edge(color="blue", style="dotted") << devices
	wifi << Edge(color="blue", style="dotted") << imprimante
	wifi << Edge(color="blue", style="dotted") << brix
	wifi << Edge(color="blue", style="dotted") << aura
