import matplotlib.pyplot as plt


# Neste caso o robo começa na posição [1][1]
currLine = 1
currCol = 1

POSICAO_ACIMA = 'acima'
POSICAO_ABAIXO = 'abaixo'
POSICAO_ESQUERDA ='esquerda'
POSICAO_DIREITA = 'direita'
POSICAO_ASPIRAR = 'aspirar'

def agenteReativoSimples(percepcao):
    pass

def exibir(matriz):
    plt.imshow(matriz, 'gray')
    plt.show(block=True)
    plt.plot(currCol, currLine, '*r', 'LineWidth', 5)
    plt.pause(0.5)
    plt.clf()

if __name__ == "__main__":
    matriz = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 2, 0, 2, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    exibir(matriz)