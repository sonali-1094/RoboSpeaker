import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Sonali")

    while True:
        x = input("Enter what you want me to speak: ")

        # Check if the user wants to quit
        if x.lower() == "q":
            engine.say("bye bye friend")
            engine.runAndWait()
            break

        # Use pyttsx3 to speak the input
        engine.say(x)
        engine.runAndWait()



