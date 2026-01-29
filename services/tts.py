import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak_once(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()
