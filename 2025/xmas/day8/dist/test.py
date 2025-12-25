#!/usr/bin/env python3
# encode_for_jail.py
# Usage:
#   python3 encode_for_jail.py "TARGET STRING"
# Example:
#   python3 encode_for_jail.py "tr '\0' '\n' < /proc/$(awk '{print $4}' /proc/$$/stat)/environ|grep -i flag"
#
# Output: one long line you can paste into the jail prompt. The output line will not contain
# letters, digits or spaces (it contains punctuation and $ only).
#
# WARNING: The produced payload can be very long. Paste it as a single line into the jailed prompt.

import sys

# Helper: produce an expression (string) that evaluates to "1" using only $$ and operators
ONE = '($$/$$)'

# Helper: produce expression for integer n using only ONE, +, *, parenthesis
def make_int_expr(n):
    # Build using binary decomposition to keep it shorter.
    # We cannot include digits in the literal, so we only use ONE, + and *.
    if n == 0:
        return f'($$-$$)'
    # produce n by summing powers of two
    parts = []
    bit = 0
    while n > 0:
        if n & 1:
            # compute (ONE << bit) as repeated doubling
            if bit == 0:
                parts.append(ONE)
            else:
                expr = ONE
                for _ in range(bit):
                    expr = f'(({expr})+({expr}))'   # multiply by 2
                parts.append(expr)
        n >>= 1
        bit += 1
    # sum parts
    if len(parts) == 1:
        return parts[0]
    return '(' + '+'.join(parts) + ')'

# Convert integer (0-255) to an expression producing that ASCII code
def ascii_expr(code):
    return make_int_expr(code)

# Build expression that prints a single byte using a dynamically-generated printf.
# We must generate a printf name and call it. The generator constructs a tiny command string
# like: printf '\\xHH' where HH is hex of code, but we cannot type 'printf' or hex digits.
# Instead we will reconstruct the *whole command string* (target bytes) and then run it via
# synthesized "bash -c" (we synthesize the letters for bash and -c via arithmetic->chars).
#
# Simpler approach used by this encoder:
# We will produce a single expression that builds the entire target command (the command
# we want executed) as a sequence of bytes and then ask /bin/bash -c "that command".
# Because the jailed child is already a bash process, we will call "eval" to execute the command
# string. But since we cannot type "eval" we will instead exploit command substitution:
#   $(printf '%b' <constructed-escapes>)
#
# Implementation detail: we produce a string of octal escapes like '\101\102...' using arithmetic
# to compute each digit; then we call builtin $'...' style at runtime by using printf with format %b.
#
# To keep the payload strictly free of letters/digits, we will *construct the word "printf"* from bytes
# and then call it via indirect invocation: $( $(constructed_printf) args ). That is tricky and may not
# work in all restricted shells; an alternative is to produce a command that contains only builtins,
# but constructing eval/builtins also requires letters. This encoder will output a conventional method:
#
# It builds a command that echoes the constructed bytes by using - the child shell's builtin printf
# invoked via its name reconstructed at runtime and executed via eval. This is mechanical but long.

def byte_to_octal_escape_expr(b):
    # returns an expression (string) that will, at runtime, evaluate to the three-octal-digit string like \101
    # We'll produce a string concatenation of three chars: backslash + digit + digit + digit
    # But digits cannot be literal in input; we produce each digit by arithmetic and use printf at runtime.
    # To keep things simpler for real-world usage, the encoder will build the entire final payload by
    # assembling characters via $'...' like escapes — but we cannot place digits inside $'...' literal.
    # So here we instead produce a marker placeholder; actual assembly happens later in the final python output.
    raise NotImplementedError("This small encoder is a generator scaffold. See usage instructions in the message.")

def usage_and_examples():
    print("""
This script is a scaffold that explains and automates the mechanical conversion of an ASCII target
into a punctuation-only payload for the jail. The actual conversion depends on small target-system
details; use the guidelines below to adapt if necessary.

Suggested workflow (practical):
1) Choose the *target command string* you want the jailed shell to execute. Typical target:
   tr '\\0' '\\n' < /proc/$(awk '{print $4}' /proc/$$/stat)/environ|grep -i flag
   (But note: '<' and '>' are blocked by the jail's filter; better to read file arguments than use redirection.)

2) Run a generator (this file is scaffold) to produce a punctuation-only payload. If you want, I can
   finish the generator for you into a fully-automated payload builder — tell me and I will produce
   the completed encoder that outputs a legit paste-ready line.

If you prefer, tell me which of the two target commands you want encoded now:
A) Read parent environ pipeline (preferred if flag exported into environment)
B) Fallback: find flag by reading /proc/<ppid>/mem and running strings+grep (less portable)
and I will output a fully-expanded one-liner payload for that target.
""")

if __name__ == '__main__':
    usage_and_examples()
