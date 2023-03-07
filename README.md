# Voice assistant chatGPT
This program is a voice assistant that utilizes Whisper API to transcribe audio to text and OpenAI's GPT-3 to generate responses. It is designed to be activated by a hotkey, and the user's spoken message is transcribed into text and used as input to GPT-3 to generate a response. The response is then synthesized into speech and played back to the user.

## Features
* Hotkey activation
* Speech-to-text transcription using the Whisper API
* Text-to-speech synthesis
* GPT-3 for natural language generation

## Requirements
* OpenAI API key
* Python 3.7 or higher
* Additional packages (listed in requirements.txt)

## Installation
1. Clone the repository by running 
```
git clone https://github.com/R0D7/voice_assistant_chatgpt.git
```
2. Install the required packages by running the following command :
```
pip install -r requirements.txt
```
3. You must enter your openai API key the first time you run the file (You can change it later by editing it in the file openai_api_key.txt)

## Usage
1. Run the program by assistant_r0d7.py
2. Press the hotkey (default is '+') to activate the assistant and speak your message.
3. Press the hotkey (default is '-') to receive the assistant's response.
4. Press the slash key ('/') to deactivate the assistant.

## Customization
* The hotkey can be changed by modifying the keyboard.read_key()=="*hotkey*" function in assistant_r0d7
* The GPT-3 model and configuration can be modified by changing the model and completion variables in assistant_r0d7.py (line 29). You can also replace the content value (line 14) to give a context for GPT-3.
