# Programa que desenha o contorno de uma forma

altura = int(input("Digite a altura da sua forma: "))
largura = int(input("Digite a altura da sua forma: "))

escreve_linha = 1

while escreve_linha <= altura:
    print("*", end = "")
    coluna = 2
    while coluna < largura: 
        if escreve_linha == 1 or escreve_linha == altura:
            print("*", end = "")
        else:
            print(end = " ")
        coluna = coluna + 1
    print("*")
    escreve_linha = escreve_linha + 1