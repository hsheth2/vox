#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
    while (1) {
        char phoneme[128];
        char stress[128];
        scanf("%s", phoneme);
        scanf("%s", stress);
        char path[1024] = "./wav/";
        strcat(path, phoneme);
        strcat(path, stress);
        strcat(path, ".wav");
        printf("%s\n", path);
    }
}
