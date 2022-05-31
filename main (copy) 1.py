

proxy = {
  "http": "http://qlgv6:dyui6qsl@92.240.217.80:5432",
  "https": "http://qlgv6:dyui6qsl@92.240.217.80:5432"
  }
from keep_alive import keep_alive
#keep_alive()
import os
from os import system
from os import sys
#os.system("pip install Dick.py==1.3.1")
os.system("pip install secmail pytz pymongo")
os.system("pip install websocket-client==0.57.0")
from os import path
#from keep_alive import keep_alive
keep_alive()
import json
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"800.json")
dictlist=[]
with open(emailfile) as f:
    dictlist = json.load(f)
from Tam import l_amino
#import amino
from time import sleep
import threading
import requests
import json
from replit import db as bdh
from datetime import datetime
import time
from json import dumps, load
from pathlib import Path
from contextlib import suppress
from string import punctuation
from unicodedata import normalize
import time
import urllib
import pytz
import json
from BotAmino import *
import random
import string
import re
import shutil
from PIL import Image, ImageFont, ImageDraw
path_utilities = "utilities"
path_amino = f'{path_utilities}/amino_list'
path_eljson1 = f"{path_utilities}/elJson.json"
path_eljson2 = f"{path_utilities}/elJson2.json"
path_download = f"{path_utilities}/download"
#keep_alive()
#proxy={"http":"http://188.133.157.61:10000","http":"http://45.5.68.18:999","http":"http://213.14.50.250:8080"}
with suppress(Exception):
    for i in (path_utilities, path_amino):
        Path(i).mkdir(exist_ok=True)
file = open("sids.txt", "r+")
sidd=(file.read())
WARNS=[]
ANTI_SPAM = {}
JOIN_LEAVE_DETECTOR ={}
si=mongo["sid"]
sit=si["sds"]
ress=sit.find({},{'_id': 0})
for i in ress:
	sidss=i["sid"]




client=BotAmino(proxies=proxy,email="Loganpp2921@gmail.com", password="spamer123lodu")
#lient=BotAmino(sid=sidd)

def is_staff(data):
    return data.authorId in ("501cc6f5-1e38-4a22-9df5-cd0625b0205e")
def jo(s,id,cid):
		email=s["email"]
		password=s["password"]
		device=s["device"]
		cli=l_amino.Client(device,proxies=proxy)
		cli.login(email, password)
		cli.join_community(comId=cid)
		sub=l_amino.SubClient(comId=cid,profile=cli.profile)
		#sub.join_chat(id)
		#sub.send_message(id,"hey")
		cli.join_screen_room(comId=cid,chatId=id)
		print(f"Joined screening with {email}")
		#cli.logout()
		#os.remove("device.json")
#	except Exception as e:
	#	pass
		#print(e)
		#cli.logout()
@client.command("pings")
def pings(data):
	data.subClient.send_message(data.chatId,message="ping")
@client.command("sidcange",condition=is_staff)
def sidchange(data):
	try:
		sit.drop()
		time.sleep(1)
		it={"sid":data.message}
		sit.insert_one(it)
		data.subClient.send_message(chatId=data.chatId,message="Sid changed")
		#rebot()
	except:
		data.subClient.send_message(message="Error in sid",chatId=data.chatId)
#@client.on_all()
def text_mege(data):
  xu=data.info.json
  
  try:
    	mt=[114,109,107,115,116,110,111,112,113,114,117,124,125,126,128,1,50,51,57,58,59]
    	user_id=data.authorId
    	AID=client.get_user_info(userId=user_id).aminoId
    	val=data.subClient.get_chat_thread(data.chatId).title
    	#ch=data.subClient.favorite_chats
    	x=data.subClient.get_chat_thread(data.chatId).json["uid"]
    	rol=data.subClient.get_user_info(data.authorId).json['role']
    	if user_id !=client.userId and rol==0:
    		mtype = data.info.message.type
    		if mtype in mt and data.message != None:
    			try:
    				data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)
    				data.subClient.ban(userId=data.authorId,reason="Ghost spam")
    			except:
    				pass
  except:
  	pass
@client.command("smmon")
def smmon(data):
#	data.subClient.send_message(data.chatId,message="[i]leaving live..")
	id=data.chatId
	cid=data.comId
	for s in dictlist:
		threading.Thread(target=jo,args=(s,id,cid)).start()
	for s in dictlist:
		jo(s,id,cid)

@client.command()
def reboot(args):
        if client.check(args, "admin"):
        	f=open("comid.txt","w").close()
        	#args.subClient.send_message(args.chatId,message="Restarting Bot")
        	os.execv(sys.executable, ['python'] + sys.argv)
@client.on_member_join_chat()
def onnjoin(data):
#	names=["xaek","xaquaker","huesosaye228","huesos228","starmoonq55"]
	iconn=data.subClient.get_user_info(data.authorId).icon
	nick=data.subClient.get_user_info(data.authorId).nickname
	lvl=data.subClient.get_user_info(data.authorId).level
	if lvl <= 3 and iconn==None:
		data.subClient.ban(userId=data.authorId,reason="spammer")
	else:
		pass

#keep_alive()
client.launch()
print('ready')

def reconsocketloop():
    while True:
        client.close()
       # cli.close()
        client.start()
       # cli.start()
        sleep(120)


socketloop = threading.Thread(target=reconsocketloop, daemon=True)
socketloop.start()