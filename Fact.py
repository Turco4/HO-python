n=146
def factorprimo (n):
	s = ' '
	i = -1
	j = 0
	fact = [2] + [x for x in range(3,n+1,2)]
	while i < len(fact) - 1:
	    i += 1
		while True:
			if n % fact[i] == 0:
				j += 1
				n = int(n/fact[i])
			else:
			    if j > 0: 
				s += str(fact[i]) + '^' + str(j) + 'x'
				j = 0
				break
	return s.rstrip(' x ')
