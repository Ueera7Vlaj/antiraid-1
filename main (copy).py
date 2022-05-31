from keep_alive import keep_alive
keep_alive()
import os
from os import sys
from os import system
#os.system("pip install Dick.py==1.3.1")
os.system("pip install secmail")
#os.system("pip install websocket-client==0.57.0")
import json
from Tam import local_amino
from time import sleep
import threading
from replit import db
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
with suppress(Exception):
    for i in (path_utilities, path_amino):
        Path(i).mkdir(exist_ok=True)
file = open("sids.txt", "r+")
sidd=(file.read())
ANTI_SPAM = {}
JOIN_LEAVE_DETECTOR = {}
#client=BotAmino(sid=sidd)
client=BotAmino()
def is_staff(data):
    return data.authorId in ("501cc6f5-1e38-4a22-9df5-cd0625b0205e")

def is_black(data):
	return data.authorId not in data.subClient.favorite_users

#client.wait=2

try:
    with open("levels.json", "r") as g:
        levels = json.load(g)
except Exception:
    levels = {}

try:
    with open("users.json", "r") as f:
        use = json.load(f)
except Exception:
    use = {}

    
def join_community(comId: str = None, inv: str = None):
    if inv:
        try:
            client.join_community(comId=comId, invitationId=inv)
            return True
        except Exception as e:
            print_exception(e)        

    
@client.command()
def joinamino(args):
    invit = None
    if not client.check(args,"admin"):
        args.subClient.send_message(args.chatId, "Admin command")
        return

    staff = args.subClient.get_staff(args.message)
    if not args.message:
        args.subClient.send_message(args.chatId, "Wrong amino ID!")
        return

    try:
        test = args.message.strip().split()
        amino_c = test[0]
        invit = test[1]
        invit = invit.replace("http://aminoapps.com/invite/", "")
    except Exception:
        amino_c = args.message
        invit = None

    try:
        val = args.subClient.client.get_from_code(f"http://aminoapps.com/c/{amino_c}")
        comId = val.json["extensions"]["community"]["ndcId"]
    except Exception:
        val = ""

    isJoined = val.json["extensions"]["isCurrentUserJoined"]
    if not isJoined:
    	join_community(comId, invit)
    	val = client.get_from_code(f"http://aminoapps.com/c/{amino_c}")
    	isJoined = val.json["extensions"]["isCurrentUserJoined"]
    	if isJoined:
    	       Thread(target=client.threadLaunch, args=[comId, True]).start() 
    	       auth = client.get_community(comId).get_user_info(args.authorId).nickname 
    	       client.get_community(comId).ask_amino_staff(f"Hello! I am a bot and i can do a lot of stuff!\nI've been invited here by {auth}.\nIf you need help, you can do !help.\nEnjoy^^") 
    	       args.subClient.send_message(args.chatId, "Joined!") 
    	       return 
    	       args.subClient.send_message(args.chatId, "Waiting for join!")
    	       return
    else:
        args.subClient.send_message(args.chatId, "Allready joined!")
        return    
@client.on_member_join_chat()
def joined(data):
	if data.authorId not in use.keys():
		update_data(use, data.authorId)
		with open('users.json', 'w') as f:
			json.dump(use, f)

@client.command("sidch")
def sidch(data):
	f = open("sids.txt", "r+")
	f.seek(0)
	f.truncate()
	data.subClient.send_message(data.chatId,message="Sid removed")
	xs=client.sid
	file = open('sids.txt', 'w') 
	file.write(xs)
	file.close()
	data.subClient.send_message(data.chatId,message="sid changed")
	time.sleep(5)
	os.execv(sys.executable, ["None", os.path.basename(sys.argv[0])])
	data.subClient.send_message(data.chatId,message="Bot restarted")
#@client.on_message()
def messg(data):
    if data.authorId != client.userId:
    	update_data(use, data.authorId)
    	add_experience(use, data.authorId, 2)
    	level_up(use, data.authorId, data)
    	with open('users.json', 'w') as f:
    		json.dump(use, f)



