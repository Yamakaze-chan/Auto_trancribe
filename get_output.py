from scipy.io.wavfile import write
import sounddevice as REC

# Recording properties
SECONDS = 10

def get_speaker(filename, time, SAMPLE_RATE = 44100):
    # Command to get all devices listed: py -m sounddevice 
    # Device you want to record
    REC.default.device = [13, 3] #You can change this with value based on your device
    # print(REC.default.device)

    REC.default.channels = 1, 2

    # print(f'Recording for {SECONDS} seconds')

    # Starts recording
    recording = REC.rec( int(time * SAMPLE_RATE), samplerate = SAMPLE_RATE, channels = 1)
    REC.wait()  # Waits for recording to finish

    # Writes recorded data in to the wave file
    write(filename, SAMPLE_RATE, recording)