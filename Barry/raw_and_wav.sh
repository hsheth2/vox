
# sox -r 16000 -e signed -b 16 -c1 goforward.raw goforward.wav
ffmpeg -i "Dreams From My Father Barack Obama (Full Audiobook) Narrated by Barack Hussein Obama. (Part 1).wav" -acodec pcm_s16le -ac 1 -ar 16000 output.wav
sox output.wav output.raw