def update_data(use,user):
    if not user in use:
        use[user] = {}
        use[user]['experience'] = 0
        use[user]['level'] = 1


def add_experience(use, user, exp):
    use[user]['experience'] += exp


def level_up(use, user, db):
	experience = use[user]['experience']
	lvl_start = use[user]['level']
	lvl_end = int(experience*(1/800))
	if lvl_start < lvl_end:
	       print(f"levelup {lvl_end}")
	       imgg2 = ("rank.png")
	       Image.open(imgg2).resize((1007, 400)).save("anim.png")
	       img2=Image.open("anim.png")
	       x=db.subClient.get_user_info(user).icon
	       response=requests.get(f"{x}")
	       file=open(".amhkbple.png","wb")
	       file.write(response.content)
	       file.close()
	       img5=open(".amhkbple.png","rb")
	       img = Image.open(".amhkbple.png").resize((300,300))
	       #img2 = Image.open(".level.png")
	       img2.paste(img, (50,50))
	       title_fo = ImageFont.truetype('BebasNeue-Regular.ttf', 50)
	       title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 70)
	       draw = ImageDraw.Draw(img2)
	       draw.text((390,50), f"{db.author}",(255,255,0), font=title_fo,align="right")
	       draw.text((390,110), "Congrats", (255, 0, 0), font=title_font,align="right")
	       draw.text((390,180), f"You Reached Level {lvl_end}", (255, 0, 0), font=title_font)
	       img2=img2.save(".ihbjh3.png")
	       imgg=open(".ihbjh3.png","rb")
	       msg=f"Congrats {db.author} 🎉"
	       db.subClient.full_embed(f"ndc://x{db.comId}/user-profile/{db.author}",imgg,msg,db.chatId)
	       use[user]['level'] = lvl_end

