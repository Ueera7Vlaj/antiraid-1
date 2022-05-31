from amino.lib.util import device
import hmac
import base64
import requests
from hashlib import sha1
from uuid import uuid4
sid = None
def sigug(data) -> str:
    return requests.post(f"https://bad-team.herokuapp.com/lool?data={data}").text
def sigg(data):
        key='f8e7a61ac3f725941e3ac7cae2d688be97f30b93'
        mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("42") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")

class Headers:
    def __init__(self, data = None, type = None, deviceId: str = None, sig: str = None):
        if deviceId:
            dev = device.DeviceGenerator(deviceId=deviceId)
        else:
            dev = device.DeviceGenerator()

        headers = {
            "NDCDEVICEID": dev.device_id,
            #"NDC-MSG-SIG": dev.device_id_sig,
            "Accept-Language": "en-US",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": dev.user_agent,
            "Host": "service.narvii.com",
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive"
        }

        if data:
            #print(data)
            headers["Content-Length"] = str(len(data))
            headers["NDC-MSG-SIG"] = sigg(data)
        if sid: headers["NDCAUTH"] = f"sid={sid}"
        if type: headers["Content-Type"] = type
        if sig: headers["NDC-MSG-SIG"] = sig
        self.headers = headers
 
 
