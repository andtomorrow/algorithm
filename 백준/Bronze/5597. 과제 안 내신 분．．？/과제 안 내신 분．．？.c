#include <stdio.h>

int main(void)
{
  int completed[30] = {0};
  int stdNum;

  for (int i = 0; i < 28; ++i)
  {
    scanf("%d", &stdNum);

    completed[stdNum - 1] = 1;
  }

  for (int i = 0; i < 30; ++i)
  {
    if (completed[i] == 0)
    {
      printf("%d\n", i + 1);
    }
  }

  return 0;
}