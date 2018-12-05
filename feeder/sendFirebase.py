from firebase import firebase
import json
import os


firebase = firebase.FirebaseApplication(os.environ['FIREBASE'], None)

def adddataFirebase(data):
	'''
	Add the email to the database
	'''
	jsondata = json.loads(data.decode('utf-8'))
	print(jsondata)
	store = str(jsondata['store'])
	shell = str(jsondata['shell'])
	


	result = firebase.post('/detect/'+store+'/'+shell+'/', jsondata, params={'print': 'pretty'})
	print(result)