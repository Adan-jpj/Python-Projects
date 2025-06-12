import pyttsx3
import random

# Urdu jokes
jokes = [
    "بیوی: تم مجھ سے کتنا پیار کرتے ہو؟ شوہر: جتنا موبائل سے!",
    "استاد: اگر زمین سے سونا نکلے تو کیا بنے گا؟ شاگرد: سر خوشی!",
    "شوہر: میری بیوی مجھ سے بہت محبت کرتی ہے۔ دوست: کیوں؟ شوہر: ہر روز کہتی ہے تم مر کیوں نہیں جاتے!"
]

# Random joke
joke = random.choice(jokes)
print(joke)

# Initialize engine
engine = pyttsx3.init()

# Try to set Urdu voice if available
for voice in engine.getProperty('voices'):
    if 'urdu' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Speak
engine.say(joke)
engine.runAndWait()
