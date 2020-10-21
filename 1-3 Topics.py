from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

try:
    client = WaapiClient()

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

else:
    # Create the 'on_name_changed()' as a Callback Function in the subscription
    def on_name_changed(*args, **kwargs):
        # Get object type
        obj_type = kwargs.get("object", {}).get("type")
        # Get previous name
        old_name = kwargs.get("oldName")
        # Get new name
        new_name = kwargs.get("newName")

        # Use the format function to format the output information ({} represents the corresponding variable in the 'format()' function) to inform the user that the object of type XXX has been renamed from A to B
        print("Object '{}' (of type '{}') was renamed to '{}'\n".format(old_name, obj_type, new_name))
        # After the execution is complete, disconnect the WAMP connection. If you want to continue subscribing to information, you can also keep the connection
        client.disconnect()

    # Subscribe to the required topic, and use the callback function as the parameter one of the function. At the same time, use the option type as the second parameter, so that when the object name in Wwise is modified, the modified object type is returned
    handler = client.subscribe("ak.wwise.core.object.nameChanged", on_name_changed, {"return": ["type"]})

    # Print a message to remind the user that he has subscribed to 'ak.wwise.core.object.nameChanged' and suggest that the user perform a rename operation to verify that the script runs normally
    print("Subscribed 'ak.wwise.core.object.nameChanged', rename an object in Wwise")