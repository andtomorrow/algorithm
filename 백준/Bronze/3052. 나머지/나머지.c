#include <stdio.h>

int main(void)
{
  int inputNum;
  int remainders[42] = {0};
  int numRemainders = 0;

  for (int i = 0; i < 10; ++i)
  {
    scanf("%d", &inputNum);
    remainders[inputNum % 42] = 1;
  }

  for (int i = 0; i < 42; ++i)
  {
    if (remainders[i] != 0)
    {
      numRemainders += 1;
    }
  }

  printf("%d", numRemainders);

  return 0;
}