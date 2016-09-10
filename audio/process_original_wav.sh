
# sox -r 16000 -e signed -b 16 -c1 goforward.raw goforward.wav
ffmpeg -i "preprocessing/$1.wav" -acodec pcm_s16le -ac 1 -ar 16000 "wav/$1.wav"
sox "wav/$1.wav" "raw/$1.raw"
