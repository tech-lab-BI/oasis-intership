import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define responses to common greetings
greetings = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi! What's up?",
    "hey": "Hey! What can I do for you?"
}

# Define a function to respond to voice commands
def respond_to_voice_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="en-US")
            print("You said: " + command)
            command = command.lower()

            # Respond to greetings
            if command in greetings:
                engine.say(greetings[command])
                engine.runAndWait()

            # Tell the time
            elif "what time" in command or "what's the time" in command:
                time = datetime.datetime.now().strftime("%I:%M %p")
                engine.say("The current time is " + time)
                engine.runAndWait()

            # Tell the date
            elif "what date" in command or "what's the date" in command:
                date = datetime.datetime.now().strftime("%B %d, %Y")
                engine.say("Today's date is " + date)
                engine.runAndWait()

            # Search the web
            elif "search" in command or "look up" in command:
                query = command.replace("search ", "").replace("look up ", "")
                engine.say("Searching for " + query)
                engine.runAndWait()
                webbrowser.open("https://www.google.com/search?q=" + query)

            # Unknown command
            else:
                engine.say("Sorry, I didn't understand that.")
                engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print("Error: " + str(e))

# Run the voice assistant
while True:
    respond_to_voice_command()
