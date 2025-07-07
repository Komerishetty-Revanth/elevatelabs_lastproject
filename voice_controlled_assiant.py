import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import pyjokes

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your operator. How can I help you?")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='tel-in')
        print(f"User said: {query}\n")
    except Exception:
        speak("Sorry, I didn't get that. Could you say it again?")
        return ""
    return query.lower()

def run_assistant():
    greet()
    while True:
        command = listen_command()

        if 'open notepad' in command:
            speak("Opening Notepad.")
            os.system("notepad.exe")
             
        elif 'close notepad' in command:
            speak("Closing Notepad.")
            os.system("taskkill /f /im notepad.exe")

        elif 'open browser' in command:
            speak("Opening browser.")
            webbrowser.open("https://www.google.com")

        elif 'search for' in command:
          query = command.replace('search for', '').strip()
          speak(f"Searching for {query}")
          webbrowser.open(f"https://www.google.com/search?q={query}")
    
        elif 'close browser' in command:
         speak("Closing browser.")
         os.system("taskkill /f /im chrome.exe")
         os.system("taskkill /f /im msedge.exe")
         os.system("taskkill /f /im firefox.exe")


        elif 'what is the time ' in command or 'tell me the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'tell me a joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'open instagram' in command:
         speak("Opening Instagram.")
         webbrowser.open("https://www.instagram.com")

        elif 'search instagram for' in command:
         query = command.replace("search instagram for", "").strip().replace(" ", "%20")
         speak(f"Searching Instagram for {query}")
         webbrowser.open(f"https://www.instagram.com/explore/tags/{query}/")

        elif 'open profile' in command:
         username = command.replace("open profile", "").strip()
         speak(f"Opening Instagram profile of {username}")
         webbrowser.open(f"https://www.instagram.com/{username}/")

        elif 'open reels' in command:
         speak("Opening Instagram Reels.")
         webbrowser.open("https://www.instagram.com/reels/")
       
        
        elif 'exit' in command or 'quit' in command or 'stop' in command:
         speak("Goodbye!")
         break

        elif command:
         speak("Sorry, I can't do that yet.")

if __name__ == "__main__":
    run_assistant()

