import time
import speech_recognition as sr
import pandas as pd
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        data1 = r.recognize_google(audio, language='en-in')
        print(f"user said :{data1}")
    except Exception as e:
        print("Say that again please...")
        return "none"
    return data1
def info():
    data1 = takeCommand().lower()

    if 'tell me about student' in data1 or 'show me aiml student data' in data1: 
            speak('sure sir, please wait sir ')
            df = pd.read_csv("C://Users//Hp//OneDrive//Desktop//attendence.csv")
            speak('sir please enter your query what you want know' )
            speak("if you want to know about  any particular student then enter 1")
            speak("if you want to know about all student Name/Roll no./Branch then enter 2")
            speak("if you want to know about all student or some student all data then enter 3")
            p = int(input("Enter the our numbering system :"))
            if p == 1:
                df = pd.read_csv("C://Users//Hp//OneDrive//Desktop//attendence.csv")
                speak("Enter the student Serial number")
                y = int(input("Enter the Serial number :"))
                x = y+1
                speak("Your Enrollment number is 0133CL21100" + str(x) + "")
                df = df.iloc[int(y)]
                print(df)
                while True:
                    speak("Sir Are you want to know about more information about any particular student yes or no")
                    z=input("Sir Are you want to know about more information about any particular student yes or no :")
                    if 'yes' in z:
                        df = pd.read_csv("C://Users//Hp//OneDrive//Desktop//attendence.csv")
                        speak("Enter the next student Serial number")
                        y = int(input("Enter the next student Serial number :"))
                        x = y+1
                        speak("Your Enrollment number is 0133CL21100" + str(x) + "")
                        df = df.iloc[int(y)]
                        print(df)
                    elif 'no' in z:
                        speak('thanks for using me sir , have a good day')
                        break  
            elif p == 2:
                speak("sir please enter the your query  like Name/Roll no./Branch")
                x1 = input("sir please enter the your query  like Name/Roll no./Branch :")
                print(df[[x1]])
                while True:
                    speak('sir you want to know more information about Name/Roll no/Branch yes or no')
                    q = input('sir you want to know more information about Name/Roll no/Branch yes or no :')
                    if 'yes' in q:
                        x1 = input( "sir please enter the your query what you want to know about student like Name/Roll no./Branch :")
                        print(df[[x1]])
                    elif 'no' in q:
                        speak('Thanks for using me sir , Have a good day')
                        break
            elif p == 3:
                speak('Sir please Enter the number how many students you want to know about according your class strenth')
                x = int(input("Sir please Enter the number how many students you want to know about according your class strenth :"))
                a =df.head(x)
                # speak(a)
                print(a)
                while True:
                    speak('Sir are you want to more information')
                    y = input('Sir are you want to more information yes or no :')
                    if 'yes' in y:
                        speak("Sir please again Enter the number how many students you want to know about according your class strenth")  
                        x = int(input("Sir please Enter the number how many students you want to know about according your class strenth :"))
                        a =df.head(x)
                        # speak(a)
                        print(a)
                    elif 'no' in y:
                        speak("Thanks for using me sir, have a good day")
                        break
def info1():
    data1 = takeCommand().lower()
    
                        
    if 'open the attendance system' in data1 or 'activate the attendance system' in data1:       
            speak('sure sir , ready for attendance')
            file_path = 'C://Users//Hp//OneDrive//Desktop//attendence.csv'  # Replace with your file path/
            df = pd.read_csv(file_path)  # Use pd.read_excel() for Excel files
            speak('Enter the row index num')
            r = int(input("enter the row index num :"))  # Replace with the row index where you want to insert the value
            speak('enter the today date')
            c= str(input("enter the today date :"))  # Replace with the column name where you want to insert the value
            speak("enter the attendence present or absent")
            i = str(input("enter the attendence Present or Absent :"))
            # i = takeCommand().lower()
            df[c][int(r)]= i
            df.to_csv(file_path, index=False)
            speak('are you want to show the attendance yes or no')
            b = input("Are you want to show the attendance yes or no :")
            # b = takeCommand().lower()
            if 'yes' in b:
                print(df)
            elif 'no' in b:
                speak('ok sir  ')
            while True:
                speak('Are you want to more attendence yes or no')      
                t = input("Are you want to more attendence yes or no :")
                # t = takeCommand().lower()
                if 'yes' in t:
                    speak('Enter the row index num')
                    r = int(input("enter the row index num :"))  # Replace with the row index where you want to insert the value
                    speak('enter the today date')
                    c= str(input("enter the today date :"))  # Replace with the column name where you want to insert the value
                    speak("enter the attendence p or a")
                    i = str(input("enter the attendence P or A :"))
                    # i = takeCommand().lower()
                    df[c][int(r)]= i
                    df.to_csv(file_path, index=False)
                    speak('are you want to show the attendance yes or no')
                    b = input("Are you want to show the attendance yes or no :")
                    # b = takeCommand().lower()
                    if 'yes' in b:
                        print(df)
                    elif 'no' in b:
                        speak('thanks for using me sir , have agood day ')
                        break
                elif 'no' in t:
                    speak('thanks for using me sir , have agood day ')
                    break
                
if __name__ == "__main__":
    info() 
    info1()              
