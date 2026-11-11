#programa de apoyo famuliar
sexo=input("ingrese se sexo ")
edad=int(input("ingrese su edad"))
hijos=int(input("ingresse su cantidad de hijos"))
if sexo=="hombre":
    estado_civil=input("ingres su estad civil")
if sexo== "mujer" and hijos==1 and edad<18:
    print("eres mujer y eres mayor de edad")
elif sexo=="mujer" and hijos==1 and edad>18:
    print("eres mujer tienes un hijo y eres mayor de edad el apoyo sera de 300")
elif sexo=="mujer" and hijos>1 and edad<18:
    print("eres mujer tienes mas de un hijo y eres menor de edad entonces el apoyo es de 1500")
elif sexo=="mujer" and hijos>1 and edad>18:
    print("eres mujer tienes mas de un hijo y eres mayor de edad entonces el apoyo es de 500")
elif sexo=="hombre" and hijos>=1 and edad>18:
    print("eres hombre y tienes hijos el apoyo es 700")