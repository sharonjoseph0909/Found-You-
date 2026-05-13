import speech_recognition as sr


def listen_here():
   # Create a recognizer object
   listening = sr.Recognizer()


   # Use the microphone as the audio source
   with sr.Microphone() as source:
       print("Listening, speak now...")


       listening.adjust_for_background_noise(source, duration=4)  # Adjust for ambient noise
     
       # Listen for audio and store it in the 'audio' variable
       audio = listening.listen(source)
       print("Processing voice...")


   try:
       # Use Google's speech recognition to convert audio to text
       text = listening.recognize_google(audio)
       print("You said: " + text)
       return text
  
   except sr.UnknownValueError:
       print("Sorry, I could not understand the audio.")
       return None
   except sr.RequestError:
       print("Could not request results from the speech recognition service; {0}".format(e))
       return None
  
# Use recursion to start listening
if __name__ == "__main__":
   listen_here()