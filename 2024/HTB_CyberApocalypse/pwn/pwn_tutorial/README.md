This is a simple questionnaire to get started with the basics.

◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉
◉                                                                                           ◉
◉  C/C++ provides two macros named INT_MAX and INT_MIN that represent the integer limits.   ◉
◉                                                                                           ◉
◉  INT_MAX = 2147483647                  (for 32-bit Integers)                              ◉
◉  INT_MAX = 9,223,372,036,854,775,807   (for 64-bit Integers)                              ◉
◉                                                                                           ◉
◉  INT_MIN = –2147483648                 (for 32-bit Integers)                              ◉
◉  INT_MIN = –9,223,372,036,854,775,808  (for 64-bit Integers)                              ◉
◉                                                                                           ◉
◉  When this limit is passed, C will proceed with an 'unusual' behavior. For example, if we ◉
◉  add INT_MAX + 1, the result will NOT be 2147483648 as expected, but something else.      ◉
◉                                                                                           ◉
◉  The result will be a negative number and not just a random negative number, but INT_MIN. ◉
◉                                                                                           ◉
◉  This 'odd' behavior, is called Integer Overflow.                                         ◉
◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉

[*] Question number 0x1:

Is it possible to get a negative result when adding 2 positive numbers in C? (y/n)

>> y

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠


[*] Question number 0x2:

What's the MAX 32-bit Integer value in C?

>> 2147483647 

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠

[*] Question number 0x3:

What number would you get if you add INT_MAX and 1?

>> -2147483648 

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠


[*] Question number 0x4:

What number would you get if you add INT_MAX and INT_MAX?

>> -2

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠

[*] Question number 0x5:

What's the name of this bug? (e.g. buffer overflow)

>> buffer overflow

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                 ♠
♠      Wrong      ♠
♠                 ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠

[*] Question number 0x5:

What's the name of this bug? (e.g. buffer overflow)

>> integer overflow

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠


[*] Question number 0x6:

What's the MIN 32-bit Integer value in C? 

>> -2147483648

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠

[*] Question number 0x7:

What's the number you can add to INT_MAX to get the number -2147482312?

>> 1337

HTB{gg_3z_th4nk5_f0r_th3_tut0r14l}
