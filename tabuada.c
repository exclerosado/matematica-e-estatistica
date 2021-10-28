/*
Descrição: Tabuada com Do While
Autor: Alef Matias
*/

#include <stdio.h>

int main()
{
    int num;
    int i = 0;
    
    printf("Escolha o número da tabuada desejada: ");
    scanf("%i", &num);
    
    do{
        i = i + 1;
        printf("\n%d X %d = %d", num, i, num * i);
    }while(i < 10);
}

