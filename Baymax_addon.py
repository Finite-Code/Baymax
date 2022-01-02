import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
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
import os
import cv2
import random
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import requests
import pyautogui
from email.mime.text import MIMEText
from requests import get
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

# ###############################################################################################################################
# ###############################################################################################################################

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am cody sir. please tell me how may i help you")


"""    
#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ADDRESS', 'YOUR PASSWORD')
    server.sendmail('YOUR EMAIL ADDRESS', to, content)
    server.close()
 """


# for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="YOUR_API_HERE"'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


if __name__ == "__main__":  # main program
    wish()
    while True:
        # if 1:

        query = takecommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "A:\\music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))



        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+918104035661", "Hi This is CODY", 4, 13)
            time.sleep(1)
            speak("message has been sent")

        elif "song on youtube" in query:
            kit.playonyt("sunflower")

        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')

            time.sleep(timing)
            speak('Your time has been finished sir')
        """
        elif "email to atharva" in query:
           try:
               speak("what should i say?")
               content = takecommand().lower()
               to = "EMAIL OF THE OTHER PERSON"
               sendEmail(to,content)
               speak("Email has been sent to atharva")
           except Exception as e:
               print(e)
               speak("sorry sir, i am not able to sent this mail to atharva")

             """

        """elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()"""

    # to close any application
    """elif "close notepad" in query:
    speak("okay sir, closing notepad")
    os.system("taskkill /f /im notepad.exe")"""

# to set an alarm
elif "set alarm" in query:
    nn = int(datetime.datetime.now().hour)
    if nn == 22:
        music_dir = 'A:\\Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
# to find a joke
elif "tell me a joke" in query:
    joke = pyjokes.get_joke()
    speak(joke)

elif "shut down the system" in query:
    os.system("shutdown /s /t 5")

elif "restart the system" in query:
    os.system("shutdown /r /t 5")

elif "sleep the system" in query:
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



###########################################################################################################################################
###########################################################################################################################################

elif 'switch the window' in query:
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.keyUp("alt")


elif "tell me news" in query:
    speak("please wait sir, feteching the latest news")
    news()


elif "email to atharva" in query:

    speak("sir what should i say")
    query = takecommand().lower()
    if "send a file" in query:
        email = 'finitecode.contact@gmail.com'  # Your email
        password = 'ge120110'  # Your email account password
        send_to_email = 'neelamsandeep85@gmail.com'  # Whom you are sending the message to
        speak("okay sir, what is the subject for this email")
        query = takecommand().lower()
        subject = query  # The Subject in the email
        speak("and sir, what is the message for this email")
        query2 = takecommand().lower()
        message = query2  # The message in the email
        speak("sir please enter the correct path of the file into the shell")
        file_location = input("please enter the path here")  # The File attachment in the email

        speak("please wait,i am sending email now")

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Setup the attachment
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # Attach the attachment to the MIMEMultipart object
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
        speak("email has been sent to atharva")

    else:
        email = 'finitecode.contact@gmail.com'  # Your email
        password = 'ge120110'  # Your email account password
        send_to_email = 'neelamsandeep85@gmail.com'  # Whom you are sending the message to
        message = query  # The message in the email

        server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
        server.starttls()  # Use TLS
        server.login(email, password)  # Login to the email server
        server.sendmail(email, send_to_email, message)  # Send the email
        server.quit()  # Logout of the email server
        speak("email has been sent to atharva")

    if "good bye" in query or "ok bye" in query or "stop" in query:
        speak('your personal assistant cody is shutting down,Good bye')
        print('your personal assistant cody is shutting down,Good bye')
        sys.exit()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "tell me a joke" or "say me a joke" in query:
        speak(speak_print_joke)
        print(speak_print_joke)

    elif 'open youtube' in query:
        speak("Opening Youtube...")
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        time.sleep(5)

    elif 'youtube' in query:
        speak("Opening Youtube...")
        queryyt = query.replace("youtube", "", "")
        webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={queryyt}")
        speak("youtube is open now")
        time.sleep(5)

    elif 'open google' in query:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in query:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now")
        time.sleep(5)

    elif "weather" in query:
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



    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    elif 'who are you' in query or 'what can you do' in query:
        speak("You've got this, I'm cody You Say I do, I can make "
              "sandwiches to juices... Ummm Something's wrong wait a second."
              "So I can send emails help you in daily tasks i try"
              "to learn as much as i can from your daily activites"
              "Just ask me a fun fact or search to the web and i will make sure you have it.")


    elif "who made you" in query or "who created you" in query or "who discovered you" in query:
        speak("I was built by Atharva")
        print("I was built by Atharva")

    elif "open stackoverflow" in query:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        speak("Here is stackoverflow")

    elif 'news' in query:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home")
        speak('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    elif 'headlines' in query:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "robo camera", "img.jpg")

    elif 'search' in query:
        query = query.replace("search", "")
        webbrowser.open_new_tab(query)
        time.sleep(5)

    elif 'ask' in query:
        speak('I can answer to computational and geographical questions and what question do you want to ask now')
        question = takeCommand()
        app_id = "R2K75H-7ELALHR35X"
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
        print(answer)

    elif "open spotify" in query:
        webbrowser.open_new_tab("https://open.spotify.com")

    elif "play" in query:
        query_spotify = query.replace("play", "", "")
        webbrowser.open_new_tab(f"https://open.spotify.com/search={query_spotify}")

    elif "sing a song" in query:
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

    elif "pop up me notification" in query:
        notification.notify(title="hi", message="it's a message", timeout=10)

    elif "set a reminder" or "remind me" in query:
        print("What shall I remind you about?")
        speak("What shall I remind you about?")
        text = str(input())
        print("In how many minutes?")
        speak("In how many minutes?")
        local_time = float(input())
        local_time = local_time * 60
        time.sleep(local_time)
        notification.notify(title=f"Reminder: {text}", message=f"{text}", timeout=12, app_name="cody")
        print(text)
