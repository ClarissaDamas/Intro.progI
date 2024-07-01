
#include <stdio.h>
#include <stdlib.h>

int main()
{
    float peso = 3.2; //criar variavel 15
    float *ponteiro;
    
    ponteiro = &peso;
    
    printf("conteudo = %f\n", peso); 
    printf("endereco de var = %p\n", &peso); //A forma correta para imprimir um ponteiro é o %p.
    printf("endereco do ponteiro = %p\n", &ponteiro );  //se eu tiro o & tenho o endereco apontado pelo ponteiro, com o & tenho o endereco do ponteiro
    //printf("\n\nEnd.");
    //while(1);
    //return 0;
    
