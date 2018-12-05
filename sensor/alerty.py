import requests
import os
#Telegram
TELEGRAM_API = os.environ['telegram_api']
TELEGRAM_CHAT = os.environ['telegram_chat']


def alertPeople(message):
	'''
	Alert people 
	'''
	sendToTelegram(message)
	sendImageTelegram()


def sendToTelegram(message,level="info"):
	'''
	Send Message to group
	'''


	if level == "info":
		'''
		Stadard info
		'''
		r = requests.get("https://api.telegram.org/{0}/sendMessage?chat_id={1}&text={2}".format(TELEGRAM_API,TELEGRAM_CHAT,message))

def sendImageTelegram():
	'''
	Send a local image to group
	'''




	url = "https://api.telegram.org/{0}/sendPhoto".format(TELEGRAM_API);
	files = {'photo': open('bild.jpg', 'rb')}
	data = {'chat_id' : TELEGRAM_CHAT}
	r= requests.post(url, files=files, data=data)
	print(r.status_code, r.reason, r.content)