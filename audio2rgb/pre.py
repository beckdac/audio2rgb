#input preprocessing
from pydub import AudioSegment

def preprocessing(input, tmp):
    sound = AudioSegment.from_wav(input)
    sound = sound.set_channels(1)
    sound.export(tmp, format="wav")
