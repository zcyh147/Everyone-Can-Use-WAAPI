from waapi import WaapiClient, CannotConnectToWaapiException

# try…except…: Exception handling function of Python
try:
    # Connect to Wwise through the default address, if you want to connect to a different local Wwise, you can modify the port number here
    with WaapiClient() as client:

        # Both the incoming and outgoing parameters of WAAPI use JSON format. We use a dictionary to define the information to be printed as 'Hello Wwise!'
        print_args = {
            "message": "Hello Wwise!"
        }
        # Call ak.soundengine.postMsgMonitor remotely with the parameters set above
        client.call("ak.soundengine.postMsgMonitor", print_args)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")