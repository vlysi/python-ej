"""
Contar los votos de n personas y determinar el ganador de 2 equipos de futbol
"""


n = int(input("Cantidad de participantes: "))
print("Argentina --> opcion: 1")
print("Brasil --> opcion: 2")

cont = 0
contador = 0
for i in range (1, n+1):
  voto = int(input(f"Asistente numero {i} : "))
  while voto < 1 or voto > 2 :
    print("opcion no valida")
    voto= int(input(f"Asistente numero {i} : "))
  if voto == 1:
    cont = cont + 1
  if voto == 2:
    contador+=1

print("Votos para Argentina son", cont)
print("Votos para Brasil son", contador)


