import pyttsx3
import os
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice, voices[2].id', value='1')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


if __name__ == '__main__':


    while True:
        speak("Hotword Detection Available")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "Hey, Beymax" or "Hey Baymax" or "Ok Beymax" or "Ok Baymax" or "Beymax" or "Ok Baymax" in statement:
            os.startfile("A:\AI-Personal-Voice-assistant-using-Python-master\AI-Personal-Voice-assistant-using-Python-master\venv\Baymax.py")


        if "Close Hotword Detection" in statement:
            speak('Hotword Detection is now shutting down!')
            print('Hotword Detection is now shutting down!')
            break
