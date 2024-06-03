from modules.tts import sound
from modules.input import input
from modules.llm import llm



inputt = input.speech_to_text()


from_llm = llm.llm_responce(inputt)


llm_responce = sound.text_to_speech(from_llm)