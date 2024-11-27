import datetime
import os
from pipes import quote
import re
import struct
import subprocess
import time
from playsound import playsound
import pyaudio
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
import eel
import pywhatkit as kit
from engine.helper import extract_yt_term, remove_words
import pvporcupine
from hugchat import hugchat

import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('jarvis.db')
cursor = conn.cursor()


@eel.expose

def playAssistantSound():
    # music_dir = "www\\assets\\audio\\start_sound.mp3"
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
def playAssistantSound2():
    music_dir = "www\\assets\\audio\\jarvis launching voice.mp3"
    playsound(music_dir)
    
def wish():
    hour =int(datetime.datetime.now().hour)

    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"  Good Morning, it's {tt} ")    

    elif hour>=12 and hour<18:
        speak(f" Good Afternoon, it's {tt} ")   

    else:
        speak(f" Good Evening, it's {tt} ")

 
    speak('i am dorothy sir , please tell me how can i help you...') 

def tellday():
    day = datetime.datetime.today().weekday()+1
    Day_dict = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thusday',5:'Friday',6:'Saturday',7:'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak('the day is '+ day_of_the_week)     



def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["alexa","jarvis"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()   
            
             
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtobe'
    match = re.search(pattern, command,re.IGNORECASE)
    return match.group(1) if match else None


#### 8. Create find contacts number Function in features.py



# Whatsapp Message Sending
def findContact(data1):
    
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    data1 = remove_words(data1, words_to_remove)

    try:
        data1 = data1.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + data1 + '%', data1 + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, data1
    except:
        speak('not exist in contacts')
        return 0, 0
    
#### 9. Create Whatsapp Function in features.py


def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 6
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 5
        message = ''
        jarvis_message = "staring video call with "+name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(3)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)

# chatBot-------------------
# def chatBot(data1):
#     user_input = data1.lower()
#     chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
#     id = chatbot.new_conversation()
#     chatbot.change_conversation(id)
#     response =  chatbot.chat(user_input)
#     print(response)
#     speak(response)
#     return response    