dictlist = [{"email":"sh6aheo@esiix.com","password":"#PROUDCATOWNER","device":"1717af0cec0293471b7b82f9e59b2c8afcfed709fc29e64f0586d396523bbe8bd09b10494aee419d0f"},{"email":"97wj6b1eku@esiix.com","password":"#PROUDCATOWNER","device":"17c666fd25cbf88d17af265e244962d1fb1eb0e7bdffa7dd1ea973465955ac33d4e83014b0cf4f0f36","auid":"14cb299c-2d9c-45e0-84b4-39867c4dffc2"},{"email":"k52pbtguy870@1secmail.net","password":"#PROUDCATOWNER","device":"1733e05d7180d6e6dde8248011b98b558e7ff5f01e16c09f3303388fdc0cb8d551dafc8349f355da9f"},{"email":"sh6aheo@esiix.com","password":"#PROUDCATOWNER","device":"1717af0cec0293471b7b82f9e59b2c8afcfed709fc29e64f0586d396523bbe8bd09b10494aee419d0f"},{"email":"twg3exl@esiix.com","password":"#PROUDCATOWNER","device":"1746030061082d4bad8ef9d9069fedc75fae6e9f2a6672b92a40e4833de5389495fd5b7d71f8433cfe"},{"email":"yswp9kt@esiix.com","password":"#PROUDCATOWNER","device":"17af3379cc5dbcda1f2b8f5d06cd8ca8d44804f6f533d787c07d704f349e8f397b2ee395fa25bdb9d6"},{"email":"lewa4w@oosln.com","password":"#PROUDCATOWNER","device":"1714c394eb81b2175a2fd9fb87dcaabf7a2866e2b840be0d5211b9ed24d22af26267a88977192a8403"},{"email":"rqenazk1u56u@oosln.com","password":"#PROUDCATOWNER","device":"17234d590ea932edc604e3a59ec00bf0b16b4ac46d0a75d6132e4dca233597bfc6967ac588db903dc8"},{"email":"zsbru3cz384k@oosln.com","password":"#PROUDCATOWNER","device":"170428e06ae48bd711d8b538b972982e1f8a1506b3778f61f0d4d635e5284de34f01379647223bc39c"},{"email":"zrj8k08g8r@vddaz.com","password":"#PROUDCATOWNER","device":"172d79a23ee345690c35912269bb9a86087427840767db9acc0a061a5f562c3b94fe77550e8f28bbac"},{"email":"i5xqj5le9son@wwjmp.com","password":"#PROUDCATOWNER","device":"1727de5fc3639eef796ab8b5694d26acf1e0ff21f4a807142eb3a5c0edd08f587443b92d27dfbbe675"},{"email":"yjhm21bi2f@1secmail.org","password":"#PROUDCATOWNER","device":"178eed3f68fdbe60cdc903d4fca859381d6ffcc230001a87a31a299b3d0ba68f00c59bab2ae286e49e"},{"email":"2j0feb1d@xojxe.com","password":"#PROUDCATOWNER","device":"178d7ccb8f9bb821960677460818e1e55ab8fd174361ae5bb7c3e2d2929a29b7d04ef27b061b1409a4"},{"email":"7o46lgd6@xojxe.com","password":"#PROUDCATOWNER","device":"179248dac9ca4c4125b45b292c5806c33c894628126be35817c5743e718c6a53abdb22e80f22e87c5e"},{"email":"auizfw3ad@1secmail.org","password":"#PROUDCATOWNER","device":"17a6b7ac598aa915926e9cf24047c96a45606a8961486668d42b59f18f79695f429fed68dfc2d47b04"},{"email":"1zo0oay@1secmail.org","password":"#PROUDCATOWNER","device":"17ffce784ecc226f5f3dca4492ee6444043761503ab3fa8313249940f1004790dfa36046927567225b"},{"email":"1zo0oay@1secmail.org","password":"#PROUDCATOWNER","device":"17ffce784ecc226f5f3dca4492ee6444043761503ab3fa8313249940f1004790dfa36046927567225b"},{"email":"ntq8zvh73pg@1secmail.org","password":"#PROUDCATOWNER","device":"17c7f1121cb4c7d7e9212f45cffcc3f399ecfd0992969abaf7c7cc3c170ab4959fc4c15c3c3bf95245"},{"email":"s2x6kl5@1secmail.net","password":"#PROUDCATOWNER","device":"179c84482f289cfe7214941473f76bda115e2b0b8f8ee7eeb22d6ab84d9dc0017cc91cbe9abfc6022b"}]

def log(cli,email,password):
	try:
		cli.login(email,password)
	except:
		pass


def jo(s,id,cid):
	email=s["email"]
	password=s["password"]
	device=s["device"]
	cli=local_amino.Client(device)
	log(cli,email, password)
	try:
		cli.join_community(comId=cid)
		sub=local_amino.SubClient(comId=cid,profile=cli.profile)
		sub.join_chat(id)
		#sub.send_message(id,"hey")
		cli.join_screen_room(comId=cid,chatId=id)
		print(f"Joined screening with {email}")
		cli.logout()
		#os.remove("device.json")
	except Exception as e:
		print(e)
		cli.logout()

@client.command("summon", condition=is_black)
def summon(data):
	data.subClient.send_message(data.chatId,message="[i]Started summon users")
	id=data.chatId
	cid=data.comId
	for s in dictlist:
		try:
			jo(s,id,cid)
			print("started")
		except Exception as e:
			print(e)

