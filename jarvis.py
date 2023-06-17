import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<=16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello sir, I am jarvis please tell me how may I help You")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('robertsharma40@gmail.com', '8764082729' )
    server.sendmail('robertsharma40@gmail.com', to , content)
    server.close()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if 1==1:
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikepedia")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        
        elif 'email to ashutosh' in query:
            try:
                speak("What could i say?")
                content = takeCommand()
                to = "ashuumishra04.as@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my master i am unable to fullfill the task right now")
        
        elif 'exit' in query:
            break





        




 

         




