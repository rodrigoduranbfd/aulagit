SENTINELA = -99999

def filtraDados (lista):
    return filter(lambda x: x >=0, lista)

def guardaZero (lista):
    return len(lista) > 0

def coletarDados ():
    lista = [] 
    entrada = input("Digite um número ou -99999 para terminar: ") 
    while entrada != SENTINELA: 
        lista.append(float(entrada)) 
        entrada = input("Digite um número ou -99999 para terminar: ") 
    return lista   

def mediaChuvas(lista): 
    if (guardaZero(lista)):
        return sum(lista)/len(lista)
    else :
        return -1

def principal():
    valoresChuva = coletarDados()
    filtrados = filtraDados(valoresChuva)
    mediaChuva = mediaChuvas(filtrados)
    print(f"Média de chuvas no período: {mediaChuva}")
