from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

try:
    # Connect to Wwise via the default IP & port
    with WaapiClient() as client:
        
        # Call ak.wwise.core.getInfo to get the global information of Wwise and store it in the variable 'result'
        result = client.call("ak.wwise.core.getInfo")
        # In order to avoid print single line printing, you need to use pprint to print the JSON result you just got
        pprint(result)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")
