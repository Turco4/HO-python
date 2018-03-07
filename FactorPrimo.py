n=600851475143
def FactorM(n):
    num=n
    FactorM=2
    FactorA=2
    while num%2==0:
            FactorM=FactorA
            num=num/FactorA
    FactorA=3   
    mFactor=num**0.5 
    #print (mFactor)
    while FactorA<=num and FactorA<=mFactor:
        while num%factorA==0:
            FactorM=FactorA
            num=num/FactorA
        FactorA+=2          
        #print (FactorA,num)
    if FactorA>mFactor and num>FactorM:
        FactorM=num
    return FactorM
print(str(FactorM))
