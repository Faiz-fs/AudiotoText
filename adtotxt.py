from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

r = sr.Recognizer()


def startConvertion(path="Audio - Martin Luther King - I Have A Dream.wav", lang='en-IN'):
    with sr.AudioFile(path) as source:
        audio_text = r.listen(source)
        text = r.recognize_google(audio_text, language=lang)
        print(text)


startConvertion()
