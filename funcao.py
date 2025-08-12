lista_numeros = [40,5,60,70,0,-408593,1,50]

def ordernar_lista (numeros) -> list:
  nova_lista = numeros.copy()
  for i in range(len(nova_lista)):
    for j in range(i+1, len(nova_lista)):
      if nova_lista[i] > nova_lista[j]:
        nova_lista[i],nova_lista[j] = nova_lista[j], nova_lista[i]
      
  return nova_lista

numeros_ordenados = ordernar_lista(lista_numeros)
print(numeros_ordenados)