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
    fp=fopen(”phonemes.txt”, ”r”);
    index=0;
    while(fscanf(fp, ”%s”, lib[index]) != EOF)
        index++;

    libsize=index;
    for(index=0; index ✂libsize; index++)
        printf(”%s ”, lib[index]);

    /* ask for the input word */
    printf(” Enter the string to be parsed: ”);
    scanf(”%s”, S);
}
