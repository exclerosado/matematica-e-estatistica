/*
Calculando o determinante de uma matriz 2x2
Autor: Alef Matias
*/

#include <stdio.h>

int main(void) {
  int matriz[2][2];
  int diagP = 0, diagS = 0;
  int mdiagP = 1, mdiagS = 1;
  int i, j;
  int ordem = 2;
  int det = 0;

  //Recebendo os valores da matriz
  for(int i = 0; i < ordem; i++){
    for(int j = 0; j < ordem; j++){
      printf("Posição [%i][%i]: ", i, j);
      scanf("%i",&matriz[i][j]);
    }
  }

  printf("\n");

  //Exibindo a matriz
  for(int i = 0; i < ordem; i++){
    for(int j = 0; j < ordem; j++){
      printf("[  %i  ] ", matriz[i][j]);
    }
    printf("\n");
  }
  printf("\n");

  //Efetuando os cálculos na matriz
  for(i = 0; i < ordem; i++){
    for(j = 0; j < ordem; j++){

      //Calculando os elementos da diagonal principal
      if (i + j == ordem - 1){
        diagS += matriz[i][j];
        mdiagS *= matriz[i][j];
      }

      //Calculando os elementos da diagonal secundária
      if(i == j){
        diagP += matriz[i][j];
        mdiagP *= matriz[i][j];
      }
    }
  }

  printf("Soma da diagonal principal: %i", diagP);
  printf("\nSoma da diagonal secundária: %i", diagS);
  printf("\nMultiplicação diagonal principal: %i", mdiagP);
  printf("\nMultiplicaçãp diagonal secundária: %i", mdiagS);
  printf("\nDeterminante: %i", det = mdiagP - mdiagS);
  
}