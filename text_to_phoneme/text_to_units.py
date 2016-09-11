import re
import sys

FILE='barack'
if len(sys.argv) >= 2:
	FILE = sys.argv[1]

dictionary = {}
with open('cmudict.dict', 'r') as inp:
	for line in inp:
		line = line.strip()
		if len(line) is 0:
			continue
		word, pron = line.split(' ', 1)
		dictionary[word.lower()] = re.sub(r'\d', '', pron).split(' ')

# print dictionary

def print_phoneme(ph):
	print '../audio/phonene/{}/{}.wav'.format(FILE, ph)

print >> sys.stderr, "waiting for initial data within text_to_units.py"
for word in sys.stdin:
	print >> sys.stderr, "got some data from text_to_units.py"
	word = word.strip().lower()
	if len(word) is 0:
		continue

	try:
		full = dictionary[word]
		for ph in full:
			print_phoneme(ph)
		sys.stdout.flush()
	except KeyError:
		print >> sys.stderr, "Could not find '{}' in dictionary".format(word)


