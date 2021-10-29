import pyttsx3
import datetime 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def time():
    Time = datetime.datetime.now().strftime("%H:%M:")
    speak(Time)

def wishme():
    speak('Welcome Back Vishnu!')
    speak("The current date is") 
    date()
    speak("The current time is") 
    time()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("good Morning")
    elif hour >= 12 and hour <= 15:
        speak("Good afternoon")
    elif hour >=15 and hour <=23:
        speak("Good Evening") 
    else:
        speak("Good Night")        
    speak("I am  at your service. How can i Help You?")


wishme() 
 