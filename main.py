from time import ctime
import time
import speech_recognition as sr
import ai
import pyttsx3

def listen():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Litesning...')
        r.pause_threshold = 0.7
        audio = r.listen(source)
    
    data = ''

    try:
        data = r.recognize_google(audio)
        print('You said: ', data)
    except sr.UnknownValueError:
        print('I did not understand your speech :(')
    except sr.RequestError as e:
        print(f'Request failed; {e}')

    return data



def respond(audio):
     
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio) 
    engine.runAndWait()


def assistant(data):

    listening = True

    if 'stop' in data:
        listening = False
        respond('Goodbye!')
        return listening
    
    else:
        respond(ai.get_completion(data))

    return listening

time.sleep(2)

respond('Hi Ario how may I help today?')
listening = True
while listening == True:
    data = listen()
    listening = assistant(data)
    print(ai.get_completion(data))