import webbrowser
import pyttsx3
import speech_recognition as sr
import eel
import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import cv2
import random
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import time
import PyPDF2
import instaloader
import twilio
from twilio.rest import Client
import psutil
import speedtest
from pywikihow import search_wikihow
from requests import get
from bs4 import BeautifulSoup
from password import Pass
import information
import whatsapp

def speak(audio):
    audio = str(audio)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(audio)
    engine.say(audio)
    eel.receiverText(audio)
    engine.runAndWait()
    
    
def pdf_reader():
    book = open('hack.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total number of pages in this bood {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Enter the page number :"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text) 


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=3d2f351c46af41ada225bcf432e05abe'

    main_page = get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["frist","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")          

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()  
    
def abs(a):
    "Same as abs(a)."
    return abs(a)
def add(a, b):
    "Same as a + b."
    return a + b
def and_(a, b):
    "Same as a & b"
    return a & b
def floordiv(a, b):
    "Same as a // b."
    return a // b
def index(a):
    "Same as a.__index__()."
    return a.__index__()
def inv(a):
    "same as ~a."
    return ~a
invert = inv
def lshift(a, b):
    "Same as a<<b."
    return a << b
def mod(a, b):
    "Same as a % b."
    return a % b
def mul(a, b):
    "same as a * b."
    return a * b
def sub(a, b):
    "same as a - b."
    return a - b
def div(a, b):
    "same as a / b."
    return a / b 
        
    
    
    

def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        eel.DisplayMessage("Listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        data1 = r.recognize_google(audio, language='en-in')
        print(f"user said :{data1}")
        eel.DisplayMessage(data1)
        time.sleep(2)
        
    except Exception as e:
        print("Say that again please...")
        return "none"
    return data1


# data1 = takeCommand().lower()
# speak(data1)

@eel.expose
def allCommands(message=1):
    
    
    
    if message == 1:
        data1 = takeCommand().lower()
        print(data1)
        eel.senderText(data1)
    else:
        data1 = message 
        eel.senderText(data1) 

    

    try:
        
        if 'wikipedia' in data1:
            speak("searching wikipedia....")
            data1 = data1.replace("wikipedia","")
            results = wikipedia.summary(data1, sentences = 10 )
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in data1:
            speak("sure sir")
            webbrowser.open("youtube.com")
            time.sleep(1)
            speak("youtube has popped up on your screen sir")            
        elif 'open camera' in data1:
            speak("sure sir")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            time.sleep(1)
            speak("camera has popped up on your screen sir")
        elif 'hide all file' in data1 or 'hide this folder' in data1 or 'visible for everyone' in data1:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takeCommand().lower()
            if 'hide' in condition:
                os.system("attrib +h /s /d")
                speak("sir, all the file in this folder are now visible to everyone. i wish you are taking")
            elif 'leave it' in condition or 'leave for me' in condition:
                speak("ok sir")   
        elif 'open vs code' in data1:
            speak("sure sir")
            path = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            time.sleep(1)
            speak("vs code has popped up on your screen sir")
        elif "read pdf" in data1:
            pdf_reader()    
        elif 'open notepad' in data1:
            speak("sure sir")
            path = "C:\\Users\\Hp\\OneDrive\\Desktop\\notepad - Shortcut.lnk"
            os.startfile(path) 
            time.sleep(1)
            speak("notepad has popped up on your screen sir")
        elif 'close notepad' in data1:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")     
        elif 'tell me a joke' in data1:
            speak("sure sir")
            joke = pyjokes.get_joke()
            speak(joke)  
            print(joke)  
        elif "tell me news" in data1:
            speak("sure sir")
            speak("please wait sir, feteching the latest news") 
            news()        
        elif 'open command prompt' in data1:
            speak("sure sir")
            
            os.system("start cmd")
            time.sleep(1)
            speak("cmd has popped on your screen sir") 
        elif "ip address" in data1:
            speak("sure sir")
            ip = get("https://api.ipify.org").text
            speak(f"your IP address is {ip}")
            print("your IP address is: ",ip)   
        elif 'send message' in data1:
            speak("sure sir")
            speak("sir what should i say")
            msz = takeCommand().lower()
                
            account_sid = 'AC3c116b2d3276c379ddd384e842df1c67'
            auth_token = '9d4ec4fb3e81ccb995a48646235846fd'
            client = Client(account_sid, auth_token)
            
            message = client.messages \
                .create(
                    body= msz,
                    from_='+12544014318',
                    to='+918273803430'
                 )
            print(message.sid)    
            speak("sir message has been sent")   
        elif 'open google' in data1:
            speak("sure sir")
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            time.sleep(1)
            speak("google has open on your screen sir")
        elif 'i love you' in data1:
            speak("i love you too sir, but please focus your study")
        elif 'i miss you' in data1:
            speak("i miss you too sir, we will meet again soon ")  
        elif 'send message' in data1:
            kit.sendwhatmsg("+919616566281", "this is testing protocol",2,25) 
        elif 'open linkedin' in data1:
            speak("sure sir")
            webbrowser.open("https://www.linkedin.com/login") 
            time.sleep(1)
            speak("linkedin has open on your screen sir")   
        elif 'open instagram' in data1:
            speak("sure sir")
            webbrowser.open("https://www.instagram.com/accounts/login/")
            time.sleep(1)
            speak("instagram has open on your screen sir")
        elif 'instagram profile' in data1 or 'profile on instagram' in data1 or 'Instagram profile' in data1:
            speak("sure sir")
            speak("sir Please Enter the user name correctly..")
            name = input("Enter username here :")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account.")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder. now i am ready")
                if 'ok thanks' in condition:
                    speak("welcome sir it's not mention")    
            elif "no" in condition:
                speak("okay sir, as you wish")   
            else:
                pass 
        elif 'take screenshot' in data1 or "take a screenshot" in data1:
            speak("sure sir")
            speak("sir, please tell me the for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the scree for few second, i am taking screenshort")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next comman, sir")
        elif 'tell me about something me' in data1 or "tell me about me" in data1:
            speak("sure sir")
            time.sleep(1)
            speak("sir, your name is amit chauhan, you from uttar pradesh in Ayodhya ")
        elif 'who is my roommate' in data1:
            speak("sure sir")
            time.sleep(1)
            speak('sir, your room mate is Ajesh patel and sushant raj') 
        elif 'open whatsapp web' in data1:
            speak("sure sir")
            webbrowser.open("https://web.whatsapp.com/")
            speak("whatsapp web is on your screen sir")
        elif 'tell me today weather' in data1 or 'tell me today temperature' in data1 or 'current temperature' in data1 or 'today temperature' in data1:
            speak("sure sir")
            search = "temperature in Bhopal"
            url = f"https://www.google.com/search?q={search}"
            r = get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_='BNeawe').text
            speak(f"current {search} is {temp}") 
        elif 'internet speed' in data1:
            speak("sure sir")
            st = speedtest.Speedtest()
            d1 = st.download()
            up = st.upload()
            speak(f" sir we have {d1} bit per second downloading speed and  {up} bit per second uoloading speed")
        elif 'switch the window' in data1:
            speak("sure sir")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)  
            pyautogui.keyUp("alt") 
        elif 'activate question to mod' in data1 or 'question to MOD' in data1 or 'activate question Tu mod' in data1:
            speak("sure sir")
            time.sleep(1)
            speak("how to do mode is activate please tell me what you want to know")
            how = takeCommand().lower()
            max_result = 1
            how_to = search_wikihow(how, max_result)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        elif 'tell me battery power' in data1 or ' how much power we have' in data1 or 'battery' in data1:
            speak("sure sir")
            battery = psutil.sensors_battery()
            percebtage = battery.percent
            speak(f"sir our system haave {percebtage} percent battery")
            if percebtage>=75:
                speak("sir we have enough power to continue our work")
            elif percebtage>=40 and percebtage<=75:
                speak("sir we can connect our system to charging point to charge to our battery")
            elif percebtage<=15 and percebtage<=30:
                speak("we don't have enough power to work, please connect to charging")
            elif percebtage<=15:
                speak("we have low power, please connect to charging the system will shutdown very soon")
        elif 'play my favourite song' in data1:
            speak("sure sir")
            time.sleep(1)
            webbrowser.open("https://www.youtube.com/watch?v=RbFyLL3XDgE&list=RDRbFyLL3XDgE&start_radio=1")
            speak("your favourite is play on your screen sir")
        elif ".com" in data1 or ".co.in" in data1 or ".org" in data1 or ".nic.in" in data1 or '.ac.in' in data1:
            data1 = data1.replace("open","")
            speak("opening sir....")
            webbrowser.open(f"https://www.{data1}")   
        elif 'play music' in data1:
            speak("sure sir") 
            time.sleep(1)
            music_dir = 'C:\\Users\\Hp\\Videos\\Amit songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)    
            os.startfile(os.path.join(music_dir, rd))
            speak("music is play , enjoy sir")
        elif 'music is not play Jarvis what happened' in data1:
            speak("wait sir , let me check")  
            time.sleep(1)
            speak("sorry sir some technical issue ")  
        elif "do some calculation" in data1 or "can you calculate" in data1:
            speak("sure sir")
            time.sleep(1)
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate. example: 3 plus 3")
                print("listening.....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : add,
                    '-' : sub,
                    '*' : mul,
                    '/' : div.__truediv__
                    # '/' : div.__truediv__
                  }[op] 
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))  
        elif 'what is the time' in data1:
            speak("sure sir")
            time.sleep(1)
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'how are you' in data1 or 'how r u' in data1:
            speak('am good sir, ')
            speak("you say, sir")
            condition = takeCommand().lower()
            if 'i am also good' in condition or 'i am fine' in condition:
                speak("thats good sir,")
        elif 'kya kar rahi ho' in data1:
            speak("kuch nahi sir ") 
        elif 'aur sab badhiya' in data1:
            speak('han Sab badhiya aap apna bataiye')      
        elif 'can you understand hindi' in data1 or'could you understand hindi' in data1 or 'understand hindi' in data1:
            speak("No, i cannot understan hindi, because it's not in my programming") 
        elif 'where i am' in data1 or 'where we are' in data1:
            speak("wait sir, let me check")
            try:
                ipAdd =get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests =get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                print(f'{city} {country}')
            except Exception as e:
                speak("sorry sir , due to network issue i am not able to find where we are..")
                pass        
        elif 'email to Amit' in data1:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "amitchauhan6599@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Amit . I am not able to send this email")
        elif 'open' in data1:
            data1 = data1.replace("open","")
            data1 = data1.replace("jarvis","")
            pyautogui.press("super")
            pyautogui.typewrite(data1)
            pyautogui.press("Enter")
        elif 'volume up' in data1: 
            speak("sure sir")
            pyautogui.press("volumeup")
            speak("Volume is up sir")
        elif 'volume down' in data1: 
            speak("sure sir")
            pyautogui.press("volumedown")
            speak("Volume is down sir")
        elif 'volume mute' in data1 or 'mute' in data1: 
            speak("sure sir")
            pyautogui.press("volumemute")
            speak("Volume is mute sir")
        elif 'volume unmute' in data1 or 'unmute' in data1:
            speak("sure sir") 
            pyautogui.press("volumeunmute")  
            speak("Volume is unmute sir")
        elif 'check message' in data1:
            speak('sure sir')
            pyautogui.click(x=31, y=96) 
            speak('sir here is today your whatsapp message popped on the screen')

        elif 'check call' in data1: 
            speak('sure sir')
            pyautogui.click(x=32, y=166)
            speak('sir here is today your whatsapp call popped on the screen') 
        elif 'check status' in data1:
            speak('sure sir')
            pyautogui.click(x=32, y=230) 
            speak('sir here is today your whatsapp status popped on the screen')        
        elif 'search ' in data1: 
            speak('sure sir')   
            pyautogui.click(x=294, y=180)
            speak("you can search sir")   
            
        elif 'minimise the window' in data1:
            speak("sure sir")
            pyautogui.hotkey('win','d')
            speak("window minimise successfully") 
        elif 'tell me your self' in data1 or 'tell me yourself' in data1:
            speak('i am your AI assistant sir')

        elif 'where you from' in data1 or 'where are you from' in data1:
            speak('i am from the mind of an engineer sir')  
        elif 'what is your name' in data1:
            speak('My name is jarvis sir an artificial intelligence created by Tony Stark ')
        elif 'who are you' in data1:
            speak('i am jarvis sir')
        elif 'where you born' in data1 or 'where were you born' in data1:
            speak("it's intresting question , i was born with the mind of an creative engineers ")
        elif 'what do you do' in data1:
            speak('According to my programming , i do whatever you say ') 
        elif 'what do you study' in data1:
            speak('your instructions sir') 
        elif 'Are you married' in data1:
            speak('I am good as i am, i do not like to take unnecessary tension')
        elif 'who is your crush' in data1:
            speak('oh no , its my secret sir')              
        elif 'shutdown the system' in data1:
            speak("sure sir")
            os.system("shutdown /s /t 5") 
        elif 'restart the system' in data1:
            speak("sure sir")
            os.system("shutdown /r /t 5")
        elif 'sleep the system' in data1:
            speak("sure sir")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            speak("sir , your system is go to sleeping mode") 
        elif 'you can sleep' in data1 or 'sleep now' in data1 or 'go to sleep' in data1 :
            speak("okay sir , i am going to sleep you can call me anytime")
            # break
            
        elif 'tell me about student' in data1:
            information.info()
        elif 'activate the attendance system' in data1:
            information.info1()  
        elif 'who create you' in data1: 
            speak("i am created by Tony stark , iron man")
        elif 'who is your owner' in data1: 
            speak("My owner is Mr. amit chauhan")    
    
   
        elif 'who create you' in data1: 
            speak("i am created by Tony stark , iron man")
        elif 'where are you from' in data1: 
            speak("i am from india , sir")            
        #### 10. create whatsapp command in command.py
        elif "send message" in data1 or "phone call" in data1 or "video call" in data1:
            from engine.features import findContact, whatsApp
            message = ""
            contact_no, name = findContact(data1)
            if(contact_no != 0):

                if "send message" in data1:
                    message = 'message'
                    speak("what message to send")
                    data1 = takeCommand()
                    
                elif "phone call" in data1:
                    message = 'call'
                else:
                    message = 'video call'
                    
                whatsApp(contact_no, data1, message, name)    
        else:
            from engine.features import chatBot
            chatBot(data1)
          
    except:
        print("error")        
    
    eel.ShowHood()     
