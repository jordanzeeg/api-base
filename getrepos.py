import requests
import json
import os
from writeToLogs import writeToLogs
from translation import encodeToJSON
from translation import decodeFromJSON
#get APIs
#takehome.io/twitter
#takehome.io/facebook
#takehome.io/instagram
fileName = 'MOCK_DATA.json'
fileName2 = 'MOCK_DATA2.json'
highestId = 0
def getRepos():
	writeToLogs("Program is called. ")
	
	#check status code
	if(response.status_code >= 200 and response.status_code < 300):
		#call translation and store result
		#check if request is not json
		try:
			value = response.json()  #store json portion of response
			writeToLogs("Successful storage of json from "+ str(i))

		except Exception as e:
			writeToLogs("Program encountered an error. Error: " + str(e))
			value = [] #if error, return blank value
	else:
		value = []
		writeToLogs("response Status code invalid. code given: " + str(response.status_code))
	success[str(i)] = value #adds value to success
	#endloop
	return encodeToJSON(success)

def returnData(data):
	data['id']=highestId
	return encodeToJSON(data)

def addRecord(data):
	#data = json.loads(jsonData) #data is already a (dict)
	f = open(fileName,'r') #open json file
	listings = json.load(f) #create list of dicts
	f.close()
	highestId = len(listings)+1
	data['id']=highestId #add id to added record (overwrite id if specified previous to keep id matching line in json file)
	listings.append(data)
	#f = open(fileName, 'w')
	#json.dump(listings,f)
	with open(fileName,"w") as outfile:
		outfile.write("[")
		for i in range(len(listings)-1):
			outfile.writelines(encodeToJSON(listings[i])+",\n")
		outfile.write(encodeToJSON(listings[len(listings)-1]) + "]")
		
		# change this to remove the ] and then reAdd it at the end
	return encodeToJSON(data)
	#POST

#Get all records. tested to work through curl
# TODO create test file that tests curls for me
# TODO create line to log the fact that get records ran	
def getRecords():
	#GET
	f = open(fileName, 'r')
	return (f.read())


#get record by id, tested through curl and works
#TODO create test file that tests curls for me
#TODO create line to log the fact that getRecordById ran
def getRecordById(id):
	#GET /<id>
	record = ""
	infile = open(fileName, 'r')
	record = infile.readlines()[id-1] #get record from file
	return record[0:len(record)-2] #remove newline and comma



def updateRecordById(id, data):
	#data = json.loads(data) data is already a dict
	f = open(fileName,'r')
	listings = json.load(f)
	record = listings[id-1]
	listings[id-1].update(data)
	record = listings[id-1]
	f.close()
	with open(fileName,"w") as outfile:
		outfile.write("[")
		for i in range(len(listings)-1):
			outfile.writelines(encodeToJSON(listings[i])+",\n")
		outfile.writelines(encodeToJSON(listings[len(listings)-1]) + "]")
		
	return encodeToJSON(record)
			#reading lines in
			#updates line

def getRecordBySearch(key, value):
	#GET /search
	#read in whole file as list of jsons
	# for each element of list
	# if key value in element
	#then save index, return list[index]
	listings = []
	f = open(fileName,'r')
	listings = json.load(f)
	temp = ""
	for i in listings:
		if(i[key] == value):
			temp = i
			break
	result = temp
	return encodeToJSON(result)


def deleteRecordById(id):
	#DELETE
	listings = []
	id = id
	f = open(fileName,'r')
	listings = json.load(f)
	f.close()
	with open(fileName, 'w') as infile:
		infile.write("[")
		for i in range(len(listings)-1):
			if(listings[i]['id']!= id):
				if(listings[i]['id'] > id):
					listings[i]['id'] = int(listings[i]['id'])-1
				infile.writelines(encodeToJSON(listings[i])+",\n")
		lastid = len(listings)-1
		if(listings[lastid]['id']>id):
			listings[lastid]['id'] = int(listings[lastid]['id'])-1		
		infile.write(encodeToJSON(listings[lastid]) + "]")
	return "this was a smashing success"

