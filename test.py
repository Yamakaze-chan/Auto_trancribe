import os
from pathlib import Path
from get_output import get_speaker
from whisper import initwhisper, whisper
import threading
import uuid
import keyboard

# Sorted files by created time and get the oldest one
def get_oldest_file(path):
    if len(os.listdir("./pendingFile/")) == 0:
        return None
    return sorted(Path(path).iterdir(), key=os.path.getmtime)[0].__str__()

# init datas
model_type = "small"
model = initwhisper("./"+model_type)
pathFolder = "./pendingFile/"
temp_var = True

# Get sound from your speaker
def get_sound():
    while(temp_var):
        filename = pathFolder+str(uuid.uuid4())+".wav"
        get_speaker(filename, 10, 10) #I am using Stereo Mix, but it would be better if you have better way to record the output sound

# Get transcription from recorded files
def get_transcribe():
    while(temp_var or get_oldest_file("./pendingFile/") != None):
        filename = get_oldest_file("./pendingFile/")
        if(filename):
            transcriptions = whisper(model, filename)
            for trans in transcriptions:
                print(trans[1])
            os.remove(filename)

# Using thread to keep record sound even when transcription is in progress
t1 = threading.Thread(target=get_sound)
t2 = threading.Thread(target=get_transcribe)

t1.start()
t2.start()

print("Start record")
while(1):
    if keyboard.is_pressed("p"):
        print("aaaaaaaaaaaaaaaa") #Just to check if the key 'p' is pressed
        temp_var = False
        t1.join()
        t2.join()
        break
