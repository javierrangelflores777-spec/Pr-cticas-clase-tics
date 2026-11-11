#programa que me indica si reprobe o no
#solicitar calif
calif1=float(input("ingresa la primera calificacion"))
calif2=float(input("ingresa la segunda calificacion"))
calif3=float(input("ingresa la tercera calificacion"))
calif4=float(input("ingresa la cuarta calificacion"))
califpromedio= (calif1+calif2+calif3+calif4)/4
if califpromedio >=6:
    print("pasaste")
else:
    print("reprobaste")
#hola
edad=(int(input("ingrsa tu edad")))
if edad>=18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

#temperatura
temp=float(input("ingresa la temperatura"))
if temp >=35.0:
    print("hace mucho calor")
else:
    print("no hace tanto calor")