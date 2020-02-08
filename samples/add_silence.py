from pydub import AudioSegment
import os

for sample in os.listdir("."):
	if sample.endswith(".wav") and not sample.startswith("ss"):
		silence = AudioSegment.silent(duration=32000) # or be explicit
		song = AudioSegment.from_wav(sample) + silence
		song.export("ss"+sample)