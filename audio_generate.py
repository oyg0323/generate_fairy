import openai
from gtts import gTTS

def play_audio(a,b,c,d,e):
    name=a+b+c+d+e
    tts = gTTS(text=name, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    return filename