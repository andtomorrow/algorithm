#include <stdio.h>

int main(void)
{
  int inputYear;

  scanf("%d", &inputYear);

  if (inputYear % 4 == 0)
  {
    if (inputYear % 400 == 0)
      putchar('1');
    else if (inputYear % 100 != 0)
      putchar('1');
    else
      putchar('0');
  }
  else
    putchar('0');

  return 0;
}