#condiciones 2
#programa que me indica como me fue
calif=float(input("dame tu calif"))
if calif==10:
    print("excelente")
elif calif==9:
    print("muy bien")
elif calif==8:
    print("bien")
elif calif==7:
    print("puedes mejorar")
elif calif==6:
    print("ay mijo")
elif calif<=6:
    print("chanclazo")
else:
    print("error ingrese una calificacion de 1-10")

print("saber si hay mucha temperatura")
temp=float(input("ingrese la temperatura"))
if temp>=40:
    print("HACE MUCHO CALOR")
elif temp==30:
    print("esta templadp")
elif temp==20:
    print("esta fresco")
elif temp<=10:("hace frio")
else:
    print("no valido")

print("saber si hay mucha temperatura")
temp=float(input("ingrese la temperatura"))
if temp>=40:
    print("HACE MUCHO CALOR")
elif temp>=30 and temp<40:
    print("esta templadp")
elif temp>=20 and temp<30:
    print("esta fresco")
elif temp<=10:("hace frio")
else:
    print("no valido")

#solicitar sexo e edad para servicio militar
edad=int(input("ingrese su edad"))
print("escriba el numero que indique su sexo")
sexo=float(input("1.- maculino 2.- femenino"))
if sexo==1 and edad>=17:
    print("puedes calificar")
elif sexo==2 and edad>=17:
    print("no es posible por el genero")
elif sexo==1 and edad<=17:
    print("necesitas ser un adulto")
elif sexo==2 and edad<=17:
    print("no puedes calificar por el sexo y la edad")
