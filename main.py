import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't request results at the moment. Please try again later.")
        return ""

if __name__ == "__main__":
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Convert text to speech
        text_to_speech("You said: " + user_input)
        
        # Convert speech to text
        user_input_audio = speech_to_text()
        
        # Convert text to speech
        text_to_speech("You said: " + user_input_audio)
