#include <pocketsphinx.h>

int
main(int argc, char *argv[])
{
    ps_decoder_t *ps;
    cmd_ln_t *config;
    FILE *fh;
    char const *hyp, *uttid, *phonemes;
    int16 buf[512];
    int rv;
    int32 score;
    ps_seg_t *seg;

    config = cmd_ln_init(NULL, ps_args(), TRUE,
                 "-hmm", MODELDIR "/en-us/en-us",
                 "-lm", MODELDIR "/en-us/en-us.lm.bin",
                 "-dict", MODELDIR "/en-us/cmudict-en-us.dict",
                 "-allphone", MODELDIR "model/en-us/en-us-phone.lm.bin",
                 "-logfn", "/dev/null",
                 NULL);
    if (config == NULL) {
        fprintf(stderr, "Failed to create config object, see log for details\n");
        return -1;
    }
    
    ps = ps_init(config);
    if (ps == NULL) {
        fprintf(stderr, "Failed to create recognizer, see log for details\n");
        return -1;
    }

    fh = fopen("/root/vox/Barry/output.raw", "rb");
    if (fh == NULL) {
        fprintf(stderr, "Unable to open input file\n");
        return -1;
    }

    rv = ps_start_utt(ps);
    
    while (!feof(fh)) {
        size_t nsamp;
        nsamp = fread(buf, 2, 512, fh);
        rv = ps_process_raw(ps, buf, nsamp, FALSE, FALSE);
    }
    
    rv = ps_end_utt(ps);
    hyp = ps_get_hyp(ps, &score);
 
    if (hyp != NULL) {
        printf("%-20s %-5s %-5s\n", "word", "start", "end");
        for (seg = ps_seg_iter(ps); seg; seg = ps_seg_next(seg)) {
            char const *word;
            int sf, ef;
            
            word = ps_seg_word(seg);
            ps_seg_frames(seg, &sf, &ef);
            printf("%-20s %-5d %-5d\n", word, sf, ef);
        }
    }

    fclose(fh);
    ps_free(ps);
    cmd_ln_free_r(config);
    
    return 0;
}
