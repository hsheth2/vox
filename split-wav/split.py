from pydub import AudioSegment

import time
import os
import sys
import re
import argparse
import splitutil

sys.stdin.readline()
sys.stdin.readline()

data = []
for line in sys.stdin:
	line = list(filter(bool, line.strip().split(' ')))
	
	line[1] = 10*int(line[1])
	line[2] = 10*int(line[2])
	
	# print(line)
	data.append(line)
	
# print(data)

# times = [data[0][1]]
times = []
for x in data:
	times.append( x[:3] )

times.sort()
print(times)

def split_song(full_track, track_info):
	# print("\t{}) {}".format(str(index+1), track))
	start = track_info[1]
	end = track_info[2]
	duration = end-start
	track_path = './morgan/{}.wav'.format(track_info[0])
	full_track[start:][:duration].export(track_path, format="wav")

album = AudioSegment.from_file("goforward.wav", 'wav')
for part in times:
	print(part)
	split_song(album, part)