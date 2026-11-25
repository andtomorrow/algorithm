#include <stdio.h>

int main(void)
{
  int inputScore;

  scanf("%d", &inputScore);

  if (inputScore >= 90)
    putchar('A');
  else if (inputScore >= 80)
    putchar('B');
  else if (inputScore >= 70)
    putchar('C');
  else if (inputScore >= 60)
    putchar('D');
  else
    putchar('F');

  return 0;
}