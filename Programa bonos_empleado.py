#PROGRAMA BONOS EMPLEADO
print("prograna para calcular el sueldo")
Nombre=(input("ingrese su nombre"))
Pago_hora=int(input("ingrese su sueldo por hora"))
Horas_trabajadas_dia=int(input("ingrese las horas trabajadas en el dia"))
sueldo_sin_bonos_mes=(Pago_hora*Horas_trabajadas_dia)*30 
sueldo_sin_bonos_semana=Pago_hora*Horas_trabajadas_dia*7
sueldo_sin_bonos_dia=Pago_hora*Horas_trabajadas_dia

print("que opcion elige")
bonos_bonos=(input("opcion 1 sueldo sin bomos opcion 2 sueldo con bonos"))
if bonos_bonos==1:
    print("que es lo que quiere saber")
    opcion=int(input("1 sueldo por dia 2 sueldo por semana 3 sueldo mensual"))
elif bonos_bonos==2:
    print("que es lo que quiere saber")
opcion=int(input("1 sueldo por dia 2 sueldo por semana 3 sueldo mensual los bonos solo se agregaran a lo mensual debido a falta de tiempo"))

if bonos_bonos==1:
    print("elegiste sueldo sin bonos")
elif  opcion==1:
    print("su sueldo por dia es")
    sueldo_sin_bonos_dia
elif opcion==2:
    print("su sueldo por semana es")
elif opcion==3:
    print("su sueldo por mes es", sueldo_sin_bonos_mes)

if bonos_bonos==2:
    print("elegiste sueldo con bonos")
elif opcion==1:
    print("su sueldo por dia es", sueldo_sin_bonos_dia)
elif opcion==2:
    print("su sueldo por semana es", sueldo_sin_bonos_semana)
elif opcion==3:
    print("su sueldo por mes es")

if sueldo_sin_bonos_semana>=100 and sueldo_sin_bonos_mes<=300:
    sueldo_sin_bonos_mes+500
elif sueldo_sin_bonos_mes>300 and sueldo_sin_bonos_mes<=1500:
    sueldo_sin_bonos_mes+1700
elif sueldo_sin_bonos_mes>1500 and sueldo_sin_bonos_mes<=3000:
    sueldo_sin_bonos_mes+3500
elif sueldo_sin_bonos_mes>3000 and sueldo_sin_bonos_mes<=8000:
    sueldo_sin_bonos_mes+8500
elif sueldo_sin_bonos_mes>8000:
    sueldo_sin_bonos_mes+10000
else:
    print("no valido")



