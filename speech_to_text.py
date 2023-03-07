import openai
def whisper_recognition(speech_path):
    transcribe = openai.Audio.transcribe("whisper-1", open(speech_path, "rb"))
    print("User : ", transcribe["text"])
    return transcribe["text"]
