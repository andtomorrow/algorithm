#include <stdio.h>

int main(void)
{
  int H, M;
  int min;

  scanf("%d%d", &H, &M);

  min = H * 60 + M;
  min -= 45;

  H = min / 60;
  M = min % 60;

  if (M < 0)
  {
    H = 23;
    M += 60;
  }

  printf("%d %d", H, M);

  return 0;
}