#include <stdio.h>

int main()
{
  int A = 0, B = 0;
  int num1 = 0, num10 = 0, num100 = 0;

  scanf("%d", &A);
  scanf("%d", &B);

  num100 = B / 100;
  num10 = (B % 100) / 10;
  num1 = B % 10;

  printf("%d\n", A * num1);
  printf("%d\n", A * num10);
  printf("%d\n", A * num100);
  printf("%d", A * B);

  return 0;
}