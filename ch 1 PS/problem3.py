from gtts import gTTS
import os

# Text to convert
text = "My name is Osman."

# Convert text to speech
tts = gTTS(text=text, lang="en")

# Save the speech to an audio file
tts.save("speech.mp3")

# Play the audio file
os.system("start speech.mp3")  # Windows
# os.system("afplay speech.mp3")  # macOS
# os.system("mpg321 speech.mp3")  # Linux


