#include <stdio.h>

void print_flag(void) {
   long long local_48 = 0x3948faf2b2d78fa1;
   long long local_40 = 0x8c6544581092c26b;
   long long local_38 = 0x896851660b56754a;
   int local_30 = 0x678dfd0c8d;
   int uStack_2b = 0xfdf22;
   int uStack_28 = 0xb9259b8fca;
   long long local_78 = 0x333c6ab858e52faa;
   long long local_70 = 0xde6231384258d615;
   long long local_68 = 0x77fcbde8b8e9a4cd;
   int local_60 = 0xa2c17a89a2;
   int uStack_5b = 0x3733da;
   int uStack_58 = 0x14b99d4bd8;
   long long local_20 = 0x25;

  int local_c;

  for (local_c = 0x24; local_c > 0; local_c--) {
    *((char*)&local_78 + local_c) =
         *((char*)&local_78 + local_c - 1) ^
         *((char*)&local_78 + local_c);
  }

  for (int local_10 = 0; local_10 < (int)local_20; local_10++) {
    *((char*)&local_78 + local_10) = *((char*)&local_78 + local_10) ^ 0x69;
  }

  for (int local_14 = 0; local_14 < (int)local_20; local_14++) {
    *((char*)&local_78 + local_14) =
         *((char*)&local_48 + local_14) ^ *((char*)&local_78 + local_14);
  }

  puts((char *)&local_78);
}

int main() {
  print_flag();
  return 0;
}
