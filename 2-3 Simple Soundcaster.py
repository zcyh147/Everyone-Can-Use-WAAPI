# 1. Create a Transport Object for the object, and the GUID of the transport object will be returned after creation. For management convenience, we put the object name and the GUID of the transport strip object in the same dictionary as the function return value
from waapi import WaapiClient, CannotConnectToWaapiException

def transportX(object_guid):
    try:
        with WaapiClient() as client:
            # Set the query parameter to the GUID of the controllable object of the transport
            transport_args = {
                "object": object_guid
            }

            # The return value is the transport object ID in dictionary format, such as {'transport': 12}
            result_transport_id = client.call("ak.wwise.core.transport.create", transport_args)

            # Set the conditions through 'object_guid' and get the object name through ʻak.wwise.core.object.get`. Of course, if you directly pass in the object name above to create a transport object, you can also omit this step
            args = {
                "from": {
                    "id": [
                        object_guid
                    ]
                }
            }

            opts = {
                "return": [
                    "name"
                ]
            }
            
            # Call 'ak.wwise.core.object.get' to get the object name in dictionary format, such as {'name':'MyObjectName'}
            result_dict_name = client.call("ak.wwise.core.object.get", args, options=opts)['return'][0]

            # Combine the two dictionaries of object name and transport object ID to obtain a transport strip session with a dictionary structure like {'name':'MyObjectName','transport': 1234}
            return result_dict_name.update(result_transport_id)

    except CannotConnectToWaapiException:
        print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

# After obtaining the data in the 'dictionary + tape ID' format of multiple Transport Objects, you can put them in a list for storage. This structure is already a simple Soundcaster Session, for example:
# env_session = [{'name': 'MyObjectName1', 'transport': 1234}, {'name': 'MyObjectName2', 'transport': 12345}]

# 2. Obtain the Transport ID dictionary of the transport to be controlled from the Transport Session

def get_transport_args(env_session, object_name, play_state):
    # Traverse the list 'env_session' that stores the transport object Session, and get the dictionary 'transport_dict' corresponding to the given object name 'object_name'
    for i in env_session:
        if i['name'] == object_name:
            transport_dict = i
    
    # Obtain the dictionary corresponding to the ID of the transport object from the transport_dict, merge it with the play behavior dictionary, and prepare to pass it as a parameter
    transport_id = {'transport': transport_dict[transport]}
    args = {"action": play_state}
    return args.update(transport_id)

# 3. Take Transport Session, the transport object and playback behavior that need to be played in the Session as function parameters, obtain the parameters through the function in the second step, and remotely call 'executeAction' to control the playback behavior of the transport
from waapi import WaapiClient, CannotConnectToWaapiException

try:
    with WaapiClient() as client:
        args = get_transport_args(env_session, object_name, play_state)
        client.call("ak.wwise.core.transport.executeAction", args)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")
