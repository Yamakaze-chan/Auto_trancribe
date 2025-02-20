import sounddevice as REC
device_index =0
while (device_index < 28):
    try:
        # Command to get all devices listed: py -m sounddevice 
        # Device you want to record
        REC.default.device = device_index #You can change this with value based on your device
        # print(REC.default.device)

        # REC.default.channels = 4
        SAMPLE_RATE = int(REC.query_devices(device_index)['default_samplerate'])

        # print(f'Recording for {SECONDS} seconds')

        # Starts recording
        recording = REC.rec( int(1 * SAMPLE_RATE), samplerate = SAMPLE_RATE, channels=1)
        REC.wait()  # Waits for recording to finish
        print(device_index, REC.query_devices(device_index))
    except:
        print()
    finally:
        device_index = device_index + 1