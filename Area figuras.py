#Programa para calcular areas
#Area cuadrado; lado x lado
print("sacar el area de un cuadrado")
lado=float(input("ingresa lado"))
areacuadrado=lado*lado
print("el area es", areacuadrado)
print(f"el area es{areacuadrado}")
#Area de un triangulo tipo deci,al
print("Sacar el area de un triangulo")
altura=float(input("ingresa altura"))
base=float(input("ingresa base"))
areaTriangulo=(base*altura)/2
print("el area es", areaTriangulo)
print(f"el area es{areaTriangulo}")
#Area de un trapecio
print("Sacar el area de un trapecio")
base_mayor=float(input("ingresa base_mayor"))
base_menor=float(input("ingresa base_menor"))
altura=float(input("ingresa altura"))
areaTrapecio=(base_mayor+base_menor*altura)/2
print("el area es", areaTrapecio)
print(f"el area es{areaTrapecio}")
#Area de un circulo
print("sacar el area de un circulo")
radio=float(input("ingrese el radio"))
pi=3.1416
area_circulo=radio*radio*pi
print("el area es", area_circulo)
print(f"el area es{area_circulo}")
#Area de pentagono
print("Sacar el area de un pentagono")
apotema=float(input("ingresa apotema"))
perimetro=float(input("perimetro"))
area_pentagono =(perimetro*apotema)/2
print("el area es", area_pentagono)
print(f"el area es{area_pentagono}")