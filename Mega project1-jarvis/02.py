import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice commands."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("There was an error with the speech service.")
            return None

def process_command(command):
    """Process voice commands."""
    if "search for" in command:
        query = command.replace("search for", "").strip()
        speak(f"Searching for {query}")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak(f"Multiple results found. Try being more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find anything on that topic.")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit() 
    else:
        speak("Sorry, I didn't understand that.")

# Main loop
if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            process_command(command)


