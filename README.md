# Introduction
Hi, I am Yamakaze-chan, the creator of these code.   
I want to create something that could create transcription from my laptop speaker, so I created this. I have inspired by [Whisper](https://openai.com/index/whisper/) so I think I could try something with this. Then I found [faster-whisper](https://github.com/SYSTRAN/faster-whisper).   
If you feel interested in this, please don't forget to give bot **Whisper** and **faster-whisper** a star.
# How to run this????
I used [Miniconda](https://docs.anaconda.com/miniconda/) so I explain with *Miniconda* way.
- **Step 1:** Open ***Miniconda*** terminal
- **Step 2:** Use command to create virtual environment
```py
conda create --name <your_env_name> python=3.10
```
- **Step 3:** Activate virtual environment
```py
conda activate <your_env_name>
```
- **Step 4:** Install libraries
```py
pip install -r requirements.txt
```
- **Step 5:** Run this project
```py
python test.py
```
# Why my code is not running???
- ***I have no idea what is `small` in line 16 of test.py mean, but I don't see it anywhere in this code***   
  You can change line 5 of `whisper.py` with below line
  ```
    return WhisperModel(
        model_size_or_path = "small", 
        device="cpu", 
        local_files_only = False, 
        compute_type="int8")
  ```
  Please take a look at [this](https://github.com/SYSTRAN/faster-whisper) for more information.   
     
- ***Why i received `Error opening InputStream: Invalid number of channels` or the record did not record anything?***   
  Please take a look at line 7 of `get_output.py`, you have to change the index of device depend on your device you are using. Please take a look at [this](https://python-sounddevice.readthedocs.io/en/0.3.12/api.html#sounddevice.default) for more information.

### Please remember
- **Non-commercial**
- Have fun

Thank you and I hope this project can help you.