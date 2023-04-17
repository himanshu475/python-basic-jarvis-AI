from datetime import datetime

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  #0 for boy, 1 for girl

# print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour >=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good night")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Wait....")
        query=r.recognize_google(audio, language='en-in')
        print("User said : "+(query))

    except Exception as e:
        speak("Say that again please.....")
        return "none"
    return query.lower()
def sendemail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('himanshusali60@gmail.com', 'Himanshu&123')
    server.sendmail('himanshusali60@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    
    speak("i am virtual assitance kira, how can i help you?")
    while True:
        query=takecommand()

        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'play music' in query:
            music_dir="D:\\music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strtime}")
        elif 'open vscode' in query:
            codepath="C:\\Users\\himan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)
        elif 'email to himanshu' in query:
            try:
                speak("What should i say")
                content=takecommand()
                to="himanshusali57@gmail.com"
                sendemail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, could not send email")
        elif 'quit' or 'exit' in query:
            exit()
   
