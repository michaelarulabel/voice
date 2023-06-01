import speech_recognition as sr
import pyttsx3
import pywhatkit

listener=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


with sr.Microphone() as source:
    print('')


def song():
    with sr.Microphone() as source:
        engine.say('Which Song Do you want to play')
        engine.runAndWait()
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        pywhatkit.playonyt(command)
        engine.say('Have you enjoyed the song')
        engine.runAndWait()
        voice = listener.listen(source)
        command = listener.recognize_google(source)
        if 'yes' in command:
            engine.say('Thats great')
            engine.runAndWait()

def date_time():
     with sr.Microphone() as source:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        engine.say(time)
        engine.runAndWait()

def repeat_me():
        with sr.Microphone() as source:
           engine.say('say something')
           engine.runAndWait()
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           engine.say(command)
           engine.runAndWait()

def type_me():
        with sr.Microphone() as source:
           engine.say('Say something')
           engine.runAndWait()
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           print(command)
        
def main():
     print('Start')
     with sr.Microphone() as source:
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          command = command.lower()
          if 'hi' in command:
               engine.say('hello')
               engine.runAndWait()
               print('Hello')
          print('Listening...')
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          if 'repeat' in command:
               repeat_me()
          print('Listening...')
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          if 'type' in command:
               type_me()
          print('Listening...')
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          if 'song' in command:
               song()
          print('Listening...')
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          if 'time' in command:
               date_time()
          
        


          