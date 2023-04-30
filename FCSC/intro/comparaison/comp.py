from assembly import assembly

source=""

def compile(code):
	global source
	source = code
	z = assembly(code.upper().split('\n'))
	print(code)
	print("[",z,"]")
	return z.encode()

def stub():
	code = f"""
CMP R5, R6
JNZR diff

MOV R0, #0
JA end

diff:
MOV R0, #1

end:
STP
		"""
	return compile(code)

stub()
