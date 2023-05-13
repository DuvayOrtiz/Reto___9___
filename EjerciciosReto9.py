#Ejercicios
# 1
x = int(input("Ingrese el primer número entero: ")) 
y = int(input("Ingrese el segundo número entero: ")) #Pido las variables
mcd1 = lambda a, b: a if b == 0 else mcd1(b, a % b) #Hago la función con el proceso de residuos
mcd2 = mcd1(x, y) #Nombro la función 
print("El mcd " + str(x) + " y " + str(y) + " es " + str(mcd2)) #imprimo el resultado
#2
x = int(input("Ingrese valor de x: "))  #Pido la variable
suma = (lambda x : x / (x**(1/3)-1))(x) #Hago la función con la expresión dada
print("La funcion para cuando x vale " + str(x) + ", Y vale " + str(suma)) #imprimo el resultado
#3
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