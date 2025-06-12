import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# Initialize components
recognizer = sr.Recognizer() 
engine = pyttsx3.init()
newsapi = "d093053d72bc40248998159804e0e67d"
# Securely retrieve OpenAI API key
OPENAI_API_KEY = os.getenv("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")

def speak_old(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()


def speak(text):    
    tts = gTTS(text)
    tts.save('temp.mp3')
   

# Initialize pygame mixer
    pygame.mixer.init() 

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running so the music can play
    while pygame.mixer.music.get_busy():  
        pygame.time.Clock().tick(10)  # Wait for the music to finish
        



def aiProcess(command):
    """Processes the command using OpenAI's API."""
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts."},
            {"role": "user", "content": command}
        ]
    )
    
    return completion.choices[0].message.content  # Ensure the response is returned

def processCommand(command):
    """Executes the given voice command."""
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open twitter" in command:
        webbrowser.open("https://x.com/?lang=en") 
    elif command.startswith("play"):
        song = command.split(" ", 1)[1]  # Get song name safely
        song_link = musicLibrary.music.get(song)  # Use .get() to avoid KeyError

        if song_link:
            webbrowser.open(song_link)
        else: 
            speak("Sorry, I couldn't find that song in your library.")
    elif "news" in command:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            

            for article in articles[:5]:  # Limit to 5 headlines
                speak(article['title'])
        else:
            output = aiProcess(command)  # Get AI response
            speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis!...")  
    
    
    while True:
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=10)
                word = recognizer.recognize_google(audio).lower()

                if word == "jarvis":
                    speak("Yes?")

                    print("Listening for command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
        except Exception as e:
            print(f"Error: {e}")
