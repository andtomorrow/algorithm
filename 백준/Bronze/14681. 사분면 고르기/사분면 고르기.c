#include <stdio.h>

int main(void)
{
  int x, y;
  scanf("%d", &x);
  scanf("%d", &y);

  if (y > 0)
  {
    if (x > 0)
      putchar('1');
    else
      putchar('2');
  }
  else
  {
    if (x > 0)
      putchar('4');
    else
      putchar('3');
  }

  return 0;
}