stdbuf -i0 -o0 -e0 command
#(cd google_speech ; python -u listener_recognize.py )
cat recog_words | (cd text_to_phoneme ; python -u text_to_units.py 'nickvoice') | stdbuf -i0 -o0 -e0 tee phons | (cd output_wav ; python -u play_files.py)
