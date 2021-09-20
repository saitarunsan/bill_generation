from gtts import gTTS
from playsound import playsound

audio = 'voice.mp3'
language = 'en'

sp = gTTS(text="hello sai tarun how python preperation is going on..",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print('=========here is your audio===========')