@client.command()
def rank(data):
	user_id=data.authorId
	with open('users.json', 'r') as f:
		use = json.load(f)
		lvl = use[str(user_id)]['level']
		ex = use[str(user_id)]['experience']
		print(lvl ,ex)
		img2 = ("rank.png")
		Image.open(img2).resize((1000, 300)).save("aniim.png")
		img3=Image.open("aniim.png")
		
		x=data.subClient.get_user_info(user_id).icon
		response=requests.get(f"{x}")
		file=open(".user772.png","wb")
		file.write(response.content)
		file.close()
		img = Image.open(".user772.png").resize((250,250))
		hl="tab.png"
		img4 = Image.open(hl).resize((600,50))
		#img2 = Image.open(".rank.png")
		title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 60)
		draw = ImageDraw.Draw(img3)
		draw.text((350,50), f"{data.author}",(255,255,0), font=title_font,align="right")
		draw.text((350,130), "LEVEL", (255, 0, 0), font=title_font)
		draw.text((490,130), f"{lvl}", (255, 255, 0), font=title_font)
		draw.text((710,130), f"EXP", (255, 0, 0), font=title_font)
		draw.text((790,130), f"{ex}", (255, 255, 0), font=title_font)
		img3.paste(img, (30,30))
		img3.paste(img4,(340,200))
		img3=img3.save(".ihhhh3.png")
		imggg=open(".ihhhh3.png","rb")
		print("done")
		msg=f"{data.author}"
		data.subClient.full_embed(f"ndc://x{data.comId}/user-profile/{data.author}",imggg,msg,data.chatId)

@client.command("block")
def block(args):
    if client.check(args,'staff','admin'):
        mention = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId).mentionUserIds
        for user in mention:
        	args.subClient.add_favorite_users(str(user))
        	#h=args.subClient.get_user_info(userId=str(user)).nickname
        	#args.subClient.client.block(userId=str(user))
        	#args.subClient.block(userId=str(user))
        	#args.subClient.send_message(args.chatId, f"<$@{h}$> is blocked from using Alexa!",mentionUserIds=[str(user)])



@client.command("unblock")
def unblock(args):
    if client.check(args,'staff','admin'):
        mention = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId).mentionUserIds
        for user in mention:
        	#h=args.subClient.get_user_info(userId=str(user)).nickname
        	#args.subClient.client.unblock(userId=str(user))
        	args.subClient.remove_favorite_users(str(user))
        	#args.subClient.unblock(userId=str(user))
        	#args.subClient.send_message(args.chatId, f"<$@{h}$> is unblocked from using Alexa!",mentionUserIds=[str(user)])

@client.command("setcoin")
def setcoin(args):
    if client.check(args, 'staff','admin') and not args.subClient.welcome_chat:
        args.subClient.set_welcome_chat(args.chatId)
        args.subClient.send_message(args.chatId, "Coin GC set!")
    else:
    	args.subClient.send_message(args.chatId,message="Admin Command")


@client.command("usetcoin")
def usetcoin(args):
    if client.check(args, 'staff','admin'):
        args.subClient.unset_welcome_chat()
        args.subClient.send_message(args.chatId, "Coin GC removed")
    else:
    	args.subClient.send_message(args.chatId,message="Admin command")

@client.command("urank")
def urank(data):
	mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user_id in mention:
		with open('users.json', 'r') as f:
			use = json.load(f)
			lvl = use[str(user_id)]['level']
			ex = use[str(user_id)]['experience']
			print(lvl ,ex)
			img2 = ("rank.png")
			nm=data.subClient.get_user_info(str(user_id)).nickname
		Image.open(img2).resize((1000, 300)).save("aniim.png")
		img3=Image.open("aniim.png")
		
		x=data.subClient.get_user_info(user_id).icon
		response=requests.get(f"{x}")
		file=open(".user772.png","wb")
		file.write(response.content)
		file.close()
		img = Image.open(".user772.png").resize((250,250))
		hl="tab.png"
		img4 = Image.open(hl).resize((600,50))
		#img2 = Image.open(".rank.png")
		title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 60)
		draw = ImageDraw.Draw(img3)
		draw.text((350,50), f"{nm}",(255,255,0), font=title_font)
		draw.text((350,130), "LEVEL", (255, 0, 0), font=title_font)
		draw.text((490,130), f"{lvl}", (255, 255, 0), font=title_font)
		draw.text((710,130), f"EXP", (255, 0, 0), font=title_font)
		draw.text((790,130), f"{ex}", (255, 255, 0), font=title_font)
		img3.paste(img, (30,30))
		img3.paste(img4,(340,200))
		img3=img3.save(".ihhhh3.png")
		imggg=open(".ihhhh3.png","rb")
		print("done")
		msg=f"{nm}"
		data.subClient.full_embed(f"ndc://x{data.comId}/user-profile/{user_id}",imggg,msg,data.chatId)

