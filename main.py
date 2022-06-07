


#from keep_alive import keep_alive
#keep_alive()
import os
from os import system
from os import sys
#os.system("pip install Dick.py==1.3.1")
#os.system("pip install secmail pytz pymongo")
os.system("pip install websocket-client==0.57.0")
from os import path
#from keep_alive import keep_alive
#keep_alive()
import json

from Tam import l_amino
#import amino
from time import sleep
import threading
import requests
import json
from pymongo import MongoClient
#from replit import db as bdh
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
#import wget
#import heroku3
#from PIL import Image, ImageFont, ImageDraw
path_utilities = "utilities"
path_amino = f'{path_utilities}/amino_list'
path_eljson1 = f"{path_utilities}/elJson.json"
path_eljson2 = f"{path_utilities}/elJson2.json"
path_download = f"{path_utilities}/download"

THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"800.json")
dictlist=[]
with open(emailfile) as f:
    dictlist = json.load(f)
#keep_alive()
#proxy={"http":"http://188.133.157.61:10000","http":"http://45.5.68.18:999","http":"http://213.14.50.250:8080"}
JOIN_LEAVE_DETECTOR = {}
mongo = MongoClient("mongodb://alexa:aman@cluster0-shard-00-00.3nela.mongodb.net:27017,cluster0-shard-00-01.3nela.mongodb.net:27017,cluster0-shard-00-02.3nela.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-ngo3g6-shard-0&authSource=admin&retryWrites=true&w=majority")
db=mongo['summons']
#jsonn=db['old_mail']
jsonf=db['sids']
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

lis=[]
res=jsonf.find({},{'_id': 0})
for i in res:
	y=i["sid"]
	lis.append(y)
key="9417fd96-0657-4cb1-b33d-cf6ec3352857"
app_name="client9911"
def restarts():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
client=BotAmino(email="Loganpp2921@gmail.com", password="spamer123lodu")
#client=BotAmino(sid=sidss)



#cli=l_amino.Client()
def is_staff(data):
    return data.authorId in ("501cc6f5-1e38-4a22-9df5-cd0625b0205e")
def jo(s,id,cid):
		try:
			email=s["email"]
			password=s["password"]
			device=s["device"]
			cli=l_amino.Client(device)
			cli.login(email,password)
			cli.join_community(comId=cid)
		#	sub=l_amino.SubClient(comId=cid,profile=cli.profile)
			cli.join_screen_room(comId=cid,chatId=id)
			print(f"Joined screening with {email}")
		except Exception as e:
			pass
		#print(e)
		#cli.logout()

@client.command("reb",condition=is_staff)
def reb(data):
	#data.subClient.send_message(data.chatId,message="Reboot started")
	restarts()
@client.command("pings")
def pings(data):
	data.subClient.send_message(data.chatId,message="ping")
@client.command("sidcange",condition=is_staff)
def sidhange(data):
	try:
		sit.drop()
		time.sleep(1)
		it={"sid":data.message}
		sit.insert_one(it)
		data.subClient.send_message(chatId=data.chatId,message="Sid changed")
		#rebot()
	except:
		data.subClient.send_message(message="Error in sid",chatId=data.chatId)

