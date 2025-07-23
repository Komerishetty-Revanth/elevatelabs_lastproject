import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import pyjokes

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   
is_muted=False

def speak(text):
    global is_muted
    if not is_muted:
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
        query = r.recognize_google(audio, language='en-in')
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

        elif 'open settings' in command:
         speak("Opening Settings.")
         os.system("start ms-settings:")    

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


        elif 'what is the time' in command or 'tell me the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'tell me a joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'open insta'  in command:
         speak("Opening Instagram.")
         webbrowser.open("https://www.instagram.com")

        elif 'open facebook' in command:
         speak("opening facebook")
         webbrowser.open("https://www.facebook.com")  

        elif 'open linkedln' in command:
         speak("opening linkedin")
         webbrowser.open("https://www.linkedln.com")

        elif 'open youtube' in command:
         speak("Opening YouTube.")
         webbrowser.open("https://www.youtube.com")

        elif 'open whatsapp' in command:
         speak("Opening WhatsApp.")
         webbrowser.open("https://web.whatsapp.com")

        elif 'open reels' in command:
         speak("Opening Instagram Reels.")
         webbrowser.open("https://www.instagram.com/reels/")
         
        elif 'open twitter' in command:
         speak("Opening Twitter.")
         webbrowser.open("https://www.twitter.com")

        elif 'open google' in command:
         speak("Opening Google.")
         webbrowser.open("https://www.google.com")

        elif 'open gmail' in command:
         speak("Opening Gmail.")
         webbrowser.open("https://mail.google.com")

        elif 'open calculator' in command:
         speak("Opening Calculator.")
         os.system("calc.exe")


        elif 'exit' in command or 'quit' in command or 'stop' in command:
         speak("Goodbye!")
         break

        elif command:
         speak("Sorry, I can't do that yet is not in my capabilities.")

if __name__ == "__main__":
    run_assistant()                        
