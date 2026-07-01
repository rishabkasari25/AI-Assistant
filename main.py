import datetime
import webbrowser
import random
import os
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


print("="*40)
print("AI Assistant")
print("="*40)

name = input("What is your name? ")
print("calling speak...")
speak(f"welcome,{name}!")
print("speak finished")

while True:
    recognizzer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizzer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizzer.listen(source)
    try:
        command = recognizzer.recognize_google(audio).lower()
        print("you said: " , command)
    except Exception:
        speak("Sorry, I didn't understand that.")
        continue

    if command == "hello":
        print("speak function called")
        speak(f"Hello, {name}! How can I assist you today?")
    elif command == "time":
        speak(f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}")
        print(f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}")
    elif command == "today's date":
        speak(f"Today's date is {datetime.datetime.now().strftime('%d-%m-%Y')}")
        print(f"Today's date is {datetime.datetime.now().strftime('%d-%m-%Y')}")
    elif command == "open google":
        query = input("What do you want to search on Google? ")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif command == "open youtube":
        query = input("What do you want to search on YouTube? ")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif command == "funny joke":
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why did the bicycle fall over? Because it was two-tired!"
        ]
        speak(random.choice(jokes))
    elif command == "notepad":
        os.system("notepad")
    elif command == "calc":
        os.system("calc")
    elif command == "vs code":
        os.system("code")
    elif command == "git hub":
        webbrowser.open("https://www.github.com")
    elif command == "chat gpt":
        webbrowser.open("https://chat.openai.com")
    elif command.startswith("search "):
        query = command.replace("search ", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif command == "calculator":
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
          speak(f"The answer is {num1 + num2}")

        elif operator == "-":
          speak(f"The answer is {num1 - num2}")

        elif operator == "*":
          speak(f"The answer is {num1 * num2}")

        elif operator == "/":
            if num2 != 0:
                speak(f"The answer is {num1 / num2}")
            else:
                speak("Error: Division by zero is not allowed.")
        else:
            speak("Invalid operator.")

    elif command == "note":
        note = input("Enter your note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        speak("Note saved.")

    elif command == "show notes":
        try:
            with open("notes.txt", "r") as file:
                print("\nYour notes:")
                print(file.read())
        except FileNotFoundError:
            speak("No notes found.")

    elif command == "exit":
        speak("Goodbye!")
        break

    else:
        speak("Invalid command. Please try again.")