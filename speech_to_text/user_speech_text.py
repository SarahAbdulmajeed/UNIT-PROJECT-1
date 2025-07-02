"""PyAudio Example: Record a few seconds of audio and save to a wave file. https://people.csail.mit.edu/hubert/pyaudio/"""
import wave #Built in module 
import sys
import pyaudio
import whisper

FILE_NAME = 'speech_to_text/output.wav'

# Recording Settings 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100 #hz
RECORD_SECONDS = 20

def record_audio(): 
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        frames.append(stream.read(CHUNK))
    print("Done recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(FILE_NAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def transcript_audio():
    model = whisper.load_model("base")
    result = model.transcribe(FILE_NAME)
    return result["text"]
    
