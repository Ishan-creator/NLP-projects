from gtts import gTTS
from playsound import playsound


class sound():
    
    def text_to_speech(text):
        
        speech = gTTS(text)
        speech_file = "speech.mp3"
        speech.save(speech_file)
        return playsound(speech_file)
    
    
    
        
    

    
    
    
