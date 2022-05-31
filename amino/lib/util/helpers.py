import json
import requests
import names
from hashlib import sha1
from functools import reduce
from base64 import b85decode, b64decode
import random
import hmac
import platform,socket,re,uuid 
def dev():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    mac = hmac.new(bytes.fromhex('02b258c63559d8804321c5d5065af320358d366f'), b"\x42" + identifier, sha1)
    return (f"42{identifier.hex()}{mac.hexdigest()}").upper()
def devi() -> str:
    link = requests.get("https://pastebin.com/raw/a6BJ9suL").text
    api = f"{link}"
    device = requests.get(f"{api}/man").text
    return device
def generate_device_info():
    try:
        deviceId=dev()
    except:
        deviceId ="17925AEBB52F0AB6309A4D963914DD5ABBA536CE2ACC53643300942EF82983B504AF220835D92B95DB"

    return {
        "device_id": deviceId,
        "device_id_sig": "Aa0ZDPOEgjt1EhyVYyZ5FgSZSqJt",
        "user_agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)"
    }
def generte_device_id() -> str:
    link = requests.get("https://pastebin.com/raw/a6BJ9suL").text
    api = f"{link}"
    device = requests.get(f"{api}/man").text
    return device
def genrate_device_info():
    return {
        "device_id": generate_device_id(),
        "user_agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.5.33562)"
    }

# okok says: please use return annotations :(( https://www.python.org/dev/peps/pep-3107/#return-values

def decode_sid(sid: str) -> dict:
    return json.loads(b64decode(reduce(lambda a, e: a.replace(*e), ("-+", "_/"), sid + "=" * (-len(sid) % 4)).encode())[1:-20].decode())

def sid_to_uid(SID: str) -> str: return decode_sid(SID)["2"]

def sid_to_ip_address(SID: str) -> str: return decode_sid(SID)["4"]
