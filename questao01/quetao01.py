import matplotlib.pyplot as plt
import random


class Posicao:
    def __init__(self, i, j):
        self.i = i
        self.j = j


class Questao01:
    # Neste cas0o o robo começa na posição [1][1]

    def __init__(self):
        self.voltou_comeco = False
        self.mapeado = False
        self.limpou = False
        self.lugares_sujos = []
        self.current_line = 1
        self.current_col = 1
        self.quantidade_linhas = 0
        self.quantidade_colunas = 0
        self.matriz = []
        self.matriz_mapeado = []
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
        # TODO: fazer através de um FOR
        self.matriz = [
            [self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE,  self.STATUS_PAREDE_VERDE,
                self.STATUS_PAREDE_VERDE,    self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,
                self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,
                self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,
                self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,
                self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE,  self.STATUS_PAREDE_VERDE,
                self.STATUS_PAREDE_VERDE,    self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE]
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
        print(self.matriz_mapeado)

    def agenteReativoSimples(self, percepcao):
        pass

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

    def mapear(self):
        if(self.matriz[self.current_line][self.current_col] == self.STATUS_SUJO_AMARELO):
            self.lugares_sujos.append(
                Posicao(self.current_line, self.current_col))

        if(self.current_col < self.quantidade_colunas and self.current_line < self.quantidade_linhas):
            if(self.matriz_mapeado[self.current_line][self.current_col + 1] == False):
                self.current_col = self.current_col + 1
                self.matriz_mapeado[self.current_line][self.current_col] = True
                return

        if(self.current_col > 1):
            if(self.matriz_mapeado[self.current_line][self.current_col - 1] == False):
                self.current_col = self.current_col - 1
                self.matriz_mapeado[self.current_line][self.current_col] = True
                return

        if (((self.current_col == self.quantidade_colunas) or (self.current_col == 1)) and self.current_line < self.quantidade_linhas):
            if(self.matriz_mapeado[self.current_line + 1][self.current_col] == False):
                self.current_line = self.current_line + 1
                self.matriz_mapeado[self.current_line][self.current_col] = True
                return
        self.mapeado = True

    def limpar(self):
        pass

    def exibir(self, matriz):
        while 1 == 1:
            plt.imshow(matriz, 'gray')
            plt.show(block=False)
            plt.plot(self.current_col, self.current_line, '*r', 'LineWidth', 5)
            plt.pause(0.2)
            if not self.voltou_comeco:
                self.voltar_ao_comeco()
            elif not self.mapeado:
                self.mapear()
            elif not self.limpou:
                for lugar_sujo in self.lugares_sujos:
                    print(str(lugar_sujo.i) + " "  + str(lugar_sujo.j))
                self.limpar()
                self.limpou = True
            plt.clf()



if __name__ == "__main__":
    q = Questao01()
