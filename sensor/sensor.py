import os
import time
import datetime
from addToQue import *
from alerty import *
#####
#
# detect a value and if it smaller then last time alert
#

#Values to send
store = "ica-1"
shell = "one"





#Lets start with 0
current_weight =0




def sendData(weight):
	'''
	Send data to the que and on to the database
	'''
	data ={"store":"{0}".format(store),"shell":"{0}".format(shell),"datetime":"{0}".format(datetime.datetime.now()),"data":{"weight":"{0}".format(weight)}}
	print(data)
	dataClean = str(data).replace('\'','"')
	add_to_que(dataClean)




while True:
	'''
	Run this for ever
	'''
	#Get the weight from the scale
	print("chech values")
	file = open("weight.txt", "r") 
	weight = int(file.readline()) 



	print("on scale {0} last value {1}".format(weight,current_weight))

	if current_weight == 0:
		current_weight = weight


	if current_weight > weight:
		print("We have weight loss")
		diffrence = current_weight - weight
		diffrence_procent = float(diffrence) / float(current_weight)
		if diffrence_procent > 0.25:
			print("We have a big change")
			#alertPeople("{0}:{1} - Detetced a big drop change !".format(store,shell))
		current_weight = weight

	
	if current_weight < weight:
		print("We have gain weight")
		#Set new current waight
		current_weight = weight
		#alertPeople("{0}:{1} - Detetced incresse in data !".format(store,shell))
	

	#Send all data to database
	sendData(weight)

	#Sleep so not repet
	time.sleep(5)