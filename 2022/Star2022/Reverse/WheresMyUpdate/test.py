import dis
import marshal

with open('chall.pyc', 'rb') as f:
    f.seek(16)
    dis.dis(marshal.load(f))
