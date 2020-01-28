#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  char code[64];
  
  printf("I will execute your code instead of you. Give me machine code bytes: ");
  fflush(stdout);
  fgets(code, 64, stdin);

  printf("Executing...\n");

  (*(void(*)()) code)();

  printf("Since you reached here I bet you got the FLAG. Bye.\n");

  return 0;
}