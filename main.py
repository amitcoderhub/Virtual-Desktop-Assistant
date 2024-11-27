# import os
# import eel


# from engine.features import *
# from engine.command import *
# from engine.auth import recoganize


    
# def start():
#     eel.init("www")

#     playAssistantSound()
#     @eel.expose
#     def init():
#         # subprocess.call([r'device.bat'])
#         eel.hideLoader() 
#         speak("Ready for face Authentication")
#         flag = recoganize.AuthenticateFace()
#         if flag == 1:
#             eel.hideFaceAuth()
#             speak("Face Authenticated Successfully")
#             eel.hideFaceAuthSuccess()
#             speak("welcome to my world sir")
#             wish()
#             tellday()
#             eel.hideStart()
#             playAssistantSound()
#             playAssistantSound2()
#             speak("hello sir , how can assist you ")
#         else:
#             speak("Face Authentication Failed")    


#     os.system('start msedge.exe --app="http://localhost:8000/index.html"')

#     eel.start('index.html', mode=None, host='localhost', block=True)

    

import os
import eel

from engine.features import *
from engine.command import *
from engine.auth import recoganize

def start():
    eel.init("www")

    playAssistantSound()

    @eel.expose
    def init():
        try:
            # subprocess.call([r'device.bat'])  # Uncomment this if you need to run the batch file
            eel.hideLoader()
            playAssistantSound()
            speak("Ready for face Authentication")
            flag = recoganize.AuthenticateFace()
            if flag == 1:
                eel.hideFaceAuth()
                speak("Face Authenticated Successfully")
                eel.hideFaceAuthSuccess()
                speak("Welcome to my world, sir")
                wish()
                tellday()
                eel.hideStart()
                playAssistantSound()
                playAssistantSound2()
                speak("Hello sir, how can I assist you?")
            else:
                speak("Face Authentication Failed")
        except Exception as e:
            speak("An error occurred during authentication.")
            print(f"Error: {e}")

    try:
        os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    except Exception as e:
        print(f"Failed to start browser: {e}")
    
    eel.start('index.html', mode=None, host='localhost', block=True)
    

if __name__ == "__main__":
    start()
