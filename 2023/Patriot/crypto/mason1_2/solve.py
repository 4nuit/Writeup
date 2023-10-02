import string
import random

def reverse_finalstage(w):
    # Reverse the operations of finalstage
    flag = ''
    w = list(w)
    i = 0
    while i < len(w):
        if i + 1 < len(w):
            flag += w[i+1] + w[i]
            i += 2
        else:
            flag += w[i]
            i += 1
    flag = list(flag)
    flag.reverse()
    return "".join(g for g in flag)

def reverse_stage2(b):
    # Reverse the operations of stage2
    t = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++.++++++.-----------.++++++."[-15:(7*9)].strip('-')
    reversed_str = ''
    random.seed(10)  # Set the seed to ensure the random values are consistent
    for q in range(len(b)):
        reversed_str += chr(ord(b[q]) + random.randint(0, 5))
    return reversed_str

def reverse_stage1(a):
    # Convert the string to a list for modification
    a = list(a)
    b = list(string.ascii_lowercase)
    z = list(a)
    for y in range(len(z)):
        b[y%len(b)] = chr((ord(z[y])^ord(a[y]))+len(b))
    for o in range(len(a)):
        a[o] = chr(ord(a[o])^o)
    # Convert the list back to a string before returning
    return "".join(x for x in a)


def reverse_entry(f):
    # Reverse the operations of entry
    f = list(f)
    f.reverse()
    return "".join(i for i in f)

# Start with the string `^seqVVh+]>z(jE=%oK![b$\NSu86-8fXd0>dy`
input_str = "^seqVVh+]>z(jE=%oK![b$\\NSu86-8fXd0>dy"


# Reverse the operations step by step
reversed_finalstage = reverse_finalstage(input_str)
reversed_stage2 = reverse_stage2(reversed_finalstage)
reversed_stage1 = reverse_stage1(reversed_stage2)
reversed_entry = reverse_entry(reversed_stage1)

print(reversed_entry)
