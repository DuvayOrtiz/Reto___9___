# Reto___9___
## Holaaaaaaaa :D
###Ejercicips
### *Ej1* :star:
```ruby
# 1
x = int(input("Ingrese el primer número entero: ")) 
y = int(input("Ingrese el segundo número entero: ")) #Pido las variables
mcd1 = lambda a, b: a if b == 0 else mcd1(b, a % b) #Hago la función con el proceso de residuos
mcd2 = mcd1(x, y) #Nombro la función 
print("El mcd " + str(x) + " y " + str(y) + " es " + str(mcd2)) #imprimo el resultado
```
### *Ej2* 🪃
```ruby
x = int(input("Ingrese valor de x: "))  #Pido la variable
suma = (lambda x : x / (x**(1/3)-1))(x) #Hago la función con la expresión dada
print("La funcion para cuando x vale " + str(x) + ", Y vale " + str(suma)) #imprimo el resultado
```
### *Ej3* :boom:
```ruby
def mym(a,b, menor=False): #defino la función con a y b
    if menor:
        return min(a,b)  #saco el menor
    elif a == b: #en caso de ser iguales se imprime que son la misma
        print("los numeros " + str(a) + " y " + str(b) + " son iguales")
    else:
        return min(a,b) 
a = float(input("Ingrese el número a: "))
b = float(input("Ingrese el número b: ")) # pido dos numeros
mayor = mym(a, b,)
menor = mym(a, b, menor=True) #aplico la función y la imprimo
print("El número mayor es:" + str(mayor) + "El número menor es", menor) 
```
## *Punto 1* :snowflake:
- De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.
```ruby
#punto 1
#1
import math # Importo libreria
Pi=math.pi # Guardo a pi
if __name__ == "__main__":
    r1=float(input("ingresar radio de la esfera: "))
    r2=float(input("ingresar radio de la base del cono : "))
    h=float(input("ingresar altura del cono : ")) #Pido las variables
volumen = lambda r1,r2,h: ((r1**3)*Pi*(4/3))+((r2**2)*Pi*h) #Declaro la función con el lambda
print("el volumen de la figura es " + str(volumen(r1,r2,h))) #Imprimo la función de los datos dados
```
```ruby
#2   
import math # Importo libreria
Pi=math.pi
if __name__ == "__main__":
    r1=float(input("ingresar radio de la esfera: "))
    r2=float(input("ingresar radio de la base del cono : "))
    h=float(input("ingresar altura del cono : ")) #pido las variables
areaSup = lambda r1,r2,h: (4*Pi*(r1**2))+((Pi*h*r2)+((r2**2)*Pi)) #Declaro la función con el lambda
print("el area supericial de la figura es  " + str(areaSup(r1, r2, h))) #imprimo la función
```
```ruby
#3
if __name__ == "__main__":
  m1 = float(input("Ingrese masa de cuerpo 1:"))
  m2 = float(input("Ingrese masa cuerpon 2:"))
  r = float(input("Ingrese la distancia entre los cuerpos en metros:")) #pido las variables
  G: float = 6.67384e-11 
calcularFuerza = lambda m1, m2, G, r : G*m1*m2/(r**2) #Declaro la función con el lambda
fuerzaFinal = calcularFuerza(m1, m2, G, r )
print("la fuerza entre los cuerpos es  " + str(fuerzaFinal)) #imprimimos le resultado
```


## *Punto 2* 🏁
- De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).
```ruby
#punto 2
#1
import math  # Importo libreria
def valorAbs(*args):     
    return math.fabs(x) # Hago la funcion con el args
if __name__ == "__main__":
    x=float(input("ingresar valor: ")) #pido una x
print("la distancia del punto al origen es  " + str(valorAbs(x))) #se imprime
```
```ruby
#2
def factorial(*args): # Hago la funcion con el args
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
n = int(input("Ingrese numero para factorial : ")) #pido una x
print(factorial(n))  #se imprime
```
```ruby
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
```

## *Punto 3* :wolf:
- Escriba una función recursiva para calcular la operación de la potencia.

```ruby
x=int(input("ingresar x: "))
n=int(input("ingresar n: ")) # Pido x y n
def pot(x,n): 
    if n==1:
        return x
    else:
        return x*pot(x,n-1) # Hago la funcion con recursión
print(pot(x,n)) # se imprime
```


## *Punto 4* :snail:
- Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.

```ruby
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
```
## *Punto 5* :leopard:
- Crear cuenta en stackoverflow y adjuntar imagen en el repo

![image](https://github.com/DuvayOrtiz/Reto___9___/assets/124726079/6f5d66b8-0cd8-4793-95ed-a7ae304b60a0)
## *Punto 6* :paw_prints:
- Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalon. Dejar enlace en el repo
https://www.linkedin.com/in/brayan-duvay-ortiz-martinez-580264276/

#### *Eso es todo por hoy :D* _-Duva-_
