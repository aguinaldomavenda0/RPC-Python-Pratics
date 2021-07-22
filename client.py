import xmlrpc.client

ip = input("Digite o IP do servidor[127.0.0.1]: ")
porta = input("Digite a porta: [9090]")
if ip == "":
    ip = "127.0.0.1"
if porta == "":
    porta = "9090"
    
listaItems = []
servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(ip, porta))
response = 0

while response != -1:
    print('««««««««««««««««««««««««««CLIENTE»»»»»»»»»»»»»»»»»»»»»»»»»\n')
    print("  1 - > Adicionar número na lista")
    print("  2 - > Remover número na lista")
    print("  3 - > Ordenar a lista QuickSort - RPC")
    print("  4 - > Busca Binária na lista - RPC")
    print(" -1 - > Terminar \n")
    print(listaItems)
    print("\n")
    response = int(input('Opção: '))
    if response == 1:
        response = int(input('Digite o número -> ADD: '))

        listaItems.append(response)
    
    elif response == 2:
        response = int(input('Digite o número -> Remover: '))
        listaItems.remove(response)

    elif response == 3:
        novalista = servidor.organizar(listaItems)
        listaItems = novalista
    
    elif response == 4:
        response = int(input('Digite o número -> Procurar: '))
        resultado = servidor.binarySearch(listaItems,response)
        if resultado:
            print('--------------------------')
            print('- Número existe na lista -')
            print('--------------------------')
        else:
            print('------------------------------')
            print('- Número não existe na lista -')
            print('------------------------------')
        
