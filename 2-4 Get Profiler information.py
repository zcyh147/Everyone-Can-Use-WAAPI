# 1. Start profiler data acquisition, and return to the start time
def start_capture():
    return client.call("ak.wwise.core.profiler.startCapture")

# 2. End Profiler data acquisition and return the time
def stop_capture():
    return client.call("ak.wwise.core.profiler.startCapture")

# 3. Obtain information from the captured data. Note that the value range of 'cursor_time' needs to be between 'start_capture()' and 'stop_capture()'
def capture_log_query(cursor_time):
    # Set the time point to query
    args_times = {
        "time": cursor_time
    }

    # Get the name of the voice at the current time point, whether it is a Virtual, and the name and ID of the game object related to it
    opts_get_voices = {
        "return": [
            "objectName", "isVirtual", "gameObjectName", "gameObjectID"
        ]
    }
    
    # Get the Bus that exists at the current point in time
    opts_get_busses = {
        "return": [
            "objectName"
        ]
    }

    # Returns the currently active RTPC ID and value
    log_rtpcs = client.call("ak.wwise.core.profiler.getRTPCs", args_times)["return"]
    log_voices = client.call("ak.wwise.core.profiler.getVoices", args_times, options=opts_get_voices)["return"]
    log_busses = client.call("ak.wwise.core.profiler.getBusses", args_times, options=opts_get_busses)["return"]