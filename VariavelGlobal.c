#include <stdio.h>

int variavel_global = 8;

int main()
{
    printf("Hello World\n");
    int variavel_local = 6;
    printf("%d, %d",variavel_local, variavel_global);
    teste();

    return 0;
}

int teste(){
    printf("%d",variavel_global);
    
}
