import speech_recognition as sr

recognizer = sr.Recognizer()


class input():
    def speech_to_text():
        with sr.Microphone() as source:
            print("Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
            print("okayy")

            try:
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                print(text)
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                
        return text
    




