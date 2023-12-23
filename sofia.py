
import os
import webbrowser
import subprocess
import openai
openai.api_key = "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"
import pyttsx3
import datetime
# required only if you need to use microphone input, Microphone
import pyaudio
import speech_recognition as sr
import re
import pywhatkit
import json
import pyautogui
import time

# import chatbot
# chatbot.opening( 'https://github.com/Prince-Sharma002/gfg-dsa-c-' )


with open("Number.json") as f:
    data = json.load(f)




				# sofia voice


# initialize the engine
engine = pyttsx3.init()
# set the rate of speech
engine.setProperty('rate', 130)
# set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change index to change voice

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()






                                    # alexa
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))





def wish():
    time = "morning"
    currentTime = datetime.datetime.now()
    if(currentTime.hour < 12 ):
        time = "morning"
    elif( currentTime.hour >=  12 and currentTime.hour <= 16 ):
        time = "afternoon"
    else:
        time = "evening"
    speak(f"good {time} , I am sofia an ai created by master prince")
wish()

sr.Microphone( device_index=1 )
listener = sr.Recognizer()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen( source , phrase_time_limit=7 )

    try:
        print("Recognizing...")
        command = r.recognize_google( audio , language="en-in")
        print(f"You Said:{command}")
    except Exception as e:
        return "none"

    return command    

flag  = 1
while True:
    
    if( flag):
        command = input("Enter Command:").lower()
        if("open mic" in command):
            flag = 0
    else:
        command = takecommand().lower()

    if( "hello" in command ):
        speak("hi , please provide your identity")
        print("hi , please provide your identity")
        if( "007" in takecommand().lower()  ):
            speak("hi master prince , good to see you")
        else:
            speak("not match")

    elif( ("search" in command) or ("what is" in command) or ( "find" in command ) ):
        command = command.replace("sofia" , "").replace("search" , "")
              
        print("searched item:" ,command)        
        completion = openai.Completion.create(
        engine = "text-davinci-003",    
        prompt = command ,
        max_tokens = 1000
        )        
        speak( completion.choices[0]["text"] )
    
    elif( "open control" in command ):
        speak("opening control panel")
        os.system("control")
    
    elif( ("open text editor" in command ) or ("open whatsapp" in command ) or ("open github" in command ) or ("open linkedin" in command ) or ("open chrome" in command ) ):
        import chatbot
        pattern = r"\b(text editor|whatsapp|github|linkedin|chrome)"
        match = re.search(pattern , command)
        speak(f"opening {match.group(0)}")
        profile_id = '2'
        # Define the path of the Chrome executable
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        # Build the command-line arguments to pass to Chrome
        args = [chrome_path, '--profile-directory=Profile ' + profile_id]
        # Start a new process for Chrome with the specified profile ID
        subprocess.Popen(args)     
    
    elif( ("open file manager" in command) or ("open manager" in command) ):
        speak("opening file manager")
        os.startfile(".")
    
    elif( ("setting" in command) ):
        speak("opening windows setting")
        os.system("start ms-settings:")
    
    elif("send message" in command ):
        name = command.replace("send message to" , "")
        name = name.strip()
        print("sending message to-" , name )
        speak("what's the message sir")
        text = input("enter message sir : ")
        for i in data.keys():
            if( i == name ):
                print(data[i])
                # extract the hour and minute components
                now = datetime.datetime.now()
                current_hour = now.hour 
                current_minute = now.minute + 1
                print(current_hour , "   " , current_minute )
                pywhatkit.sendwhatmsg( "+91"+ data[i] , text , current_hour , current_minute )    
            else:
                continue
        else:
            pass
            
   
    
    

    elif( ("search" in command) or ("what is" in command) or ( "find" in command ) ):
        command = command.replace("sofia" , "").replace("search" , "")
              
        print("searched item:" ,command)        
        completion = openai.Completion.create(
        engine = "text-davinci-003",    
        prompt = command ,
        max_tokens = 1000
        )        
        speak( completion.choices[0]["text"] )
    
    elif( "open window" in command ):
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(2)
        pyautogui.keyUp("alt")

    elif( ("switch" in command) ):
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("alt")

    elif( ("shutdown" in command) or ("close pc" in command) ):
        sec = re.search(r'\d+' , command)
        if sec:
            numeric_value = int(sec.group())
            print(f'pc will shut down in {numeric_value} second')
            speak( f'pc will shut down in {numeric_value} second' )
            os.system(f'shutdown /s /t {numeric_value}')
        else:   
            speak( f'pc will shut down in {30} second' )              
            os.system(f'shutdown /s /t {30}')
            
    elif( ("stop shut down" in command) or ("stop" in command) or ("abort" in command)):     
        speak( "alright sir , abort shut down" )               
        os.system('shutdown /a')

    elif( "text input" in command ):
        flag = 1

    elif( "stop speak" in command ):
        engine.stop()
        engine.runAndWait()







    









