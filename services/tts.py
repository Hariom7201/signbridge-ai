# services/tts.py
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()
