from pydub import AudioSegment

import time
import os
import sys
import re
import argparse
import splitutil

FILE = "goforward"
if len(sys.argv) >= 2:
	FILE = sys.argv[1]

sys.stdin = open('../audio/times/{}.txt'.format(FILE))

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

times.sort(reverse=True)
print(times)

def split_song(full_track, track_info):
	# print("\t{}) {}".format(str(index+1), track))
	start = track_info[1]
	end = track_info[2]
	duration = end-start
	track_path = '../audio/phonene/{}/{}.wav'.format(FILE, track_info[0])
	full_track[start:][:duration].export(track_path, format="wav")

os.makedirs('../audio/phonene/{}'.format(FILE), exist_ok=True)
album = AudioSegment.from_file("../audio/wav/{}.wav".format(FILE), 'wav')
for part in times:
	print(part)
	split_song(album, part)