import pyttsx3

print("Initializing TTS engine...")
try:
    engine = pyttsx3.init()
    engine.say("If you can hear this, the test was successful.")
    print("Engine initialized. Speaking now...")
    engine.runAndWait()
    print("Test finished.")
except Exception as e:
    print(f"An error occurred: {e}")
