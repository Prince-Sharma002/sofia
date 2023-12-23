
import pyttsx3
import threading

engine = pyttsx3.init()
text = "Hello world! How are you doing today? I hope you're having a great day adf kjsafh f fsdfhsdf  fdsfdsfdfds."

def speak():
    engine.say(text)
    engine.runAndWait()

def stop():
    engine.stop()

# Start speaking in a separate thread
speech_thread = threading.Thread(target=speak)
speech_thread.start()

# Check for user input to stop the speech
input("Press enter to stop speaking")

# Stop speaking
stop()

# Wait for the speech thread to finish
speech_thread.join()





