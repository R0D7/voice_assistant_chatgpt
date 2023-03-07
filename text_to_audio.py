import pyttsx3

def text_to_audio(speech):

    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()