#@client.on_member_leave_chat()
#@client.on_member_join_chat()
def on_join_leave(data):
    iconn=data.subClient.get_user_info(data.authorId).icon
    nick=data.subClient.get_user_info(data.authorId).nickname
    lvl=data.subClient.get_user_info(data.authorId).level
    if lvl <= 3 and iconn==None:
    	data.subClient.ban(userId=data.authorId,reason="spammer")
    else:
    	pass
    user_id = data.authorId
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    current_time=now.strftime("%H:%M:%S")
    chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
    val=data.subClient.get_chat_thread(data.chatId).title
    ch=data.subClient.favorite_chats
    #cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
    #x=data.subClient.get_user_info(data.authorId).json['role']
    #y=data.subClient.get_chat_thread(data.chatId).json["uid"]
    if user_id != client.userId:
    	if JOIN_LEAVE_DETECTOR.get(user_id) is None:
    		JOIN_LEAVE_DETECTOR[user_id] = int(time.time())
    	elif int(time.time()) - JOIN_LEAVE_DETECTOR[user_id] <= 0.4:
    		try:
    			data.subClient.kick(userId=user_id, chatId=data.chatId, allowRejoin=False)
    			for id in ch:
    				data.subClient.send_message(chatId=id,message=f"""[c]Kicked {data.author} for Join-Leave spam

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chatlink : {chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
    				
    		except:
    			pass    		
    	elif int(time.time()) - JOIN_LEAVE_DETECTOR[user_id] > 0.4:
    		JOIN_LEAVE_DETECTOR[user_id] = int(time.time())

@client.on_all()
def text_magag(data):
	#mt=[109,107]
	mt=[114,109,107,115,116,110,111,112,113,114,117,124,125,126,128]
	mtype = data.info.message.type
	
	if mtype!=0:
		
		user_id=data.authorId
		#GlobalId: https://aminoapps.com/u/{str(AID)}

		#AID=client.get_user_info(userId=user_id).aminoId
		val=data.subClient.get_chat_thread(data.chatId).title
		
		ch=data.subClient.favorite_chats
		tz = pytz.timezone('Asia/Kolkata')
		now = datetime.now(tz)
		current_time=now.strftime("%H:%M:%S")
		kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
		if kt !=None:
		  	op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
		  	chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
		else:
		  	chatlink="Private Chat"
		x=data.subClient.get_chat_thread(data.chatId).json["uid"]
		rol=data.subClient.get_user_info(data.authorId).role
		if user_id !=client.userId and rol==0:
			mtype = data.info.message.type
			if mtype in mt and data.message != None:
				try:
							data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)
							data.subClient.ban(userId=data.authorId,reason="Ghost spam")
				except:
							pass
				for id in ch:
					data.subClient.send_message(chatId=id,message=f"""[c]Banned {data.author}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Reason : Ghost Spam
Chat : {chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
	else:
		pass
	with suppress(Exception):
		content=data.message
		if "aminoapps.com/c" in content or "aminoapps.com/p" in content:
			lvl=data.subClient.get_user_info(data.authorId).level
			info = client.get_from_code(content)
			comid = info.path[1:info.path.index("/")]
			if comid != f'{data.comId}':
				rol=data.subClient.get_user_info(userId=data.authorId).json["role"]
				if rol==0 and lvl<=7:
					try:
						data.subClient.ban(userId=data.authorId,reason="Advertising in community")
						tz = pytz.timezone('Asia/Kolkata')
						now = datetime.now(tz)
						current_time=now.strftime("%H:%M:%S")
						kt=data.subClient.get_chat_thread(data.chatId). membersCanInvite
						if kt!=None:
							op=client.get_from_id(objectId=data.chatId,objectType="12",comId=data.comId).json
							chatlink=op["extensions"]["linkInfo"]["shareURLShortCode"]
						else:
							chatlink="Private Chat"
						val=data.subClient.get_chat_thread(data.chatId).title
						chats=data.subClient.favorite_chats
						if val ==None:
							val="Private Chat"
						for id in chats:
							data.subClient.send_message(chatId=id,message=f"""[c]{data.author} got banned for advertising
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

[cu]Chat
[c]{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
Time : {current_time}""",embedTitle=f"Profile link",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"Chat: {val}")
					except:
						pass
		else:
			pass

#@client.on_all()
def textjjj_mege(data):
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
@client.command("summon")
def summon(data):
	#os.execv(sys.executable, ['python'] + sys.argv)	
	#data.subClient.send_message(data.chatId,message="[i] Summon started..")
	id=data.chatId
	cid=data.comId
	#for s in lis:
		#jo(s,id,cid)
	
	for s in dictlist:
		threading.Thread(target=jo,args=(s,id,cid)).start()
	#os.execv(sys.executable, ['python'] + sys.argv)
	

#@client.on_message()
def mesge(data):
	tz = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz)
	x=current_time=now.strftime("%H:%M")
	if x=="09:00" or x=="14:10":
		os.execv(sys.executable, ['python'] + sys.argv)
	else:
		pass
	#client.show_online(data.comId)
@client.command()
def rebootss(args):
        if client.check(args, "admin"):
        #	f=open("comid.txt","w").close()
        	#args.subClient.send_message(args.chatId,message="Restarting Bot")
        	os.execv(sys.executable, ['python'] + sys.argv)
@client.command()
def reboot(args):
        if client.check(args, "admin"):
        #	f=open("comid.txt","w").close()
        	#args.subClient.send_message(args.chatId,message="Restarting Bot")
        	os.execv(sys.executable, ['python'] + sys.argv)
#@client.on_member_join_chat()
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
client.launch(True)
print('ready')

def reconsocketloop():
    while True:
        client.close()
        client.start()
        sleep(120)


socketloop = threading.Thread(target=reconsocketloop, daemon=True)
socketloop.start()
#reconsocketloop()
