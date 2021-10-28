/*
Cálculo de fatorial
*/

#include <stdio.h>

int main() {
  int fatorial, numero;

  printf("Insira um número para calcular o fatorial: ");
  scanf("%i", &numero);
  
  if(numero < 0){
      printf("Números negativos não são aceitos!");
      return 0;
    }

  for(fatorial = 1;numero > 1;numero--){
    fatorial *= numero;
  }
  printf("Fatorial: %i", fatorial);
}