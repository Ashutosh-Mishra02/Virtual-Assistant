import datetime
import os
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour <= 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello sir, I am Jarvis. Please tell me how may I help you.")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('robertsharma40@gmail.com', '8764082729' )
    server.sendmail('robertsharma40@gmail.com', to, content)
    server.close()

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "None"

    return query

def open_application(application_name):
    if 'notepad' in application_name:
        os.system('notepad.exe')
    elif 'calculator' in application_name:
        os.system('calc.exe')
    # Add more applications as needed
    else:
        speak("Sorry, I cannot open that application.")

def perform_calculation(operation):
    try:
        result = eval(operation)
        speak(f"The result is {result}")
    except:
        speak("Sorry, I couldn't perform the calculation.")

def create_note():
    speak("What should I write?")
    note = takeCommand()
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    speak("Note has been created.")

def read_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.read()
            speak("Your notes are:")
            speak(notes)
    except FileNotFoundError:
        speak("No notes found.")

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    speak(random.choice(jokes))

def set_reminder(reminder, delay_seconds):
    speak(f"Setting a reminder for {reminder} in {delay_seconds} seconds.")
    time.sleep(delay_seconds)
    speak(f"Reminder: {reminder}")

def play_music():
    music_dir = 'C:/Users/ashum/Downloads/SOng'  # Replace with your music directory path
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))  # Plays the first song in the directory
    else:
        speak("No songs found in your music directory.")

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to ashutosh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ashuumishra04.as@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to fulfill the task right now.")

        elif 'open' in query:
            application_name = query.replace('open', '').strip()
            open_application(application_name)

        elif 'calculate' in query:
            operation = query.replace('calculate', '').strip()
            perform_calculation(operation)

        elif 'make a note' in query or 'create a note' in query:
            create_note()

        elif 'read notes' in query:
            read_notes()

        elif 'tell me a joke' in query:
            tell_joke()

        elif 'set a reminder' in query:
            speak("What is the reminder for?")
            reminder = takeCommand()
            speak("In how many seconds should I remind you?")
            delay = int(takeCommand())
            set_reminder(reminder, delay)

        elif 'play music' in query:
            play_music()

        elif 'exit' in query:
            speak("Goodbye!")
            break
