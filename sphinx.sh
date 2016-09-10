pocketsphinx_continuous -infile ~/vox/split-wav/goforward.raw -hmm ~/install-cmu/pocketsphinx-5prealpha/model/en-us/en-us \
                        -allphone ~/install-cmu/pocketsphinx-5prealpha/model/en-us/en-us/en-us-phone.lm.bin -backtrace yes \
                        -beam 1e-20 -pbeam 1e-20 -lw 2.0
