import wave

frames = []
file_name = 'Kawai-K3-Piano-C3.wav'
w = wave.open(file_name, 'rb')
for i in xrange(w.getnframes()):
    frame = w.readframes(i)
    frames.append(frame)

frames_mod = [frame for frame in frames if frame != '']
