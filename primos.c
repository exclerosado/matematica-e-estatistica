/*
Verificando se um número é primo
*/

#include <stdio.h>
#include <math.h>

int main() {
  int i, n, result = 0;

  printf("Digite um número: ");
  scanf("%i", &n);

  for(i = 2;i <= sqrt(n);i++){
    if(n % i == 0){
      result++;
      break;
    }
  }

  if(n == 0){
    printf("O número %i não pode ser primo.", n);
  }
  else if(n <= 0){
    printf("Números negativos não podem ser primos.");
    return 0;
  }
  else if(result != 0 || n == 1){
    printf("O número %i não é primo.", n);
  }
  else{
    printf("O número %i é primo.", n);
  }
}