#3
x=int(input("ingresar x: "))
n=int(input("ingresar n: ")) # Pido x y n
def pot(x,n): 
    if n==1:
        return x
    else:
        return x*pot(x,n-1) # Hago la funcion con recursión
print(pot(x,n)) # se imprime