@client.on_all()
def text_mege(data):
  
  vl=data.subClient.get_chat_thread(data.chatId).title
  with suppress(Exception):
  	typ=["t.me/","Monetki","https:/t.me","aminoapps.com/p/bwazvk"]
  	content=data.message
  	if typ in content:
  	   	 rol=data.subClient.get_user_info(userId=data.authorId).json["role"]
  	   	 lvl=data.subClient.get_user_info(data.authorId).level
  	   	 if rol==0 and lvl==1:
  	   	 	try:
  	   	 		data.subClient.delete_message(data.chatId,data.messageId,asStaff=True,reason="Spam")
  	   	 		data.subClient.ban(userId=data.authorId,reason="Advertising in community")
  	   	 		tz = pytz.timezone('Asia/Kolkata')
  	   	 		now = datetime.now(tz)
  	   	 		current_time=now.strftime("%H:%M:%S")
  	   	 		chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
  	   	 		val=data.subClient.get_chat_thread(data.chatId).title
  	   	 		chats=data.subClient.favorite_chats
  	   	 		for id, in zip(chats):
  	   	 			data.subClient.send_message(chatId=id,message=f"""[c]{data.author} got banned for advertising

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{val}
{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
  	   	 	except:
  	   	 		pass


file = "old_messages.json"
filed = "deleted_messages.json"

try:
    with open(file, "r") as f:
        old_messages = json.load(f)
except Exception:
    old_messages = {}

try:
    with open(filed, "r") as f:
        deletd_messages = json.load(f)
except Exception:
    deletd_messages = {}

@client.command("snipe")
def snipe(data):
    
    messages = data.subClient.get_chat_messages(data.chatId,25).messageId
    for m in messages:
    	try:
    		gy=deleted_messages[data.chatId][m]
    		#values_view = gy
    		#value_iterator = iter(values_view)
    		#first_value = next(value_iterator)
    		data.subClient.send_message(data.chatId, message=f"""[c]Deleted message

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{gy}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
    	except Exception as e:
    		print(e)
    		pass


#@client.command("getdelete")
def gedelete(data):
    
    messages = data.subClient.get_chat_messages(data.chatId,10).messageId
    for m in messages:
    	try:
    		data.subClient.send_message(data.chatId, deleted_messages[data.chatId][m])
    	except Exception as e:
    		print(e)
    		pass

#@client.on_message()
def oldmge(data):
    if data.chatId not in old_messages.keys():
        old_messages[data.chatId] = {}
    old_messages[data.chatId][data.messageId] = data.message
    #file="old_messages.json"

    with open(file, "w") as f:
        json.dump(old_messages, f,indent=4)

#@client.on_message()
def on_meage(data):
    try:
    	tz = pytz.timezone('Asia/Kolkata')
    	now = datetime.now(tz)
    	current_time=now.strftime("%H:%M:%S")
    	chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
    	val=data.subClient.get_chat_thread(data.chatId).title
    	ch=data.subClient.favorite_chats
    	user_id = data.authorId
    	AID=client.get_user_info(userId=user_id).aminoId
    	cho=data.subClient.get_chat_thread(data.chatId).json['extensions']['coHost']
    	x=data.subClient.get_user_info(data.authorId).json['role']
    	y=data.subClient.get_chat_thread(data.chatId).json["uid"]
    	if user_id != client.userId and x==0:
    	       if user_id !=y and user_id not in cho:
    	       	if ANTI_SPAM.get(user_id) is None:
    	       		ANTI_SPAM[user_id] = int(time.time())
    	       	elif int(time.time()) - ANTI_SPAM[user_id] <= 0.5:
    	       	   	try:
    	       	   		data.subClient.kick(userId=user_id, chatId=data.chatId, allowRejoin=False)
    	       	   		for id in ch:
    	       	   			data.subClient.send_message(chatId=id,message=f"""[c]Kicked {data.author} for spam

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

GlobalId : https://aminoapps.com/u/{str(AID)}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
    	       	   	except Exception as e:
    	       	   		print(e)
    	       	   		pass
    	       	   		
    except:
    	pass              		
	
@client.on_member_join_chat()
def onjoin(data):
	names=["xaek","xaquaker","huesosaye228","huesos228"]
	nick=data.subClient.get_user_info(data.authorId).nickname
	lvl=data.subClient.get_user_info(data.authorId).level
	if nick in names and lvl==1:
		try:
			data.subClient.ban(userId=data.authorId,reason="Advertising in community")
			tz = pytz.timezone('Asia/Kolkata')
			now = datetime.now(tz)
			current_time=now.strftime("%H:%M:%S")
			chatlink=f"ndc://x{data.comId}/chat-thread/{data.chatId}"
			val=data.subClient.get_chat_thread(data.chatId).title
			chats=data.subClient.favorite_chats
			for id, in zip(chats):
				data.subClient.send_message(chatId=id,message=f"""[c]{data.author} got banned for Advertising

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

xaek
{chatlink}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Time : {current_time}""",embedTitle=f"{data.author}",embedLink=f"ndc://x{data.comId}/user-profile/{data.authorId}",embedContent=f"chat: {val}")
		except:
			pass
			
		
#@client.on_delete()
def getdel(data):
	if data.chatId not in deleted_messages.keys():
	   deleted_messages[data.chatId] = {}
	   try:
	       deleted_messages[data.chatId][data.messageId] = old_messages[data.chatId][data.messageId]
	       with open(filed, "w") as f:
	       	json.dump(deleted_messages, f, indent=4)
	   except KeyError:
	   	pass	

#@client.on_member_join_chat()
#@client.on_member_leave_chat()
def on_join_leave(data):
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
    	elif int(time.time()) - JOIN_LEAVE_DETECTOR[user_id] <= 0.5:
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
    	elif int(time.time()) - JOIN_LEAVE_DETECTOR[user_id] > 1:
    		JOIN_LEAVE_DETECTOR[user_id] = int(time.time())
    	

@client.command()
def prefix(args):
    if args.message and client.check(args,"staff","admin"):
        args.subClient.set_prefix(args.message)
        args.subClient.send_message(args.chatId, f"My prefix set as {args.message}")

@client.command()
def botlog(data):
	if client.check(data,'staff','admin'):
		data.subClient.add_favorite_chats(data.chatId)
		data.subClient.send_message(data.chatId,message="Botlog channel set")
		
@client.command()
def ubotlog(data):
	if client.check(data,'staff','admin'):
		data.subClient.remove_favorite_chats(data.chatId)
		data.subClient.send_message(data.chatId,message="Botlog channel removed")

@client.command()
def blg(data):
	data.subClient.add_favorite_chats(data.chatId)
	data.subClient.send_message(data.chatId,message="Botlog channel set")
		
@client.command()
def ublg(data):
	data.subClient.remove_favorite_chats(data.chatId)
	data.subClient.send_message(data.chatId,message="Botlog channel removed")
@client.command("json")
def create_community(data):
        with open(f'{path_amino}/{data.message}.json', 'w', encoding='utf8') as file:
            dict = {"welcome": "", "prefix": "!", "welcome_chat": "", "locked_command": [], "favorite_users": [], "favorite_chats": [], "banned_words": []}
            file.write(dumps(dict, sort_keys=False, indent=4))
            data.subClient.send_message(data.chatId,message=f"{data.message} file created")


@client.command("srm")
def srm(data):
	f = open("sids.txt", "r+")
	f.seek(0)
	f.truncate()
	data.subClient.send_message(data.chatId,message="Sid removed")
@client.command("sid")
def sid(data):
	exec(open('sidtxt.py').read())
	time.sleep(86200)
	f = open("sids.txt", "r+")
	f.seek(0)
	f.truncate()
	data.subClient.send_message(data.chatId,message="Sid script running")

@client.command()
def reboot(args):
        if client.check(args, "admin"):
        	args.subClient.send_message(args.chatId, "Restarting Bot")
        	os.execv(sys.executable, ['python'] + sys.argv)

@client.command("restart",condition=is_staff)
def restart(args):
        args.subClient.send_message(args.chatId, "Restarting Bot")
        os.execv(sys.executable, ["main.py", os.path.basename(sys.argv[0])])
        args.subClient.send_message(args.chatId,"bot is restarted")

@client.command("sidw")
def sidw(data):
	file = open('sids.txt', 'w') 
	file.write(f'{data.message}')
	file.close()
	data.subClient.send_message(data.chatId,message="sid changed")	
@client.command("coins", condition=is_black)
def coins(data):
	id=data.subClient.welcome_chat
	if id:
		if data.chatId==id:
			uid=data.authorId
			x=data.subClient.get_user_info(uid).icon
			response=requests.get(f"{x}")
			file=open(".sl9e.png","wb")
			file.write(response.content)
			file.close()
			imgg=open(".tvs.png","rb")
			img = open(".sl9e.png","rb")
			file = open('uss.txt', 'w') 
			file.write(f'{uid}')
			file.close()
			exec(open('tapcoin.py').read())
			data.subClient.send_message(data.chatId,message=f"""[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]Congrats <$@{data.author}$>
[c]You claimed 40+ coins
[c]Claim again after 24 hours
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
""",embedTitle='ᴍʏ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ'
,embedLink='https://youtube.com/c/techvision7',embedImage=imgg,embedContent='ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴡᴀᴛᴄʜ',mentionUserIds=[data.authorId])
			f = open("uss.txt", "r+")
			f.seek(0)
			f.truncate()
		else:
			chts=f"ndc://x{data.comId}/chat-thread/{id}"
			data.subClient.send_message(data.chatId,message=f"""
Send Coins command in this GC
{chts}
""",replyTo=data.messageId)
	else:
			data.subClient.send_message(data.chatId,message="Coin GC not set, ask Leader or Curator to set",replyTo=data.messageId)

deleted_messages=[]

keys = db.keys()
count2=len(keys)
if count2 >= 200:
  for k in keys:
    del db[k]
#print(keys)
def yoo():
  listt=[]
  dell=open("deleted.txt")
  for line in dell:
    listt.append(line.strip())
  return listt
#print(listt)
count=len(yoo())
if count  >= 50:
  open("deleted.txt","w").close()

@client.command("getdelete")
def getdelete(data):
  if data.chatId:
    messages = data.subClient.get_chat_messages(data.chatId, 10).messageId
    for m in messages:
      if m in yoo()[int(f"-{data.message}")]:
          print(m)
          if m in db.keys():
            value = db[m]
            try:
              data.subClient.send_message(chatId=data.chatId,message=f"author:{str(value).split()[0]}\nmessage:{str(value).split()[1]}")

            except:
              pass

@client.on_message()
def message(data):
  if data.chatId:
    db[data.messageId]=data.author+" "+data.message
    #print(db.keys())

@client.on_delete()
def remove(data):
    if data.chatId:
      d={}#b[.messageIdatad]="deleted"  
      s="echo "+f"{data.messageId}"+">>deleted.txt"
      system(s)

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