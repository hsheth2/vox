#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import sys
import Queue
import thread

work = Queue.Queue()

def processor(_):
	# recognize speech using Google Speech Recognition
	try:
		while True:
			try:
				print >> sys.stderr, "Worker waiting for audio to process"
				audio = work.get(block=True)
				print >> sys.stderr, "Worker got some data to process"
			
				# for testing purposes, we're just using the default API key
				# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
				# instead of `r.recognize_google(audio)`
				ans = r.recognize_google(audio)
				print >> sys.stderr, "Google Speech Recognition thinks you previously said " + ans
				for x in ans.strip().split(' '):
					print x
				sys.stdout.flush()
			except sr.UnknownValueError:
				print >> sys.stderr, "Google Speech Recognition could not understand audio"
	except sr.RequestError as e:
		print >> sys.stderr, "Could not request results from Google Speech Recognition service; {0}".format(e)
		thread.interupt_main()

thread.start_new_thread(processor, ("dummy", ))

try:
	r = sr.Recognizer()
	r.non_speaking_duration = 0.25
	r.pause_threshold = 0.4
	
	# obtain audio from the microphone
	with sr.Microphone() as source:
		print >> sys.stderr, "Please remain silent for 1 second to allow for calibration"
		r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
		print >> sys.stderr, "Energy threshold is now {}.".format(r.energy_threshold)
		
		while True:
			print >> sys.stderr, "Say something!"
			audio = r.listen(source)
			work.put(audio)
			print >> sys.stderr, "Got some data from the mic... processing. "
except KeyboardInterrupt:
	sys.exit(0)

"""# recognize speech using Google Speech Recognition
try:
	# for testing purposes, we're just using the default API key
	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	# instead of `r.recognize_google(audio)`
	print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))
"""

"""# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
	print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
	print("Wit.ai could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Wit.ai service; {0}".format(e))
"""

