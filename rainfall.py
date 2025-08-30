entrada = input("Digite um número ou STOP para terminar: ") 
lista = [] 
while entrada.strip().upper() != "STOP": 
    lista.append(float(entrada)) 
    entrada = input("Digite um número ou STOP para terminar: ") 
    if (len(lista) > 0): 
        media = sum(lista)/len(lista) 
        print(media) 
    else: 
        print("Erro ao calcular a media")