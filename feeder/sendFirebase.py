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
	airport = str(jsondata['airport'])
	storage = str(jsondata['storage'])
	


	result = firebase.post('/saldo/'+airport+'/'+storage+'/', jsondata, params={'print': 'pretty'})
	print(result)