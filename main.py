
from fileinput import filename
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list=["Go Shopping", 'Clean Room',' Record Video']

def create_note():
    
    global recognizer
    speaker.say("What do want to write onto your note?")
    speaker.runAndWait()
    
    done = False 
    
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer .adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                note = recognizer.recognize_google(audio)
                note = note.lower()
                
                speaker.say("Choose filename!")
                speaker.runAndWait()
                
                recognizer.adjust_for_ambient_noise(mic, duration =0.2)
                audio= recognizer.listen(mic)
                
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()
                
            with open(filename, 'W') as f:
                f.write(note)
                done = True
                speaker.say(f"iI successfully created the note {filename}")
                speaker.runAndWait()
    
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say = ("I did not understand you! Please try again!")
            speaker.runAndWait()
    

def add_todo():
    global recognizer
    speaker.say("What todo do you want to add?")
    speaker.runAndWait()
    
    done = False 
    while not done:
        try:
            with speech_recognition.Microphone as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio= recognizer.listen(mic)
                
                item =recognizer.recognize_google(audio)
                item = item.lower()
                
                todo_list.append(item)
                
                
    
    



assistant = GenericAssistant('intents.json')
assistant.train_model()

