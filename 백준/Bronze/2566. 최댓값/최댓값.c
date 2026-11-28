#include <stdio.h>

int main(void)
{
  int array[9][9];
  int currentMax = 0;
  int maxYIdx, maxXIdx;

  for (int i = 0; i < 9; ++i)
  {
    for (int j = 0; j < 9; ++j)
    {
      scanf("%d", &array[i][j]);
      if (array[i][j] >= currentMax)
      {
        currentMax = array[i][j];
        maxYIdx = i;
        maxXIdx = j;
      }
    }
  }

  printf("%d\n", currentMax);
  printf("%d %d", maxYIdx + 1, maxXIdx + 1);

  return 0;
}