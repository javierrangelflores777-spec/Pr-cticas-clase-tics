#LISTAS
deportes=[]
dep=input("ingresa un deporte")
deportes.append(dep)
print(deportes)
dep2=input("ingresa otro deporte:")
print(deportes)
depborrar=input("cual quieres borrar")
deportes.remove(depborrar)
print(deportes)
dep3=input("dime otro deporte")
pos=int(input("en que posicion"))
deportes.insert(pos,dep3)
print(deportes)
#tarea de jupyter
palabra=input("escribe algo")
letra=input("ingresa una letra")
if letra in palabra:
    print("la letra si esta em la palabra")
else:
    print("la letra no esta en la palabra")

#ponerle nombre a mi lista
peliculas=[]
#oreguntar cuantas peliculas
cantidadpelis=int(input("cuantas peliculas vas a agregar"))
i=0
while i<=cantidadpelis:
    peli=input("ingresa peli:")
    print("peliculas")
    i=i+1