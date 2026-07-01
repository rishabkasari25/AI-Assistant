import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 170)  # Set the speech rate (words per minute)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the voice (0

engine.say("Hello! I am your AI assistant. How can I help you today?")
engine.runAndWait()