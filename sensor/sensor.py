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
airport = "arlanda"
storage = "one"





#Lets start with 0
number =0




def sendData(number):
	'''
	Send data to the que and on to the database
	'''
	data ={"airport":"{0}".format(airport),"storage":"{0}".format(storage),"datetime":"{0}".format(datetime.datetime.now()),"data":{"kolli":"{0}".format(number)}}
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



	print("on scale {0} last value {1}".format(weight,number))

	if number == 0:
		number = weight


	if number > weight:
		print("We have change")
		alertPeople("{0}:{1} - Brush kolli has bean updated to  {2}".format(airport,storage,weight))
		number = weight

	
	if number < weight:
		print("We have gain weight")
		alertPeople("{0}:{1} - Brush kolli has bean updated to  {2}".format(airport,storage,weight))
		number = weight
	

	#Send all data to database
	sendData(weight)

	#Sleep so not repet
	time.sleep(10)