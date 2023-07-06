# Audio file formats
# .mp3
# .flac
# .wav
import wave

# Audio signal parameters
# - number of channels (like the audio is coming from two different directions)
# - sample width (numbers of bytes for each sample)
# - framerate/sample_rate (number of samples for each second, like 44,100 Hz standrad sampling rate for CD quality means 44,100 sample values in each second) 
# - number of frames
# - values of a frame (when we load it, it will be in a binary format, but we can convert it to integer values later)

# open wave file
obj = wave.open("output.wav",'rb')

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate.", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters:", obj.getparams())
frames = obj.readframes(obj.getnframes())

print(len(frames) / obj.getsampwidth(), frames[0], type(frames[0]))
obj.close()

# write wave file
sample_rate = 16000.0 # hertz
obj = wave.open("new_file.wav",'wb')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sample_rate)
obj.writeframes(frames)
obj.close()

