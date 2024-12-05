import pyjokes
import pyttsx3

engine = pyttsx3.init()
print(pyjokes.get_joke())
engine.say("my name is shubh patel")
engine.runAndWait()
