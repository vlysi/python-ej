"""
Ingresar N notas, mostrarlos en una lista y calcular el producto de todos sus valores
"""

n = int(input("Ingrese la cantidad de notas: "))

lista = []
producto = 1

for i in range(n):
  nota=int(input("Ingrese la nota: "))
  lista.insert(i, nota)
  producto = producto * lista[i]

print(lista)
print("El producto de los valores ingresados es: ", producto)