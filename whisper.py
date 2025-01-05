from faster_whisper import WhisperModel

# init model
def initwhisper(model_size):
    return WhisperModel(model_size_or_path = model_size, device="cpu", local_files_only = True, compute_type="int8")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

# function for transcription
def whisper(model, filename):
    segments, info = model.transcribe(filename)
    # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    trancribe_arr = []
    for segment in segments:
        trancribe_arr.append([[segment.start, segment.end], segment.text, info.language]) #[[timeStart, timeEnd], text, lang]
    return trancribe_arr