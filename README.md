# Voice assistant chatGPT
This program is a voice assistant that utilizes Whisper API to transcribe audio to text and OpenAI's GPT-3 to generate responses. It is designed to be activated by a hotkey, and the user's spoken message is transcribed into text and used as input to GPT-3 to generate a response. The response is then synthesized into speech and played back to the user.

## Features
Hotkey activation
Speech-to-text transcription using the Whisper API
Text-to-speech synthesis
GPT-3 for natural language generation

## Requirements
* OpenAI API key
* Python 3.7 or higher
* Additional packages (listed in requirements.txt)

## Installation
1. Clone the repository.
2. Install the required packages by running pip install -r requirements.txt.
3. Replace "API_KEY" (line 9) in assistant_r0d7 by your API key.
4. Replace the the path in speech_to_audiofiles.py (line 8) and in speech_to_text.py (line 3) by the path of the speech.wav files (in speech_to_audiofiles directory)

## Usage
1. Run the program by assistant_r0d7.
2. Press the hotkey (default is '+') to activate the assistant and speak your message.
3. Press the hotkey (default is '-') to receive the assistant's response.
4. Press the slash key ('/') to deactivate the assistant.

## Customization
* The hotkey can be changed by modifying the keyboard.read_key()=="*hotkey*" function in assistant_r0d7
* The GPT-3 model and configuration can be modified by changing the model and completion variables in assistant_r0d7.py (line 29). You can also replace the content value (line 14) to give a context for GPT-3.