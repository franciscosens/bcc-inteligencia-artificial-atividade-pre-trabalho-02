import matplotlib.pyplot as plt
import random
import time

class Ponto:
    def __init__(self, i, j, direcao):
        self.i = i
        self.j = j
        self.direcao = direcao


class Questao01:
    # Neste cas0o o robo começa na posição [1][1]

    def __init__(self):
        self.matriz_geradora = [
            Ponto(1, 1, self.POSICAO_DIREITA),   
            Ponto(1, 2, self.POSICAO_DIREITA),   
            Ponto(1, 3, self.POSICAO_DIREITA),   
            Ponto(1, 4, self.POSICAO_ABAIXO),   
            Ponto(2, 4, self.POSICAO_ABAIXO),   
            Ponto(3, 4, self.POSICAO_ABAIXO),   
            Ponto(4, 4, self.POSICAO_ESQUERDA),
            Ponto(4, 3, self.POSICAO_ACIMA),
            Ponto(3, 3, self.POSICAO_ACIMA),  
            Ponto(2, 3, self.POSICAO_ESQUERDA),
            Ponto(2, 2, self.POSICAO_ABAIXO),
            Ponto(3, 2, self.POSICAO_ABAIXO),
            Ponto(4, 2, self.POSICAO_ESQUERDA),
            Ponto(4, 1, self.POSICAO_ACIMA),
            Ponto(3, 1, self.POSICAO_ACIMA),
            Ponto(2, 1, self.POSICAO_ACIMA),
        ]
        self.current_line = 1
        self.current_col = 1
        self.quantidade_linhas = 0
        self.quantidade_colunas = 0
        self.matriz = []
        self.gerar_matriz()
        self.gerar_posicao_aspirador()
        self.exibir(self.matriz)

    POSICAO_ACIMA = 'acima'
    POSICAO_ABAIXO = 'abaixo'
    POSICAO_ESQUERDA = 'esquerda'
    POSICAO_DIREITA = 'direita'
    POSICAO_ASPIRAR = 'aspirar'
    STATUS_PAREDE_VERDE = 1
    STATUS_LIMPO_AZUL = 0
    STATUS_SUJO_AMARELO = 2

    def gerar_matriz(self):
        self.matriz = [
            [self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE,  self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE,    self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,     self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,     self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,     self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,     self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE,  self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE,    self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE]
        ]
        self.quantidade_linhas = len(self.matriz) - 2
        self.quantidade_colunas = len(self.matriz) - 2
        for i in range(1, self.quantidade_linhas):
            for j in range(1, self.quantidade_colunas):
                sujo = random.randint(0, 1)
                if(sujo):
                    self.matriz[i][j] = self.STATUS_SUJO_AMARELO
        self.matriz_mapeado = [[False for x in range(
            self.quantidade_colunas + 2)] for y in range(self.quantidade_linhas + 2)]

    def agenteReativoSimples(self, percepcao):
        if(percepcao == self.POSICAO_DIREITA):
            self.current_col = self.current_col + 1
        elif percepcao == self.POSICAO_ESQUERDA:
            self.current_col = self.current_col - 1
        elif percepcao == self.POSICAO_ACIMA:
            self.current_line = self.current_line - 1
        elif percepcao ==  self.POSICAO_ABAIXO:
            self.current_line = self.current_line + 1

    def gerar_posicao_aspirador(self):
        self.current_line = random.randint(1, 4)
        self.current_col = random.randint(1, 4)
        # Verificar se o aspirador não está em uma posição já utilizada
        if(self.matriz[self.current_line][self.current_col] == self.STATUS_SUJO_AMARELO):
            return self.gerar_posicao_aspirador()

    def voltar_ao_comeco(self):
        if(self.current_col > 1):
            self.current_col = self.current_col - 1
            return

        if(self.current_line > 1):
            self.current_line = self.current_line - 1

        if(self.current_col == 1 and self.current_line == 1):
            self.voltou_comeco = True

    def verificar_membro_mapeado(self, i, j):
        if(self.matriz_mapeado[i][j] == False):
            self.current_line = i
            self.current_col = j
            self.matriz_mapeado[self.current_line][self.current_col] = True
            return True
        return False

    def limpar(self):
        posicao = [self.matriz_geradora.index(n) for n in filter(lambda n: (n.i == self.current_line and n.j == self.current_col) or None, self.matriz_geradora)]
        if(len(posicao) == 1):
            ponto = self.matriz_geradora[posicao[0]]
            if(self.matriz[self.current_line][self.current_col] == self.STATUS_SUJO_AMARELO):
                self.matriz[self.current_line][self.current_col] = self.STATUS_LIMPO_AZUL
            self.agenteReativoSimples(ponto.direcao)

    def exibir(self, matriz):
        while 1 == 1:
            plt.imshow(matriz, 'gray')
            plt.show(block=False)
            plt.plot(self.current_col, self.current_line, '*r', 'LineWidth', 5)
            plt.pause(0.1)
            self.limpar()
            plt.clf()


if __name__ == "__main__":
    q = Questao01()
