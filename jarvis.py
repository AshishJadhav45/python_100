import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query


def execute_command(command):
    if 'time' in command:
        time()
    elif 'date' in command:
        date()
    elif 'wikipedia' in command:
        query = command.replace('wikipedia', '')
        try:
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak(f"Multiple results found for '{query}'. Please specify your query more specifically.")
            speak("Possible options:")
            options = e.options[:5]  # Limit the number of options displayed
            for i, option in enumerate(options, 1):
                speak(f"{i}. {option}")
        except wikipedia.exceptions.PageError:
            speak("No results found for the given query.")
        except wikipedia.exceptions.WikipediaException as e:
            speak("An error occurred during the Wikipedia search.")
            print(e)
    else:
        speak("I am sorry, I don't have information about that.")


while True:
    command = listen().lower()
    if 'exit' in command:
        break
    execute_command(command)
