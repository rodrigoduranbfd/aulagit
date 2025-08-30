def mediaChuvas (lista):
    if (len(lista) > 0): 
        media = sum(lista)/len(lista) 
        return media
    else:
        return -1

def coletarDados ():
    lista = [] 
    entrada = input("Digite um número ou STOP para terminar: ") 
    while entrada.strip().upper() != "STOP": 
        lista.append(float(entrada)) 
        entrada = input("Digite um número ou STOP para terminar: ") 
    return lista   

def principal():
    valoresChuva = coletarDados()
    mediaChuva = mediaChuvas(valoresChuva)
    print(f"Média de chuvas no período: {mediaChuva}")