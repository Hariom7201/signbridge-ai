import pyttsx3
import threading

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

is_speaking = False

def _speak_async(text):
    global is_speaking
    is_speaking = True
    engine.say(text)
    engine.runAndWait()
    is_speaking = False

def speak(text):
    global is_speaking
    if is_speaking:
        return  # ignore if already speaking
    t = threading.Thread(target=_speak_async, args=(text,))
    t.start()
