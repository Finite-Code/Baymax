import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
from plyer import notification
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice, voices[1].id', value='1')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 4:
        speak("Hello, I guess it's midnight")
        print("Hello, I guess it's midnight")

    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")

    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"You Said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your AI personal assistant Beymax")
wishMe()

if __name__ == '__main__':

    while True:
        speak("How can I help you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Beymax is shutting down,Good bye')
            print('your personal assistant Beymax is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            speak("Opening Youtube...")
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'youtube' in statement:
            speak("Opening Youtube...")
            statementyt = statement.replace("youtube", "", "")
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={statementyt}")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak("You've got this, I'm Beymax You Say I do, I can make "
                  "sandwiches to juices... Ummm Something's wrong wait a second."
                  "So I can send emails help you in daily tasks i try"
                  "to learn as much as i can from your daily activites"
                  "Just ask me a fun fact or search to the web and i will make sure you have it.")


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Atharva")
            print("I was built by Atharva")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'headlines' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "open spotify" in statement:
            webbrowser.open_new_tab("https://open.spotify.com")

        elif "play" in statement:
            statement_spotify = statement.replace("play", "", "")
            webbrowser.open_new_tab(f"https://open.spotify.com/search={statement_spotify}")

        elif "sing a song" in statement:
            speak("Ayy, ayy, ayy, ayy (ooh)"
                  "Ooh, ooh, ooh, ooh (ooh) Ayy, ayy Ooh, ooh, ooh, ooh"
                  "Needless to say, I keep her in check"
                  "She was a bad-bad, nevertheless (yeah)"
                  "Callin' it quits now, baby, I'm a wreck (wreck)"
                  "Crash at my place, baby, you're a wreck (wreck)"
                  "Needless to say, I'm keeping her in chec"
                  "She was all bad-bad, nevertheless"
                  "Callin' it quits now, baby, I'm a wreck"
                  "Crash at my place, baby, you're a wreck"
                  "Thinkin' in a bad way, losin' your grip"
                  "Screamin' at my face, baby, don't trip"
                  "Someone took a big L, don't know how that felt"
                  "Lookin' at you sideways, party on tilt"
                  "Ooh-ooh-ooh"
                  "Some things you just can't refuse"
                  "She wanna ride me like a cruise"
                  "And I'm not tryna lose")

        elif "pop up me notification" in statement:
            notification.notify(title="hi", message="it's a message", timeout=10)

        elif "set a reminder" or "remind me" in statement:
            print("What shall I remind you about?")
            speak("What shall I remind you about?")
            text = str(input())
            print("In how many minutes?")
            speak("In how many minutes?")
            local_time = float(input())
            local_time = local_time * 60
            time.sleep(local_time)
            notification.notify(title=f"Reminder: {text}", message=f"{text}", timeout=12, app_name="Baymax")
            print(text)

        def make_request(url):
            response = requests.get(url)
            return response.text

time.sleep(3)
