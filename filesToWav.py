#!usr/bin/env python  
#coding=utf-8  
import pyaudio
import wave
import sys

# length of data to read.
chunk = 1024

# create an audio object
p = pyaudio.PyAudio()
stream = None

try:
	for filename in sys.stdin:
		filename = filename.strip()
		if len(filename) is 0:
			continue
		
		# open the file for reading.
		wf = wave.open(filename, "rb")

		# open stream based on the wave object which has been input.
		if stream is None:
			stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
			                channels = wf.getnchannels(),
			                rate = wf.getframerate(),
			                output = True)

		# read data (based on the chunk size)
		data = wf.readframes(chunk)

		# play stream (looping from beginning of file to the end)
		while data != '':
			# writing to the stream is what *actually* plays the sound.
			stream.write(data)
			data = wf.readframes(chunk)
		
except KeyboardInterrupt:
	pass
finally:
	# cleanup stuff.
	if stream is not None:
		stream.close()
	p.terminate()
	print >> sys.stderr, "Cleanup finished"