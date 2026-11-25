#include <stdio.h>

int main(void)
{
  int H, M;
  int cookMin;
  int currentMin;

  scanf("%d%d", &H, &M);
  scanf("%d", &cookMin);

  currentMin = 60 * H + M + cookMin;

  H = currentMin / 60;
  M = currentMin % 60;

  H %= 24;

  printf("%d %d", H, M);

  return 0;
}