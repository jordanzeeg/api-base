#tests
from writeToLogs import writeToLogs
from translation import encodeToJSON
from translation import decodeFromJSON
from getrepos import addRecord
from getrepos import getRecords
from getrepos import updateRecordById
from getrepos import getRecordBySearch
from getrepos import getRecordById
from getrepos import deleteRecordById

import json
count = 0

def ABS():
	global count
	writings = "this is test: " + str(count)
	print(writings)
	
	count +=1
	return writings

testDict = { "key": "value",
			"pets": "dog" } 

testRecord = '{"first_name":"Bob", "last_name":"Saget"}'

writeToLogs("\n" + "-------------------------------------------" + "\n") #separate runtimes

writeToLogs(ABS()) #testing ABS

# writeToLogs(ABS() + addRecord(testDict))

writeToLogs(ABS())
#print(getRecords())

#test getrecordbyid
writeToLogs(ABS())
print(getRecordById(15))

writeToLogs("\n" + "-------------------------------------------" + "\n") #separate 2 from 3
#test updaterecordbyid
writeToLogs(ABS())
print(updateRecordById(15,testRecord))

writeToLogs("\n" + "-------------------------------------------" + "\n") #separate 2 from 3
print("\n" + "-------------------------------------------" + "\n")

writeToLogs(ABS())
print(getRecordBySearch("first_name","Bob"))

writeToLogs("\n" + "-------------------------------------------" + "\n") #separate 2 from 3
print("\n" + "-------------------------------------------" + "\n")

writeToLogs(ABS())
print(deleteRecordById(15))