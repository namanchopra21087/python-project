from transformers import pipeline
from scipy.io.wavfile import write
import numpy as np
import sounddevice as sd

speech = pipeline("text-to-speech",model="facebook/mms-tts-eng")
out=speech(input("Enter text to convert to speech:"))

print(out)

# --- FIX AUDIO SHAPE ---
audio = np.asarray(out["audio"]).squeeze()

# Safety check
if audio.ndim != 1:
    raise ValueError("Audio is not 1-dimensional")

# Normalize and convert to int16
audio = audio / np.max(np.abs(audio))
audio_int16 = (audio * 32767).astype(np.int16)

# Play audio via speakers
sd.play(audio, int(out["sampling_rate"]))
sd.wait()  # wait until playback finishes

write(
    "output.wav",
    int(out["sampling_rate"]),
    audio_int16
)

print("Audio saved as output.wav")