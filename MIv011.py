import speech_recognition as sr

r = sr.Recognizer()

i = 1
while i < 6:
    print(i)
    i += 1
    with sr.Microphone() as source:
        print("Szóljon!")
        audio = r.listen(source, phrase_time_limit=2)

        try:
            print("Google: " + r.recognize_google(audio, language="en-US"))
        except sr.UnknownValueError:
            print("Nem mondtál semmit!")
        except sr.RequestError as e:
            print("Valami baj van !!{0}".format(e))