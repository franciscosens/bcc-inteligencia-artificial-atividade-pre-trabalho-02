import matplotlib.pyplot as plt
import random

class Questao01:
    # Neste cas0o o robo começa na posição [1][1]

    def __init__(self):
        self.current_line = 1
        self.current_col= 1
        self.matriz = []
        self.gerar_matriz()
        self.gerar_posicao_aspirador()
        self.exibir(self.matriz)
        

    POSICAO_ACIMA = 'acima'
    POSICAO_ABAIXO = 'abaixo'
    POSICAO_ESQUERDA ='esquerda'
    POSICAO_DIREITA = 'direita'
    POSICAO_ASPIRAR = 'aspirar'
    STATUS_PAREDE_VERDE = 1
    STATUS_LIMPO_AZUL = 0
    STATUS_SUJO_AMARELO = 2

    def gerar_matriz(self):
        self.matriz = [
            [self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE,  self.STATUS_PAREDE_VERDE,  self.STATUS_PAREDE_VERDE,    self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL ,   self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,    self.STATUS_LIMPO_AZUL,      self.STATUS_LIMPO_AZUL,     self.STATUS_PAREDE_VERDE],
            [self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE,  self.STATUS_PAREDE_VERDE,  self.STATUS_PAREDE_VERDE,    self.STATUS_PAREDE_VERDE,   self.STATUS_PAREDE_VERDE]
        ]
        quantidade_linhas = len(self.matriz) - 2
        quantidade_colunas = len(self.matriz) - 2
        for i in range(1, quantidade_linhas):
            for j in range(1, quantidade_colunas):
                sujo = random.randint(0, 1)
                if(sujo):
                    self.matriz[i][j] = self.STATUS_SUJO_AMARELO

    def agenteReativoSimples(self, percepcao):
        pass

    def gerar_posicao_aspirador(self):
        self.current_line = random.randint(1, 4)
        self.current_col = random.randint(1, 4)
        if(self.matriz[self.current_line][self.current_col] == self.STATUS_SUJO_AMARELO):
            return self.gerar_posicao_aspirador()
    
    def exibir(self, matriz):
        print(self.current_col)
        print(self.current_line)
        while 1 == 1:
            plt.imshow(matriz, 'gray')
                plt.show(block=False)
            plt.plot(self.current_col, self.current_line, '*r', 'LineWidth', 5)
            plt.pause(1)
            self.current_col = 1
            self.current_line = 1
            plt.clf()

if __name__ == "__main__":
    q = Questao01()