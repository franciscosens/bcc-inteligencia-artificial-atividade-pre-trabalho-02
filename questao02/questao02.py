import matplotlib.pyplot as plt
import random
import time


class Posicao:
    def __init__(self, i, j):
        self.i = i
        self.j = j

class Questao02:

    def __init__(self):
        print("Iniciando ")
        self.mapeado = False
        self.limpou = False
        self.pontos = 0
        self.lugares_sujos = []
        self.current_line = 1
        self.current_col = 1
        self.quantidade_linhas = 0
        self.quantidade_colunas = 0
        self.matriz = []
        self.matriz_mapeado = []
        self.gerar_matriz()
        self.exibir(self.matriz)
        self.lugar_sujo

    POSICAO_ACIMA = 'acima'
    POSICAO_ABAIXO = 'abaixo'
    POSICAO_ESQUERDA = 'esquerda'
    POSICAO_DIREITA = 'direita'
    POSICAO_ASPIRAR = 'aspirar'
    STATUS_PAREDE_VERDE = 1
    STATUS_LIMPO_AZUL = 0
    STATUS_SUJO_AMARELO = 2
    NO_OP = 'NoOp'

    def gerar_matriz(self):
        # TODO: fazer através de um FOR
        self.matriz = [
            [self.STATUS_PAREDE_VERDE, self.STATUS_PAREDE_VERDE, self.STATUS_PAREDE_VERDE, self.STATUS_PAREDE_VERDE,
             self.STATUS_PAREDE_VERDE, self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE, self.STATUS_LIMPO_AZUL, self.STATUS_LIMPO_AZUL, self.STATUS_LIMPO_AZUL,
             self.STATUS_LIMPO_AZUL, self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE, self.STATUS_LIMPO_AZUL, self.STATUS_LIMPO_AZUL, self.STATUS_LIMPO_AZUL,
             self.STATUS_LIMPO_AZUL, self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE, self.STATUS_LIMPO_AZUL, self.STATUS_LIMPO_AZUL, self.STATUS_LIMPO_AZUL,
             self.STATUS_LIMPO_AZUL, self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE, self.STATUS_LIMPO_AZUL, self.STATUS_LIMPO_AZUL, self.STATUS_LIMPO_AZUL,
             self.STATUS_LIMPO_AZUL, self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE, self.STATUS_PAREDE_VERDE, self.STATUS_PAREDE_VERDE, self.STATUS_PAREDE_VERDE,
             self.STATUS_PAREDE_VERDE, self.STATUS_PAREDE_VERDE]
        ]
        self.quantidade_linhas = len(self.matriz) - 2
        self.quantidade_colunas = len(self.matriz) - 2
        for i in range(1, self.quantidade_linhas):
            for j in range(1, self.quantidade_colunas):
                sujo = random.randint(0, 1)
                if (sujo):
                    self.matriz[i][j] = self.STATUS_SUJO_AMARELO
        self.matriz_mapeado = [[False for x in range(
            self.quantidade_colunas + 2)] for y in range(self.quantidade_linhas + 2)]

    def agenteObjetivo(self, percepcao):
        pass

    def verificar_membro_mapeado(self, i, j):
        if (self.matriz_mapeado[i][j] == False):
            self.current_line = i
            self.current_col = j
            self.matriz_mapeado[self.current_line][self.current_col] = True
            return True
        return False

    def mapear(self):
        for i in range(1, len(self.matriz)-1):
            for j in range(1, len(self.matriz[i])-1):
                if (self.matriz[i][j] == self.STATUS_SUJO_AMARELO):
                    self.lugares_sujos.append(Posicao(i, j))
        self.mapeado = True

    def checkObj(self):
        if len(self.lugares_sujos) > 0:

            posicao = [self.lugares_sujos.index(n) for n in
                       filter(lambda n: (n.i == self.current_line and n.j == self.current_col) or None,
                              self.lugares_sujos)]

            if (len(posicao) == 1):
                self.lugar_sujo = self.lugares_sujos[posicao[0]]
                if self.lugar_sujo and self.current_line == self.lugar_sujo.i and self.current_col == self.lugar_sujo.j:
                    self.matriz[self.current_line][self.current_col] = self.STATUS_LIMPO_AZUL
                    self.lugares_sujos.remove(self.lugar_sujo)
                    print("Estado da percepcao: 1 Acao escolhida: "+self.POSICAO_ASPIRAR)
                    self.pontos += 1
                    return

            self.lugar_sujo = self.lugares_sujos[0]
            if self.current_line == self.lugar_sujo.i:
                if self.current_col < self.lugar_sujo.j:
                    self.current_col = self.current_col + 1
                    print("Estado da percepcao: 0 Acao escolhida: " + self.POSICAO_DIREITA)
                    self.pontos += 1
                else:
                    self.current_col = self.current_col - 1
                    print("Estado da percepcao: 0 Acao escolhida: " + self.POSICAO_ESQUERDA)
                    self.pontos += 1
            elif self.current_col == self.lugar_sujo.j:
                if self.current_line < self.lugar_sujo.i:
                    self.current_line = self.current_line + 1
                    print("Estado da percepcao: 0 Acao escolhida: " + self.POSICAO_ABAIXO)
                    self.pontos += 1
                else:
                    self.current_line = self.current_line - 1
                    print("Estado da percepcao: 0 Acao escolhida: " + self.POSICAO_ACIMA)
                    self.pontos += 1
            elif self.current_line < self.lugar_sujo.i:
                    self.current_line = self.current_line + 1
                    print("Estado da percepcao: 0 Acao escolhida: " + self.POSICAO_ABAIXO)
                    self.pontos += 1
        else:
            self.limpou = True
            print("Ponto:->" + str(self.pontos))
        pass

    def exibir(self, matriz):
        while 1 == 1:
            plt.imshow(matriz, 'gray')
            plt.show(block=False)
            plt.plot(self.current_col, self.current_line, '*r', 'LineWidth', 5)
            plt.pause(0.1)
            if not self.mapeado:
                self.mapear()
            elif not self.limpou:
                self.checkObj()
            else:
                time.sleep(1)
                print("Fim")
                plt.close()
                return self.__init__()
            plt.clf()

if __name__ == "__main__":
    q = Questao02()
