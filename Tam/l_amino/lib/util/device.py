class DeviceGenerator:
    def __init__(self, deviceId=None):
        if deviceId:
            self.device_id = deviceId
        else:
            self.device_id = "4276D7C73F60B1D64F17046A9D9EA018E79E83640DE6890B4A80A3731B41B7D740A188EB2FFE617DF0"

        self.user_agent = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)"
