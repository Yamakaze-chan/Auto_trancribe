from scipy.io.wavfile import write
import sounddevice as REC

def checkSilence(x):
  if all(abs(sum(item) / len(item)) < 1e-03 for item in x):
    return False
  else:
    return True

# def get_speaker(filename, time, device_index):
#     # Command to get all devices listed: py -m sounddevice 
#     # Device you want to record
#     REC.default.device = [device_index, 3] #You can change this with value based on your device
#     print(REC.default.device)

#     REC.default.channels = 1, 2
#     print(REC.query_devices(device_index).keys())
#     SAMPLE_RATE = int(REC.query_devices(device_index)['default_samplerate'])
#     print(SAMPLE_RATE)
#     print(REC.query_devices(device_index)['max_input_channels'])

#     # print(f'Recording for {SECONDS} seconds')

#     # Starts recording
#     recording = REC.rec( int(time * SAMPLE_RATE), samplerate = SAMPLE_RATE)
#     REC.wait()  # Waits for recording to finish
#     temp_rec = recording
#     if (list(filter(checkSilence, temp_rec))): #If recorded silence, skip it
#         # Writes recorded data in to the wave file
#         write(filename, SAMPLE_RATE, recording)

def get_speaker(filename, time, device_index):
    # Command to get all devices listed: py -m sounddevice 
    # Device you want to record
    REC.default.device = device_index #You can change this with value based on your device
    # print(REC.default.device)

    # REC.default.channels = 4
    SAMPLE_RATE = int(REC.query_devices(device_index)['default_samplerate'])
    INPUT_CHANNELS = int(REC.query_devices(device_index)['max_input_channels'])
    # print(device_index, REC.query_devices(device_index))

    # print(f'Recording for {SECONDS} seconds')

    # Starts recording
    recording = REC.rec( int(time * SAMPLE_RATE), samplerate = SAMPLE_RATE, channels=INPUT_CHANNELS)
    REC.wait()  # Waits for recording to finish
    temp_rec = recording
    # print(temp_rec, temp_rec[0], sum(temp_rec[0])/ len(temp_rec[0]))
    if (checkSilence(temp_rec)): #If recorded silence, skip it
        # Writes recorded data in to the wave file
        write(filename, SAMPLE_RATE, recording)