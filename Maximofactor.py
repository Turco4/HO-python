#Calcula del multiplo primo de mayor valor que divide a 600851475143.

num=600851475143
FactorM=2
FactorA=2
print "Número:"+str(num)
while num>1:
    while num%FactorA==0:
        FactorM=FactorA
        num=num/FactorA
    FactorA+=1
print "Maximo Factor:"+str(FactorM)
