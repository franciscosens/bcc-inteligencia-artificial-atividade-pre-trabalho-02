import matplotlib.pyplot as plt


# Neste caso o robo começa na posição [1][1]
currLine = 1
currCol = 1

def exibir(matriz):
    plt.imshow(matriz, 'gray')
    plt.show(block=False)
    plt.plot(currCol, currLine, '*r', 'LineWidth', 5)
    plt.pause(100)
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