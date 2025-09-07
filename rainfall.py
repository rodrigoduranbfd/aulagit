SENTINELA = -99999
MESSAGE = f"Digite um número ou {SENTINELA} para terminar: "


def somar (lista):
    soma = 0
    for valor in lista:
        soma = soma + valor
    return soma

def filtraDados (lista):
    return filter(lambda x: x >=0, lista)

def guardaZero (lista):
    return len(lista) > 0

def coletarDados ():
    lista = [] 
    entrada = input(MESSAGE) 
    while entrada != SENTINELA: 
        lista.append(float(entrada)) 
        entrada = input(MESSAGE) 
    return lista   

def mediaChuvas(lista): 
    if (guardaZero(lista)):
        return somar(lista)/len(lista)
    else :
        return -1

def principal():
    valoresChuva = coletarDados()
    filtrados = filtraDados(valoresChuva)
    mediaChuva = mediaChuvas(filtrados)
    print(f"Média de chuvas no período: {mediaChuva}")
