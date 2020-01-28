#include <unistd.h>
#include <string.h>
#define FLAG "NITAC{n0w_u_kn0w_h0w_2_c4us3_RCE_us1ng_LFI}\n"
int main() {
  write(1, FLAG, strlen(FLAG));
}
