import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize speech recognition and text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I assist you today?")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}\n")
    except Exception as e:
        print("Sorry, I did not catch that. Can you please repeat?")
        return ""

    return query.lower()

# import wikipedia

def execute_command(command):
    if 'wikipedia' in command:
        query = command.replace('wikipedia', '')
        try:
            results = wikipedia.summary(query, sentences=2)
            print(results)
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Multiple results found for '{query}'. Please specify your query more specifically.")
            print("Possible options:")
            options = e.options[:5]  # Limit the number of options displayed
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
        except wikipedia.exceptions.PageError:
            print("No results found for the given query.")
        except Exception as e:
            print("An error occurred during the Wikipedia search:", e)

# Rest of your code


        speak("According to Wikipedia")
        speak(results)
    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "play music" in command:
        music_dir = "path/to/your/music/folder"
        songs = os.listdir(music_dir)
        if len(songs) > 0:
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music files found in the specified directory.")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I am not programmed to perform that task.")

# Main program loop
if __name__ == "__main__":
    greet()

    while True:
        command = listen()
        if command:
            execute_command(command)
