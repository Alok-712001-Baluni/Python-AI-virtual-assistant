import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")       

    speak("I am your virtual assistant Sir, Please tell me how may I help you")

def takeCommand():
#takes Microphone input from the user and returns string output    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing......")    
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"

    return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('alokbaluni712001@gmail.com', 'enter your password here')
    server.sendmail('alokbaluni712001@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe() 
    while True:   
        query=takeCommand().lower()  


        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stack overflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir= "E:\\Music"
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,the time is {strTime}")

        elif 'open code' in query:
            codePath= "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 

        elif 'email to honey' in query:
            try:
                speak("what should I say")
                content= takeCommand()
                to="alokbaluni712001@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send the email")

        elif 'quit' in query:
            print("Okay Sir, Bye")
            speak("Okay Sir, Bye")
            break        

                     