import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import pyautogui

url="C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(url))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def clear_speech(query):
    str=""
    for i in query:
        if i.isalpha() or i.isspace() or i.isdigit():
            str=str+i
    return str
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("A very Good Morning sir!")
    elif(hour>=12 and hour<18):
        speak("A very Good Afternoon sir!")
    else:
        speak("A very Good evening sir!")
    speak("I am JARVIS , your personal ai assistant , please tell me how may I help you")

def takeCommand():
    #microphone input ----string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold= 1
        print("Listning...")
        audio = r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
        #speak(query)
    except Exception as e:
        #print("Sorry , I didn't get you")
        speak("Sorry , I didn't get you") 
        return "None"
    return query.lower()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic
        if 'wikipedia' in query:
            speak("As you wish sir!")
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)
        
        elif "sleep" in query or "i need a break" in query or "you need a break" in query or "get lost" in query or "i had enough" in query:
            speak("As you wish sir!")
            speak("Thank you Sir , and have a nice day ahead")
            break

        elif ("pc owner" in query):
            #speak("As you wish sir!")
            speak("The owner of this laptop is Anurag Das , who completed his secondary education from ,St.Edmund's School ,and higher secondary from St.Anthony's School ,. He currently studies in , Kalinga Instutute OF industrial Technology , located in bhuvaneshwar , India ")
            speak("Do you want to know more about the owner?")
            query2=takeCommand()
            if "yes" == query2:
                speak("What do you want to know? , Favourite sport? , hobby?")
                query3=takeCommand()
                if "favourite sport" == query3:
                    speak("Badminton")
                if "hobby" == query3:
                    speak("Anurag's hobbyies include , cycling , gaming  ,and , coding related to development ")
                    continue
            if "no" == query2:
                speak("okay")
                continue
        
        elif("youtube search" in query):
            speak("As you wish sir!")
            speak("What do you want to search in youtube?")
            query=takeCommand()
            query=query.replace("search","")
            web= "https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
            speak("Done , Sir!")

        elif("open gmail" in query):
            speak("As you wish sir!")
            speak("opening gmail")
            webbrowser.get('chrome').open_new_tab("gmail.com")
            
        elif("play music" in query):
            music_dir='C:\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            speak("as you wish sir!")
            speak("which song do you wish to play from the printed list? ")
            query2=takeCommand()
            speak("playing music")
            if "any song" in query2:
                os.startfile(os.path.join(music_dir,songs[int(random.randint(0,3))]))
            else :
                os.startfile("C:\\songs\\"+query2+".mp3")

        elif "time" in query:
            speak("as you wish sir!")
            tm=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {tm}")

        elif "open vs code" in query:
            speak("as you wish sir!")
            speak("opening Visual Studio Code")
            path="C:\\Users\\anura\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            
        elif "who is" in query:
            speak("I do not know this person")
        elif "open telegram" in query:
            speak("as you wish sir!")
            speak("opening telegram")
            path="C:\\Users\\anura\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(path)
        
        elif ("open cmd" in query) or ("open command prompt" in query):
            speak("as you wish sir!")
            speak("opening command prompt")
            path="C:\\Windows\\system32\\cmd.exe"
            os.startfile(path)
        
        elif "google search" in query:
            speak("as you wish sir!")
            speak("What do you want to search in google?")
            query=takeCommand()
            query= query.replace("jarvis","")
            query=query.replace("search","")
            pywhatkit.search(query)
            speak("Done , sir")
            
        elif "launch website" in query:
            speak("as you wish sir!")
            speak("Please tell me the name of the website you wish to open")
            name=takeCommand()
            name=name.replace("launch","")
            name=name.replace("website","")
            web='https://www.'+name+'.com'
            webbrowser.open(web)
            speak("Done , sir!")
            
        elif "instagram" in query:
            speak("as you wish sir!")
            webbrowser.open("https://www.instagram.com")
            speak("Done , sir!")
            
        elif "whatsapp message" in query:
            query=query.replace("whatsapp message to","")
            speak("please dictate the message")
            msg=takeCommand()
            speak("please tell the time in hours")
            hr=int(takeCommand())
            speak("please tell me the time in minutes")
            mn=int(takeCommand())
            no="+919863087160"
            pywhatkit.sendwhatmsg(no,msg,hr,mn,20)
            speak("Sending message...")
        elif "who are you" in query:
            speak("I am Jarvis , you personal ai assistant , created by Anurag")
        elif "can you play" in query:
            speak("sorry sir , i am not equipped to do that")
        elif "can you dance" in query:
            speak("sorry sir , i am not equipped to do that")
        elif "i am bored" in query:
            speak("I can help you out with that")
        elif "are you human" in query:
            speak("No , i am a personal ai assistant")
        elif "you are useless" in query:
            speak("Sorry sir for the inconvenience , hope to see you soon , have a noce day ahead")
            break
        
        #elif "launch GTA" in query or "launch GTA 5" in query:
            speak("Launching GTA 5..")
            path="C:\\Games\\Grand Theft Auto V\\GTAVLauncher.exe"
            os.startfile(path)
        
        elif "screenshot" in query:
            speak("as you wish sir!")
            speak("please tell me what should i name the screenshot file")
            name=takeCommand()
            name=name+".png"
            path = "C:\\Users\\anura\\OneDrive\\Pictures\\Screenshots\\"+name
            kk=pyautogui.screenshot()
            kk.save(path)
            speak("would you like to see the screenshot?")
            query2 = takeCommand()
            if "yes" in query2:
                os.startfile(path)
                speak("Here is your screenshot , sir")
            else:
                speak("as you wish sir!")
        
        elif "who made you" in query or "who is your ownner" in query or "who developed you" in query:
            speak("I was made by Anurag Das on 19 July , 2021")
        
        elif "map" in query and "open" in query:
            speak("opening google maps")
            webbrowser.open("https://www.google.com//maps")
        
        elif "instagram" in query and "open" in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com")
            
        elif "instagram" in query and "close" in query:
            speak("as you wish sir")
            os.system("TASKKILL /F /im chrome.exe")
            
        elif "you" in query and "good" in query:
            speak("It is my pleasure , sir")
        elif "good" in query:
            speak("Thank you , sir")
            
        elif "facebook" in query and "open" in query:
            speak("opening facebook")
            fb=webbrowser.open("https://www.facebook.com")
            
        elif "facebook" in query and "close" in query:
            speak("as you wish sir")
            speak("closing facebook")
            os.system("TASKKILL /F /im chrome.exe")
        
        elif "are you" in query:
            speak("please contact my developer for any queries")
            
        elif "i am" in query or "I am" in query:
            speak("Hello , nice to meet you")
        
        elif "hello" in query:
            speak("Hi !")
        
        elif "hi" in query:
            speak("Hello!")
        
        elif "bye bye" in query:
            speak("please give me the sleep command to shut me down")
        
        elif "" in query:
            speak("")
        
        elif "" in query:
            speak("")
        
        elif "" in query:
            speak("")