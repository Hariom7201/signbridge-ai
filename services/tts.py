import pyttsx3

_engine = pyttsx3.init()
_last_spoken = ""

def speak_once(text):
    global _last_spoken
    if text != _last_spoken:
        _engine.say(text)
        _engine.runAndWait()
        _last_spoken = text
