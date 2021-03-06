import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('Yes Boss How can I help you...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if "alexa" in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        print('Exception')
        pass


def run_payu():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        talk('playing' + song)
        print(song)

    elif 'who the hell is' in command:
        person = command.replace('who the hell is', '')
        info = wikipedia.Summary(person, 2)
        talk(info)
        print(info)

    elif 'tell me the time' in command:
        command = command.replace('tell me the time', '')
        time = datetime.datetime.now().strftime('%I %m %p')
        talk('time right now is' + time)
        print(time)

    else:
        talk('Sorry Can repeat it one more time')

    talk('Sorry Can repeat it one more time')


while True:
    run_payu()

'''''
listener = sr.recognize

pip install face-recognition
pip install dlib
pip install PyAudio

pip install opencv-python

pip install pywhatkit

pip install pyttsx3

pip install pywikipedia

pip install SpeechRecognition

pip install rotate-screen
'''''
