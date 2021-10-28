/*
Descrição: Convertendo vetor de 16 posições para uma matriz 4x4
Autor: Alef Henrique Aparecido Costa Matias
*/

#include <stdio.h>

int main() {
  int v[16] = {0};
  int m[4][4];
  int x = 0;
  int i, j, o = 4;

  puts("Digite 16 números para carregar o vetor\n");

  for(x = 0; x < 16; x++){
    printf("Vetor [%i]: ", x);
    scanf("%i", &v[x]);
  }

  puts("\n");

  puts("Valores carregados nos vetores");
  for(x = 0; x < 16; x++){
    printf("%i  ", v[x]);
  }

  puts("\n");

  x = 0;
  puts("Valores carregados na matriz");
  do{
    do{
      m[i][j] = v[x++];
      j++;
    }while(j < o);
    i++;
    j = 0;
  }while(i < o);

  i = 0;
  while(i < o){
    while(j < o){
      printf("%i   ", m[i][j]);
      j++;
    }
    puts("\n");
    i++;
    j = 0;
  }
}