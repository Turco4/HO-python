#Sucesión y suma de terminos tomados entre o y 1000 tomados de a 3 y de a 5. 

multi3= range(0,1000,3) 
multi5= range(0,1000,5)
factores = set(multi3) | set(multi5) 
print (factores)
print sum(factores)
