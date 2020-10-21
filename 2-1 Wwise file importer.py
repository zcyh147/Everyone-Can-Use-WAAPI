# 1. Import audio files and create hierarchy
def file_import(file_path):
    # Define file import parameters, which include the file path and target path in the hard disk, and the target path includes the type definition of the created object
    # For non-voice Sound SFX object, importLanguage is set to SFX. importOperation is set to useExisting, which means that if the required container already exists, it will be replaced directly, if not, it will be created
    args_import = {
        "importOperation": "useExisting", 
        "default": {
            "importLanguage": "SFX"
        }, 
        "imports": [
            {
                "audioFile": file_path, 
                "objectPath": "\\Actor-Mixer Hierarchy\\Default Work Unit\\<Sequence Container>Test 0\\<Sound SFX>My SFX 0"
            }
        ]
    }
    # Define the result parameters to only return the information under the Windows, the information includes the GUID and the name of the created object
    opts = {
        "platform": "Windows",
        "return": [
            "id", "name"
        ]
    }

    return client.call("ak.wwise.core.audio.import", args_import, options=opts)

# 2. Set audio properties
def set_property(object_guid):
    # Set the target object in the parameter to the GUID of the object to be modified, the modified attribute is Volume, the platform of the object is Mac, and the value is modified to 10
    args_property = {
        "object": object_guid, 
        "property": "Volume", 
        "platform": "Windows", 
        "value": 10
    }

    client.call("ak.wwise.core.object.setProperty", args_property)

# 3. Create Event for Sound SFX and set playback rules
def set_event():
    # Create Event for a Sound SFX object and define its play behavior as play
    args_new_event = {
        # The upper half of the attributes are the path, type, name, and processing method when the name conflict is encountered after the event is created
        "parent": "\\Events\\Default Work Unit", 
        "type": "Event", 
        "name": "Play_SFX", 
        "onNameConflict": "merge", 
        "children": [
            {
                # Create a play behavior for it, leave the name blank, use ’@ActionType’ to define its play behavior as Play, '@Target' is the sound object being played
                "name": "", 
                "type": "Action", 
                "@ActionType": 1, 
                "@Target": "\\Actor-Mixer Hierarchy\\Default Work Unit\\Test 0\\My SFX 0"
            }
        ]
    }

    return client.call("ak.wwise.core.object.create", args_new_event{)

# 4. Create a SoundBank and add Event to it
def set_soundbank():
    # Create a Soundbank in the Default Work Unit in the SoundBanks folder
    args_new_event = {
        "parent": "\\SoundBanks\\Default Work Unit", 
        "type": "SoundBank", 
        "name": "Just_a_Bank", 
        "onNameConflict": "replace"
    }
    # Receive return value
    soundbank_info = client.call("ak.wwise.core.object.create", args_create_soundbank)

    # Add content to the newly created SoundBank, and put the Event created above into it
    args_set_inclusion = {
        "soundbank": "\\SoundBanks\\Default Work Unit\\Just_a_Bank", 
        "operation": "add", 
        "inclusions": [
            {
                # Here is the content to be put in Just_a_Bank, filter is which data to put into the SoundBank
                "object": "\\Events\\Default Work Unit\\Play_SFX", 
                "filter": [
                    "events", 
                    "structures",
                    "media"
                ]
            }
        ]
    }

    return client.call("ak.wwise.core.soundbank.setInclusions", args_set_inclusion)

# 5. Generate SoundBank
def generate_soundbank():
    # Set the name of the SoundBank to be exported and set it to write to disk
    args_generate_soundbank = {
        "soundbanks": [
            {
                "name": "Ambient"
            }
        ],
        "writeToDisk": True
    }

    return client.call("ak.wwise.core.soundbank.generate", args_generate_soundbank)