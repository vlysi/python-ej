"""
Contar los divisores de un numero y mostrarlos en la pantalla
"""

numero = int(input("Ingrese el numero: "))
cont = 0
for i in range(1, numero + 1):
  if numero % i == 0:
    print(i)
    cont= cont +1
print("La cantidad de divisores de", numero, "es", cont)

