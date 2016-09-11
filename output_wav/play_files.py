#!usr/bin/env python
# coding=utf-8
import pyaudio
import wave
import sys
import scipy.io.wavfile
import scipy.interpolate
import numpy as np
from os.path import isfile

# length of data to read.
chunk = 1024

# create an audio object
p = pyaudio.PyAudio()
stream = None
frames = None
filename = None

interpol_frame = 100


def spec_smooth(frame, frame_previous):
    """
    Modified spectral smoothing algorithm with cubic spline interpolation
    """
    if frames is None:
        return None

    frame_num = [i for i in range(len(frame_previous))] + \
                [interpol_frame + i + len(frames_previous) for i in range(len(frame))]
    frame_arr = np.concatenate((frame_previous + frame))

    cs_interpolation = scipy.interpolate.CubicSpline(x=frame_num, y=frame_arr)
    interpol_val = np.array([cs_interpolation(len(frames_previous) + i) for i in range(interpol_frame)])

    return np.concatenate((interpol_val, frame))


try:
    filename_old = filename
    for filename in sys.stdin:
        filename = filename.strip()
        if len(filename) is 0:
            continue

        # open the file for reading.
        frames_previous = frames
        wf = wave.open(filename, "rb")

        # Begin smoothing code
        if filename_old is not None:
            filename_new = "./output_wav/" + filename.split('/')[-1][:-4] + "-" + \
                           filename_old.split('/')[-1][:-4] + ".wav"

            if not isfile(filename_new):
                rate, frames = scipy.io.wavfile.read(filename)
                add_frames = spec_smooth(frames, frames_previous)
                scipy.io.wavfile.write(filename_new, rate, add_frames)
            wf = wave.open(filename_new, "rb")

        # End smoothing code"""

        # open stream based on the wave object which has been input.
        if stream is None:
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

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
