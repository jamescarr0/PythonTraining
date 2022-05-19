import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
print(type(mic))
with mic as source:
    print("Adjusting for ambient noise..")
    r.adjust_for_ambient_noise(source)
    print("Say something: ")
    audio = r.listen(source)

try:
    print(f"You said '{r.recognize_google(audio, language='en-GB')}'")
except sr.UnknownValueError:
    # Speech unclear could not transcribe
    print("Error: unable to recognise speech.")