# Set up your API key

# def Commands( text ):

#     if(text.find("open notepad" ) != -1):
#         print("hello")

    # elif( ( text.find("shut down") != -1 ) or ( text.find("close pc") != -1 ) ):
    #     print(text)
    #     sec = re.search(r'\d+' , text)
    #     if sec:
    #         numeric_value = int(sec.group())
    #         print(f'pc will shut down in {numeric_value} second')
    #         engine.say(f'pc will shut down in {numeric_value} second')
    #         engine.runAndWait()
    #         os.system(f'shutdown /s /t {numeric_value}')
    #     else:
    #         engine.say(f'pc will shut down in {30} second')
    #         engine.runAndWait()                   
    #         os.system(f'shutdown /s /t {30}')
            
    # elif( text.find("abort") != -1 or text.find("stop shut down") != -1  or text.find("stop") != -1 ):
    #     engine.say("alright sir , abort shut down")
    #     engine.runAndWait()                     
    #     os.system('shutdown /a')

#     elif( text.find("open mic") != -1 ):
#         os.startfile("D:\wo mic\wo mic setup data\WOMic\WOMicClient.exe")
#         engine.say("opening wo mic")

#     elif( text.find("open control") != -1 ):
#         os.system("control")

#     elif( text.find("open manager") != -1 or text.find("open file manager") != -1):
#         os.startfile(".")
    
#     elif( text.find("window setting") != -1 or text.find("setting") != -1 ):
#         os.system("start ms-settings:")

#     elif( text.find("sofia") != -1 or text.find("search") ):
#         searchStr2 = text.replace("sofia" , "")
#         searchStr = searchStr2.replace("search" , "")
                
#         print("searched item : " ,  searchStr)

#         completion = openai.Completion.create(
#         engine = "text-davinci-003",    
#         prompt = searchStr ,
#         max_tokens = 1000
#         )

#         print(completion.choices[0]["text"])
#         engine.say(completion.choices[0]["text"])
#         engine.runAndWait() 

#     # elif( text.find("whatsapp") != -1 ):
        
                


# # Initialize recognizer instance
# r = sr.Recognizer()


# # Set the microphone as a source
# with sr.Microphone() as source:
#     # Adjust for ambient noise
#     r.adjust_for_ambient_noise(source)
#     print("Listening...")
#     # Continuously listen for speech until interrupte

#     engine.say("how do you like to give command")
#     engine.runAndWait()
#     choice = input("Text/keyboard or Voice/microphone : ")

#     while True:

#         if( choice.find("text") != -1  or choice.find("keyboard")):
#             while True:
#                 text = input("Give Command ")
#                 if( text.find("use microphone") != -1 or text.find("use Voice") != -1 ):
#                     break
#                 Commands(text)

#         if( choice.find("voice") != -1 or choice.find("microphone") ):
#             while True:   
#                 print("say something : ")
#                 # Record the audio
#                 audio = r.listen(source, phrase_time_limit=10)
#                 # Convert speech to text  
#                 try:
#                     text = r.recognize_google(audio , language="en-US" , show_all=False)
#                     text  = text.lower()  
#                     if( text.find("use text") != -1 or text.find("use keyboard") != -1 ):
#                         break  

#                     Commands(text)

#                     if( text.find("stop") ):
#                         engine.stop()
#                         continue
                    
#                     # Print the text
#                     print("You said: " + text)


#                 except sr.UnknownValueError:
#                     print("Could not understand audio")
#                 except sr.RequestError as e:
#                     print("Could not request results; {0}".format(e))
#                 except KeyboardInterrupt:
#                     # Exit loop if user interrupts
#                     break


