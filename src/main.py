# JARVIS - Voice Controlled AI Assistant

# Environment
from dotenv import load_dotenv
import os
load_dotenv()

# Standard Libraries
import webbrowser

# Third-Party Libraries
import speech_recognition as sr
import pyttsx3
import requests
from google import genai

# Local Modules
import musicLibrary

# API Keys
newsapi = os.getenv("NEWS_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not newsapi:
    raise ValueError("NEWS_API_KEY not found in .env file")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Gemini Client
client = genai.Client(api_key=gemini_api_key)

# Constants
VOICE_RATE = 170
VOICE_INDEX = 1
LISTEN_TIMEOUT = 2
PHRASE_TIME_LIMIT = 10
AMBIENT_NOISE_DURATION = 0.5
NEWS_ARTICLE_LIMIT = 5

# Text-to-Speech Engine
engine = pyttsx3.init()
response_mode = "normal"

engine.setProperty("rate", VOICE_RATE)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[VOICE_INDEX].id)

# Speak Text
def speak(text):
    engine.say(text)  # abhi bolta nhi
    engine.runAndWait()  # ab bolta he, bolna complete hone ka wait krta he


# AI Processing
def ai_process(command):
    global response_mode
    try:
        if response_mode == "short":
            prompt = f"You are Jarvis. Reply in 1 short sentences only. User: {command}"
        elif response_mode == "normal":
            prompt = f"You are Jarvis. Reply in 2-3 short sentences only. User: {command}"
        else:
            prompt = f"You are Jarvis. Reply in 4-5 short sentences only. User: {command}"
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return response.text
    except Exception:
        return "Sorry sir, AI service is currently unavailable."

# Websites
WEBSITES = {
    "open google": "https://www.google.com",
    "open linkedin": "https://www.linkedin.com/in/muhammadhaseeb997/",
    "open youtube audio library": "https://www.youtube.com/playlist?list=PL6ZNwyxUtD27vHO9BfveOM6lLzSBMb9tL",
    "open youtube": "https://www.youtube.com",
    "open instagram": "https://www.instagram.com",
    "open agency portal": "https://sixalpsportal.vercel.app/staff",
    "open calculus corner": "https://www.calculuscorner.com",
    "open github": "https://github.com/Haseeb-997",
    "open agency": "https://www.sixalps.com",
    "open data science course" : "https://www.youtube.com/playlist?list=PLaldQ9PzZd9qPYGj4aWUXitBlfWz72e9m"
}

# Command Processing
def process_command(command):
    print(command)
    global response_mode

    if "detail mode" in command:
        response_mode = "detailed"
        speak("Detailed mode activated.")
    elif "normal mode" in command:
        response_mode = "normal"
        speak("Normal mode activated.")
    elif "short mode" in command:
        response_mode = "short"
        speak("Short mode activated.")

    for key, url in WEBSITES.items():
        if key in command:
            webbrowser.open(url)
            return

    if command.startswith("play"):
        song = command[5:].strip()

        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry, I couldn't find that song.")

    elif "music library" in command or "list songs" in command:
        speak("Here are the available songs.")
        print("\nAvailable Songs:")
        print("-" * 30)
        speak(f"You have {len(musicLibrary.music)} songs in your library.")
        for i, song in enumerate(musicLibrary.music.keys(), start=1):
            print(f"{i}. {song.title()}")
            speak(song.title())

    elif "news" in command:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            r.raise_for_status()

            data = r.json()
            articles = data.get("articles", [])

            if not articles:
                speak("No news received.")
            else:
                speak("Here are today's top headlines.")
                for i, article in enumerate(articles[:NEWS_ARTICLE_LIMIT], start=1):
                    speak(f"News {i}")
                    speak(article["title"])

        except requests.RequestException:
            speak("Unable to fetch the news right now.")

    else:
        output = ai_process(command)
        speak(output)

# Main Program
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()  # object that understand speech "speech_recognition.Recognizer"

        try:
            with sr.Microphone() as source:
                # temporary resource use karo, kam khatam -> automatically close
                # source microphone ko represent karega
                print("\nListening...")
                r.adjust_for_ambient_noise(source, duration=AMBIENT_NOISE_DURATION)
                # Ambient noise -> Fan, AC, Keyboard, Room noise | recognizer 0.5 second tak sunta hai,
                # estimate karta hai, ye background noise hai, taake baad me sirf tumhari voice pe focus kare
                audio_text = r.listen(source, timeout=LISTEN_TIMEOUT, phrase_time_limit=PHRASE_TIME_LIMIT)
                # listen() source se audio record krta he, agr 2 sec tak na bola to "WaitTimeoutError exception" dega,
                # 5 sec tak recognize kare ga uske baad recording stop
                # audio_text -> abhi ye text nahi hai, sirf audio hai
                print("Time over")  # Ye tab print hoga jab recording complete ho jayegi

            # using google speech recognition
            word = r.recognize_google(audio_text).lower()
            if "jarvis" in word:
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    r.adjust_for_ambient_noise(source, duration=AMBIENT_NOISE_DURATION)
                    audio_text = r.listen(source, timeout=LISTEN_TIMEOUT, phrase_time_limit=PHRASE_TIME_LIMIT)
                    command = r.recognize_google(audio_text).lower()
                    process_command(command)

        except sr.WaitTimeoutError:  # agar 5 sec tak tumne bolna start nahi kiya
            print("No speech detected.")

        except sr.UnknownValueError:  # Speech mili, lekin Google samajh nahi paya
            print("Couldn't understand.")

        except sr.RequestError as e:  # Google server tak request hi nahi gayi
            print(f"Speech service error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")