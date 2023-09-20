#Calcular la suma de los cuadrados de los n primeros mumeros naturales,
#teniendo en cuenta que los n numeros deben ser positivos.

n = int(input("Ingrese la cantidad de numeros naturales: "))
suma = 0

while n<=0:
  print("El numero debe ser positivo")
  n = int(input("Ingrese la cantidad de numeros naturales: "))

for i in range(1, n+1) :
  elevar_cuadrado = i*i
  suma = suma + elevar_cuadrado

print("La suma de los n numeros naturales es: ",suma)
