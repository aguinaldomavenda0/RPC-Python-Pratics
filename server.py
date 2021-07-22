from xmlrpc.server import SimpleXMLRPCServer
import sys

ip = input("Digite o IP do servidor[127.0.0.1]: ")
porta = 0
porta_inicial = input("Digite a porta: [9090]")
if ip == "":
    ip = "127.0.0.1"
if porta_inicial == "":
    porta = 9090
    porta_inicial = "9090"
else:
    porta = int(porta_inicial)

def selectionSort(elementos):
    for  i in range(len(elementos)):
        min_idx = i
        for j in range(i+1, len(a)):
            if elementos[min_idx] > elementos[j]:
                min_idx = j
        elementos[i], elementos[min_idx] = elementos[min_idx], elementos[i]
    return elementos

def partition(arr, low, high):
    i = (low -1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
def organizar(lista):
    quickSort(lista, 0, len(lista)-1)
    return lista

def binarySearch(lista, elemento):
    quickSort(lista, 0, len(lista)-1)
    inicio = 0
    ultimo = len(lista) - 1
    encontrado = False

    while(inicio<=ultimo and not encontrado):

        pontomedio = (inicio + ultimo) // 2
        
        if lista[pontomedio] == elemento:
            encontrado = True
        else:
            if elemento < lista[pontomedio]:
                ultimo = pontomedio-1
            else:
                inicio = pontomedio + 1

    return encontrado
 
print('Escutando em: {0}:{1}'.format(ip,porta_inicial))
servidor = SimpleXMLRPCServer((ip, porta))
servidor.register_function(organizar, "organizar")
servidor.register_function(binarySearch, "binarySearch")
servidor.serve_forever()
