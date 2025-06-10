from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from datetime import datetime
today = datetime.today()

with Diagram("Carte reseau de Heuzef - %s" % today.strftime('%d/%m/%Y %H:%M'), show=False, filename="network", outformat=["png", "svg", "pdf"], direction="TB"):

	# Custom icons
	internet = Custom("Internet", "icons/internet.png")
	hetzner = Custom("Sauvegardes", "icons/hetzner.png")
	with Cluster("LAN"):
		router = Custom("Routeur Free \n 192.168.0.1", "icons/router.png")
		devices = Custom("Peripheriques \n Range DHCP", "icons/devices.png")
		pgmr = Custom("PGMR \n 192.168.0.X", "icons/computer.png")
		bmc = Custom("BMC \n 192.168.0.2", "icons/controls.png")
		pve = Custom("PVE \n 192.168.0.100", "icons/server.png")
		wifi = Custom("Wi-Fi \n 192.168.0.200/24", "icons/wifi.png")
		imprimante = Custom("Imprimante \n 192.168.0.201 \n ", "icons/print.png")
		brix = Custom("Brix \n 192.168.0.202", "icons/cpu.png")
		aura = Custom("Aura \n 192.168.0.203", "icons/clock.png")
		switch = Custom("Switch \n 192.168.0.239", "icons/switch.png")
		backup = Custom("[VM] \n backup \n 192.168.0.102", "icons/borg.png")
		with Cluster("REVERSE-PROXY"):
			proxy = Custom("[VM] \n CADDY \n 192.168.0.101", "icons/caddy.png")
			vault = Custom("[VM] \n vault.heuzef.com \n 192.168.0.103", "icons/bitwarden.png")
			budget = Custom("[VM] \n budget.heuzef.com \n 192.168.0.104", "icons/wallos.png")
			files = Custom("[VM] files.heuzef.com \n 192.168.0.110", "icons/files.png")
			www = Custom("[VM] \n heuzef.com \n 192.168.0.120", "icons/web.png")
			media = Custom("[VM] media \n 192.168.0.111", "icons/media-services.png")
			lemurier_immo = Custom("[VM] \n lemurier.immo \n 192.168.0.121", "icons/web.png")
			mk4 = Custom("mk4.heuzef.com \n 192.168.0.204", "icons/prusa.png")
			kaladrius = Custom("kaladrius.fr \n 192.168.0.150", "icons/kaladrius.png")

	# Reverse Proxy
	proxy - kaladrius
	proxy - mk4
	proxy - vault
	proxy - budget
	proxy - files
	proxy - media
	proxy - www
	proxy - lemurier_immo

	# Links
	internet >> Edge(color="red", label="FTTH", style="bold") >> router >> Edge(color="blue", style="bold") >> proxy
	hetzner << Edge(color="green", label="FTTH", style="bold") >> backup
	router << Edge(color="red", style="bold") << wifi
	router << Edge(color="red", style="bold") << bmc
	router << Edge(color="red", style="bold") << pve
	router << Edge(color="red", style="bold") << switch
	wifi << Edge(color="purple", style="dotted") << devices
	wifi << Edge(color="purple", style="dotted") << imprimante
	wifi << Edge(color="purple", style="dotted") << brix
	wifi << Edge(color="purple", style="dotted") << aura
	wifi << Edge(color="purple", style="dotted") << pgmr
