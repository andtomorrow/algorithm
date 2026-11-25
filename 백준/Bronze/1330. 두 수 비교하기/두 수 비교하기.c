#include <stdio.h>

int main(void)
{
  int A, B;
  scanf("%d%d", &A, &B);

  if (A > B)
    putchar('>');
  else if (A < B)
    putchar('<');
  else if (A == B)
    printf("==");

  return 0;
}