#!/usr/bin/env python3

try:
	s = input(">>> ")

	import ast
	tree = ast.parse(s, mode = 'eval')
	assert not any(isinstance(node, ast.Call) for node in ast.walk(tree))
	del ast

	a = eval(compile(tree, filename = '', mode = 'eval'))

	import base64
	b = int.from_bytes(base64.b64decode(s), byteorder = 'little')
	del base64

	if a == b:
		flag = open("flag.txt").read().strip()
		print(flag)

except:
	print("Please check your inputs.")
