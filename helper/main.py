from modules.tts import sound
from modules.input import input
from modules.llm import llm
from modules.youtube import utube_play



inputt = input.speech_to_text()

if inputt == "open YouTube":
    print(" "*1000)
    what = input.speech_to_text()
    search_keyword = what
    utube_play()

    
    
else:    
    from_llm = llm.llm_responce(inputt)
    llm_responce = sound.text_to_speech(from_llm)