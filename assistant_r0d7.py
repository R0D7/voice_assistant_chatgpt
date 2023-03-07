import openai
import keyboard
import os
from speech_to_audiofiles.speech_to_audiofiles import speech_to_audiofiles_
from text_to_audio import text_to_audio
from speech_to_text import whisper_recognition
from speech_to_audiofiles.speech_to_audiofiles import speech_to_audiofiles_

# Get the path of speech.wav
path_speech = os.path.dirname(os.path.abspath(__file__)) + "\\speech_to_audiofiles\\speech.wav"

# Verify if you have an API key in openai_api_key.txt files and create it if not
if os.path.exists(os.path.dirname(os.path.abspath(__file__))+"\\openai_api_key.txt"):
    with open(os.path.dirname(os.path.abspath(__file__))+"\\openai_api_key.txt", "r") as f:
        api_key = f.read().strip()
else:
    api_key = input("Entrez votre clé API openai : ")

    with open(os.path.dirname(os.path.abspath(__file__))+"\\openai_api_key.txt", "w") as f:
        f.write(api_key)

openai.api_key  = api_key

# The dictionary will store the chat messages to keep track of the conversation history for ChatGPT
# The context of the message is specified in the value of the 'content' key in the messages dictionary
messages = [
    {"role": "system", "content": "You are a voice assistant"}
]

print("Assistant is ready ...")
i = True

while i is True:

    # If the user presses the "+" key, the program initiates speech recognition to record the user's message.
    if keyboard.read_key()== "+":
       # The speech_to_audiofiles_() function is called to record the user's voice and convert it into an audio file using the wave package.
        speech_to_audiofiles_(path_speech)
        # The user's audio message is transcribed to text using the whisper_recognition() function (which uses the whisper API) and added to the messages list.
        messages.append({"role": "user", "content": whisper_recognition(path_speech)})
        
        # API configuration
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages
        )
    
        # Extracting the ChatGPT response
        chat_response = completion.choices[0].message.content
        print(f'ChatGPT: {chat_response}')
        # Transcribing the ChatGPT response to audio
        text_to_audio(chat_response)

       # Adding the ChatGPT response to the messages list
        messages.append({"role": "assistant", "content": chat_response})

    # If the user presses the "/" key, the assistant deactivates.
    if keyboard.read_key()== "/":
        text_to_audio("Disabling assistant r0d7")
        print("Disabling assistant r0d7")
        print("--- POWER OFF ---")
        break
