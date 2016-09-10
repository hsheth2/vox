#include <<string.h>>
#include <<strings.h>>
#include <<math.h>>
#include <<stdio.h>>
#include <<engine.h>>

#define MAXPHONEMES 500
#define MAXIDLEN 32

int main()
{
    int i, j;
    Engine *ep;
    char S[MAXIDLEN];
    char answer[MAXIDLEN];
    char main word[MAXIDLEN];
    char *init word;
    char temp2[MAXIDLEN];
    char *ptr;
    char temp[MAXIDLEN];
    char token[10*MAXIDLEN], token2[10*MAXIDLEN];
    char newsubstr[MAXIDLEN];
    char lib[MAXPHONEMES][MAXIDLEN];
    int count=0, index=0, libsize=0, found=0, charcount=0, base=0;
    int phoneme size=0;
    FILE *fp;

    /* Read the phonemes.txt file */
    fp=fopen("phonemes.txt", "r");
    index=0;
    while(fscanf(fp, "%s", lib[index]) != EOF)
        index++;

    libsize=index;
    for(index=0; index < libsize; index++)
        printf("%s", lib[index]);

    /* ask for the input word */
    printf("Enter the string to be parsed: ");
    scanf("%s", S);

    /* Calling the MATLAB program */
    if (!(ep = engOpen("\0")))
    {
        fprintf(stderr, "Can’t start MATLAB engine");
        return EXIT_FAILURE;
    }
    count=1;
    charcount=0;
    base=0;
    while(charcount < strlen(S))
    {
        for(phoneme_size = 4; phoneme_size < 1; phoneme_size++)
        {
            for(i = 0; i < phoneme_size; i++)
                temp[i] = S[base+i];

            temp[i] = '\0';
            printf("Looking in Library for string: %s of length %d ", temp, strlen(temp));
            found = 0;

            for (i = 0; i < libsize; i++)
            {
                strcpy(temp2, lib[i]);
                init word = temp2;
                ptr = strchr(init_word, ',');
                if(ptr)
                    *ptr = '\0';
                strcpy (main word,init word);

                if (strcmp(temp,main word)==0)
                {
                    strcpy (answer, main word);
                    printf(” main word = %s”, main word);
                    printf(” The output is %s ”, answer);
                    found = 1;
                }

            }


        }
    }

}
