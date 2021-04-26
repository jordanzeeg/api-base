#write to logs
import inspect
from datetime import datetime

def writeToLogs(writings):
	with open("logs.txt","a") as logs: #open file and write
		logs.write( "at: "	+ str(datetime.now()) + ":    " + writings +  "\n")	# write parameter to file

