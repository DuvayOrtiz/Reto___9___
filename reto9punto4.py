#punto 4
import time # Importo libreria
def fiboRecursivo(n):
  if n <=1:
    return 1
  else:
    return fiboRecursivo(n-1)+fiboRecursivo(n-2) # hago la funcion recursiva 
def fiboiterar(n):
    if n <= 1:  
        return n 
    else:
        a, b = 0, 1 
        for i in range(n-1): 
            a, b = b, a + b
        return b  #hago la funcion con iteracion

n = int(input("Ingrese el valor de n: ")) # pido el numero n 
#calcular tiempo de demora recursión
tiempito = time.time()
fibrecur = fiboRecursivo(n)
finTiempito = time.time()
timer1 = finTiempito - tiempito
print("El tiempo con recursión para n= " + str(n) + " fue de: " + str(timer1) + " segs.")
#calcular tiempo de demora iteración
tiempito2 = time.time()
fibrecur2 = fiboiterar(n)
finTiempito2  = time.time()
timer2 = finTiempito2  - fibrecur2
print("El tiempo con iteración de n= " + str(n) + " fue de: " + str(timer2) + " segs.")

if timer1 > timer2: #imprimo el mas rapido
    print("iteración es más rápido que con recursión.")
else:
    print("recursión es más rápido que con iteración.")