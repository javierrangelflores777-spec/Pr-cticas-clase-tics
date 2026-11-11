#lista y numeros y multiplicacion
numeros=[]
resultados=[]
i=0
while i < 5:
    num=int(input("ingresa un numero:"))
    numeros.append(num)
    multiplicador=int(input("¿por cuanto deseas multiplicar?"))
for num in numeros:
    resultado=num * multiplicador
    resultados.append(resultado)
print("numeros originales:",numeros)
print("resultados:",resultados)