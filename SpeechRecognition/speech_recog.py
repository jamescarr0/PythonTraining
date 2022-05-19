import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile("/Users/james/dev/python/realpython/SpeechRecognition/harvard.wav")
noisey_harvard = sr.AudioFile("/Users/james/dev/python/realpython/SpeechRecognition/jackhammer.wav")

with harvard as src:
    r.adjust_for_ambient_noise(src, duration=0.5)
    audio = r.record(src)

print("Transcript.....")
print(r.recognize_google(audio))
print()
print("Show all useful for degbugging..")
print(r.recognize_google(audio, show_all=True))