# 1. Get global information
def get_global_info():
    # Query project information through getInfo
    return client.call("ak.wwise.core.getInfo")

# 2. Get the size of Sound SFX
def get_sfx_and_event_size(sound_sfx_guid):
    # Set the query parameter to the GUID of the object
    args = {
        "from": {
            "id": [
                sound_sfx_guid
            ]
        }
    }

    # Set the return value to the object name and transcoded size
    opts = {
        "return": [
            "name", "totalSize"
        ]
    }

    return client.call("ak.wwise.core.object.get", args, options=opts)

# 3. Get the size of the generated SoundBank
def get_soundbank_size(soundbank_guid):
    # 同上例
    args = {
        "from": {
            "id": [
                soundbank_guid
            ]
        }
    }

    # Set the return value to the path after the SoundBank is generated under the Windows platform
    opts = {
        "platform" : "Windows",
        "return": [
            "soundbank:bnkFilePath"
        ]
    }
    
     # Use os.path.getsize() to get the size of the obtained SoundBank address and convert it to MB
    path =  client.call("ak.wwise.core.object.get", args, options=opts)['return'][0]
    size = os.path.getsize(path) / (1024 ** 2)
    return size
