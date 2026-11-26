#include <stdio.h>

int main(void)
{
  int N;

  scanf("%d", &N);

  for (int i = 1; i <= N; ++i)
  {
    for (int j = N - i - 1; j >= 0; --j)
    {
      putchar(' ');
    }
    for (int k = 0; k < i; ++k)
    {
      putchar('*');
    }

    putchar('\n');
  }

  return 0;
}