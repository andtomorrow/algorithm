#include <stdio.h>
#include <string.h>

int main(void)
{
  int T;

  scanf("%d", &T);

  for (int i = 0; i < T; ++i)
  {
    int R;
    char inputString[21];
    scanf("%d%20s", &R, inputString);

    for (int j = 0; j < (int)strlen(inputString); ++j)
    {
      for (int k = 0; k < R; ++k)
      {
        printf("%c", inputString[j]);
      }
    }
    putchar('\n');
  }

  return 0;
}