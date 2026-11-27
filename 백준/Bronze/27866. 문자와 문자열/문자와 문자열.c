#include <stdio.h>

int main(void)
{
  char inputWord[1001];
  int i;

  scanf("%1000s", inputWord);
  scanf("%d", &i);

  printf("%c", inputWord[i - 1]);

  return 0;
}