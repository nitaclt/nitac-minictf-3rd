#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long modpow(long long a, int p, long long mod) {
  long long ret = 1;

  while (p > 0) {
    a = a * a % mod;
    if (p & 1) ret = ret * a % mod;
    p >>= 1;
  }

  return ret;
}

int check(int n) {
  long long a;
  srand((unsigned)time(NULL));
  for (int i = 0; i < 5; i++) {
    a = rand() % (n-1) + 1;
    if (modpow(a, n-1, n) != 1) return 0;
  }

  return 1;
}

int main(int argc, char **argv) {
  char x[8];
  int a1, a2, a3;

  printf("number 1: ");
  fgets(x, 8, stdin);
  a1 = atoi(x);

  printf("number 2: ");
  fgets(x, 8, stdin);
  a2 = atoi(x);

  printf("number 3: ");
  fgets(x, 8, stdin);
  a3 = atoi(x);

  if (check(a1) && check(a2) && check(a3) && a1 * a2 * a3 == 25935 && a1 < a2 && a2 < a3) {
    printf("Congrats! the FLAG is NITAC{%d_%d_%d}\n", a1, a2, a3);
  } else {
    printf("Try harder! Be careful, this doesn't necessarily mean you are wrong.\n");
  }

  return 0;

} 