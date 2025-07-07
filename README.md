# elevatelabs_lastprojects
project1:
🗣️ Python Voice Assistant 
This is a voice-activated personal assistant written in Python. It listens to your commands in English and performs a variety of tasks like opening applications, browsing the internet, telling jokes, and interacting with Instagram.

✅ Features
🎤 Voice Recognition (English - en-in)

💬 Text-to-Speech Responses

🕒 Tells Current Time

📝 Open/Close Notepad

🌍 Search Google

🔍 Browse the Web

🤣 Tells Programming Jokes

📸 Interact with Instagram

🛑 Quit on Command

🧰 Requirements
Install the required Python libraries:

bash
Copy
Edit
pip install SpeechRecognition pyttsx3 pyjokes pyaudio
⚠️ If you face errors installing pyaudio, run:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
▶️ How to Use
Make sure your microphone is connected and working.

Save the script as voice_assistant.py.

Run the script:

bash
Copy
Edit
python voice_assistant.py
Say commands like:

open notepad

close notepad

open browser

search for weather in London

tell me a joke

what is the time

open instagram

search instagram for travel

open profile nasa

open reels

exit / stop / quit to close the assistant

🧠 Supported Voice Commands
Command	Action
"open notepad"	Opens Notepad
"close notepad"	Closes Notepad
"open browser"	Opens default web browser to Google
"search for [query]"	Google search for your query
"close browser"	Closes Chrome, Edge, and Firefox
"tell me the time"	Speaks current time
"tell me a joke"	Tells a random programming joke
"open instagram"	Opens Instagram
"search instagram for [tag]"	Opens Instagram tag search
"open profile [username]"	Opens specific Instagram user profile
"open reels"	Opens Instagram Reels page
"exit" / "quit" / "stop"	Exits the assistant

📌 Notes
Speech recognition uses Google’s online service, so an internet connection is required.

TTS (text-to-speech) works offline.

If Instagram links don't open as expected, ensure you're logged in or using a supported browser.

📄 License
This project is open-source and free to use for personal and educational purposes.
