#include <stdio.h>
#include <stdlib.h>

int pair(int size, char* argv[], int indx_start, int indx_curr)
{
  if(!atoi(argv[indx_start]))
    return 1;
  else if(indx_curr==size)
    return 0;
  else if(atoi(argv[indx_curr])==atoi(argv[indx_start]))
  {
    argv[indx_curr]="0";
    argv[indx_start]="0";
  }
  return pair(size, argv, indx_start, indx_curr+1);
}


//arguments syntax: <ages separated by space>
//the minimum age is supposed to be an integer bigger than 0.
int main(int argc, char* argv[])
{
  int size=argc;
 int i=1;
  while(i<size&&pair(size, argv, i, i+1))
     ++i;
  i==size ? printf("Everybody's got a pair.\n") : printf("The person alone is %d years old.\n", atoi(argv[i]));
}
