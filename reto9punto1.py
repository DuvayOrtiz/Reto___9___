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
#2   
import math # Importo libreria
Pi=math.pi
if __name__ == "__main__":
    r1=float(input("ingresar radio de la esfera: "))
    r2=float(input("ingresar radio de la base del cono : "))
    h=float(input("ingresar altura del cono : ")) #pido las variables
areaSup = lambda r1,r2,h: (4*Pi*(r1**2))+((Pi*h*r2)+((r2**2)*Pi)) #Declaro la función con el lambda
print("el area supericial de la figura es  " + str(areaSup(r1, r2, h))) #imprimo la función
#3
if __name__ == "__main__":
  m1 = float(input("Ingrese masa de cuerpo 1:"))
  m2 = float(input("Ingrese masa cuerpon 2:"))
  r = float(input("Ingrese la distancia entre los cuerpos en metros:")) #pido las variables
  G: float = 6.67384e-11 
calcularFuerza = lambda m1, m2, G, r : G*m1*m2/(r**2) #Declaro la función con el lambda
fuerzaFinal = calcularFuerza(m1, m2, G, r )
print("la fuerza entre los cuerpos es  " + str(fuerzaFinal)) #imprimimos le resultado
