from flask import Flask, jsonify, request
import flask
import sys
import responses

sys.path.append('../')
from writeToLogs import writeToLogs
from getrepos import *


def apiRun():
	app = flask.Flask(__name__) 
	app.config["DEBUG"] = True

	#get record by id, tested through curl and works
	#TODO create test file that tests curls for me
	#TODO create line to log the fact that this route is called
	@app.route('/', methods=['GET'])
	def home():
		#return jsonify({"data": "Hello World!"}) #hello world version
		return getRecords() #
	
	@app.route('/search/<key>=<value>', methods=['GET'])
	def search(key,value):
		return getRecordBySearch(key,value)
		#change this function to include parameters given

	@app.route('/<int:id>',methods=['GET'])
	def byId(id):
		return getRecordById(id)
		#write this function. currently does not exist

	@app.route('/<int:id>',methods=['POST'])
	def postById(id):
		req = request.get_json()
		#return jsonify({"you sent": req})
		return jsonify(updateRecordById(id, req)) #todo: fix this
	@app.route('/', methods=['PUT'])
	def add():
		req = request.get_json()
		#return returnData(req)
		return jsonify(addRecord(req))
	#update and delete
	@app.route('/<int:id>', methods=['DELETE'])
	def deleteById(id):
		req = request.get_json() #only need this if I expect to be sent id through json body
		return jsonify(deleteRecordById(id))

	app.run(port=3000)

	return ("App is running on localhost:3000")




writeToLogs(apiRun())