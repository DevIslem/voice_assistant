import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
voices = engine.getProperty('voices')
engine.setProperty('voice', voice_id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            #talk('hey there')
            #talk('what can i do for you')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = cammand.replace('alexa', '')
                talk(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is' + time)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, i have a boyfriend')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif'bye' in command:
        talk('goodbye')

    else:
        talk('please say the command again.')


while True:
    run_alexa()
