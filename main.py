# first installing speechrecogniton and pyaudio
#then installing setuptools,pyttsx3
#then importing webbrowser as it is a built in module
#INSTALLING GEMINI
# python -m pip install --upgrade pip
# pip install google-genai
#pip install --upgrade google-genai pydantic

import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from client import ask_gemini

r = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def aiprocess(command):
    return ask_gemini(command)
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    else:
        #Let openai handle the request
        output=aiprocess(c)
        print(output)
        speak(output)
if __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:

    # obtain audio from the microphone
        r = sr.Recognizer()
       
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source,timeout=10,phrase_time_limit=5)
            command=r.recognize_google(audio)
            print(command)
            if "hey" in command.lower():
               # print("hey detected!")
                speak("yeah")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)

                    processcommand(command)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

            

