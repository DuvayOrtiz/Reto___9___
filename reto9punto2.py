#punto 2
#1
import math  # Importo libreria
def valorAbs(*args):     
    return math.fabs(x) # Hago la funcion con el args
if __name__ == "__main__":
    x=float(input("ingresar valor: ")) #pido una x
print("la distancia del punto al origen es  " + str(valorAbs(x))) #se imprime
#2
def factorial(*args): # Hago la funcion con el args
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
n = int(input("Ingrese numero para factorial : ")) #pido una x
print(factorial(n))  #se imprime
#3
n=int(input("ingresar n: ")) # Pido una variable
s=[]
f=[] # Hago dos arreglios
def factorial(n : int ):
    p = 1
    for i in range(1,n+1):
        p *= i
    return p # Hago la funcion del factorial
def factorialdenumeros(*args):
    for i in args:
        s.append(n)
    for i in args:
        f.append(factorial(i)) # Hago la funcion del factorial
    return s,f
print(factorialdenumeros(n)) # Se imprime