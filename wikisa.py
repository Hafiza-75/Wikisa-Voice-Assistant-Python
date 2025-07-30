import pyttsx3
import datetime
import wikipedia
import time

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def talk(text):
    print("🗣️ Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def get_command():
    return input("👉 Type your command: ").lower()

def search_wikipedia(command):
    try:
        # Clean up user input
        for phrase in ['who is', 'what is', 'tell me about']:
            command = command.replace(phrase, '')
        command = command.strip()

        # Search Wikipedia for suggestions
        search_results = wikipedia.search(command)
        if not search_results:
            return "Sorry, I couldn't find anything on that topic."

        # Use the top result
        summary = wikipedia.summary(search_results[0], sentences=2)
        return summary
    except Exception as e:
        return "Sorry, something went wrong while searching."

def run_assistant():
    command = get_command()

    if 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time_now}")

    elif 'who is' in command or 'what is' in command or 'tell me about' in command:
        info = search_wikipedia(command)
        talk(info)

    elif 'hello' in command:
        talk("Hello there! How can I help you?")

    elif 'exit' in command or 'bye' in command:
        talk("Goodbye!")
        exit()

    else:
        talk("Sorry, I didn't understand that.")

# Main loop
while True:
    run_assistant()
    time.sleep(1)
