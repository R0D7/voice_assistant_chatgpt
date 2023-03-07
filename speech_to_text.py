import openai
def whisper_recognition():
    transcribe = openai.Audio.transcribe("whisper-1", open("path\\speech.wav", "rb"))
    print("User : ", transcribe["text"])
    return transcribe["text"]