i = 0
soma_impares = 0
quantidade_pares = 0


def Par(matriz):
    for linha in matriz:
        for numero in linha:
            if numero % 2 == 0: 
                quantidade_pares = quantidade_pares + 1
    return quantidade_pares

def SomaImpar(matriz):
    for linha in matriz:
        for numero in linha:
            if numero % 2 != 0:
                soma_impares += numero
    return soma_impares

# Inicializar matriz 30x14 com números inteiros aleatórios
matriz = []
for i in range(30):
    linha = []
    for j in range(14):
        linha.append(contador)
        contador += 1
    matriz.append(linha)

# Exibir a matriz
for linha in matriz:
    print(linha)
matriz = [[random.randint(1, 100) for _ in range(14)] for _ in range(30)]

quantidade_pares = Par(matriz) #chamei a funcao par que eu fiz la em cima
soma_impares = SomaImpar(matriz) #chamei a funcao para somar os elementos impares

print(f"Quantidade de elementos pares: {quantidade_pares}")
print(f"Soma dos elementos ímpares: {soma_impares}")
