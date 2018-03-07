# Sucesión Fibonacho y suma de sus terminos.

fibo=[]
C = 0
U = 1
num = int(29)
for n in range(num):
	fibo.append(C + U)
	K = C + U
	C = U
	U = K
print(fibo)
print(sum(fibo))
