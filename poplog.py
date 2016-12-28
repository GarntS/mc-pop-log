import sys, datetime, os, time
from mcstatus import MinecraftServer

# GLOBALS
# List containing all the mcstatus server objects
serverList = []

# appendLog() polls the server for population data and appends it to the log
# In: The hostname and population of a server, as well as the timestamp for its retrieval time
# Out: Nada.
def appendLog(host, time, pop):
	fileName = host.replace(".", "")+ ".csv"
	with open(fileName, "a") as logFile:
		# If the file is empty add the column names
		if not os.stat(fileName).st_size > 0:
			logFile.write('"time","pos"')

		# Write the data to the file
		logFile.write("\n"+ '"'+ time+ '",'+ str(pop))

# getPopulations() Gets all the populations of the servers and calls appendLog() for each
# In: the list of servers
# Out: Nada
def getPopulations():
	global serverList

	print("Oy")

	# Loop through all the servers
	for serverObject in serverList:
		status = serverObject.status()
		pop = status.players.online
		time = datetime.datetime.now().isoformat()
		appendLog(serverObject.host, time, pop)

# Entry point.
def main():
	global serverList

	print("[mpl] Minecraft Population Logger")
	print("[mpl] Version 0.1.0")

	# No server URLs?
	if len(sys.argv[1:]) < 1:
		print("[mpl] Error: At least one URL must be specified.")
		return 0

	# Populate server list
	for url in sys.argv[1:]:
		serverObject = MinecraftServer.lookup(url)

		# If the server was found
		if serverObject != None:
			print("[mpl]", url, "was found!")
			serverList.append(serverObject)
		else:
			print("[mpl]", url, "not found! It will not be tracked.")

	while 1:
		getPopulations()
		time.sleep(60)

# Run the main.
main()