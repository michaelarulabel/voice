import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
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
      engine.say('Current time is '+time)
      engine.runAndWait()

def repeat_me():
  with sr.Microphone() as source:
    print('Listening...')
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
        

    

      

def basic_operations():
  try:
      with sr.Microphone() as source:
        print('Please say something')
        engine.say('please say something')
        engine.runAndWait()
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'pluto' in command:
            engine.say('hello! glad to meet you')
            engine.runAndWait()
            print('Hello! Glad to meet you')
        elif 'repeat' in command:
            repeat_me()
        elif 'type' in command:
            type_me()
        elif 'time' in command:
            date_time()
        elif 'who is ' in command:
           person = command.replace('who is','')
           info = wikipedia.summary(person,1)
           print(info)
           engine.say(info)
           engine.runAndWait()
        elif 'joke' in command:
           engine.say(pyjokes.get_joke())
           engine.runAndWait()
           
        elif 'song' in command:
            song()
        elif 'are you single' in command:
           engine.say('No, Im committed with wifi now, sorry')
           engine.runAndWait()
        elif 'sad' in command:
           engine.say('Dont be worried, everything will be alright')
           engine.runAndWait()
        elif 'love' in command:
           engine.say('I love you to')
           engine.runAndWait()
        elif 'name' in command:
           engine.say('Im glad to hear,so, what is my name')
           engine.runAndWait()
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           engine.say('ok from now my name is'+command)
           engine.runAndWait()
        elif 'bye' in command:
           engine.say('Thank you, I hope we will meet again')
           engine.runAndWait()
           
        elif 'who are you' in command:
           engine.say('im pluto, your voice assistant')
           engine.runAndWait()



        else:
           engine.say('Sorry! Could you please repeat it again')
           engine.runAndWait()

        
           
        

  except:
    pass
  

while True:
   basic_operations()

