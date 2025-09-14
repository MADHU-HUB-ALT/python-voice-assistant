import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.say(text)
    engine.runAndWait()

print("Simple Voice Assistant. Type 'exit' to quit.")

while True:
    text = input("Enter any text: ")
    if text.lower() == 'exit':
        say("Goodbye!")
        break
    say(text)

