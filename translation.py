#turns results into json for delivery

import json
from writeToLogs import writeToLogs



def encodeToJSON(results):
	success = ""
	try:
		success = json.dumps(results) #dumps turns python dict into json
		writeToLogs("Translation happened. Encoded: " + str(results))
	except Exception as e:
		writeToLogs("Encoding failure with error: " + str(e))
	return success 

def decodeFromJSON(results):
	success = ""
	try:
		success = json.loads(results) #loads turns json results into python dict
		writeToLogs("Translation happened. Decoded: " + results)
	except Exception as e:
		writeToLogs("Translation Decoding failure with error: " + str(e))
	return success