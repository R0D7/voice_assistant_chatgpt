import wave
import pyaudio
import keyboard
import time

def speech_to_audiofiles_(speech_path):

    speech_wave = wave.open(speech_path, "wb")

    speech_wave.setnchannels(1)
    speech_wave.setsampwidth(2)
    speech_wave.setframerate(44100)

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    print("--")
    print("Talk now ... (press '-' to stop)")

    while True:
        data = stream.read(1024)
        speech_wave.writeframes(data)

        if keyboard.is_pressed("-"):
            print("--")
            time.sleep(0.5)
            break

    stream.stop_stream()
    stream.close()
    speech_wave.close()

    p.terminate()
