from gerenciadorDeMemoria import *
from Enderecos import *
class hack(object):
    gerenciadorDeMemoria = None
    def __init__(self,nomeProcesso):
        self.gerenciadorDeMemoria = gerenciadorDeMemoria(nomeProcesso)
        pass

    def injetarStatusContra3(self, status):
        self.gerenciadorDeMemoria.escreverByte(status_contra3, status.to_bytes(1, byteorder='little'))


    def vidaContra3(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(status_contra3)
        print(statusAgora)
        if (statusAgora != addvida_contra3):
            self.gerenciadorDeMemoria.escreverByte(status_contra3,addvida_contra3.to_bytes(1,byteorder='little'))
#escudo--------------------------------------------->
    def escudoContra3(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(escudo_contra3)
        print(statusAgora)
        if (statusAgora != valor_escudo):
            self.gerenciadorDeMemoria.escreverByte(escudo_contra3, valor_escudo.to_bytes(1, byteorder='little'))
#bombas------------------------------------------------->
    def bombaContra3(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(bomba_contra3)
        print(statusAgora)
        if (statusAgora != valor_bomba):
            self.gerenciadorDeMemoria.escreverByte(bomba_contra3, valor_bomba.to_bytes(1, byteorder='little'))
#arma 1 ------------------------------------------------->
    def arma1Poder1(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma1_contra3)
        print(statusAgora)
        if (statusAgora != poder1_contra3_1):
            self.gerenciadorDeMemoria.escreverByte(arma1_contra3, poder1_contra3_1.to_bytes(1, byteorder='little'))

    def arma1Poder2(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma1_contra3)
        print(statusAgora)
        if (statusAgora != poder1_contra3_2):
            self.gerenciadorDeMemoria.escreverByte(arma1_contra3, poder1_contra3_2.to_bytes(1, byteorder='little'))

    def arma1Poder3(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma1_contra3)
        print(statusAgora)
        if (statusAgora != poder1_contra3_3):
            self.gerenciadorDeMemoria.escreverByte(arma1_contra3, poder1_contra3_3.to_bytes(1, byteorder='little'))

    def arma1Poder4(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma1_contra3)
        print(statusAgora)
        if (statusAgora != poder1_contra3_4):
            self.gerenciadorDeMemoria.escreverByte(arma1_contra3, poder1_contra3_4.to_bytes(1, byteorder='little'))

    def arma1Poder5(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma1_contra3)
        print(statusAgora)
        if (statusAgora != poder1_contra3_5):
            self.gerenciadorDeMemoria.escreverByte(arma1_contra3, poder1_contra3_5.to_bytes(1, byteorder='little'))
#arma 2 --------------------------------------->>>>
    def arma2Poder1(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma2_contra3)
        print(statusAgora)
        if (statusAgora != poder2_contra3_1):
            self.gerenciadorDeMemoria.escreverByte(arma2_contra3, poder2_contra3_1.to_bytes(1, byteorder='little'))

    def arma2Poder2(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma2_contra3)
        print(statusAgora)
        if (statusAgora != poder2_contra3_2):
            self.gerenciadorDeMemoria.escreverByte(arma2_contra3, poder2_contra3_2.to_bytes(1, byteorder='little'))

    def arma2Poder3(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma2_contra3)
        print(statusAgora)
        if (statusAgora != poder2_contra3_3):
            self.gerenciadorDeMemoria.escreverByte(arma2_contra3, poder2_contra3_3.to_bytes(1, byteorder='little'))

    def arma2Poder4(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma2_contra3)
        print(statusAgora)
        if (statusAgora != poder2_contra3_4):
            self.gerenciadorDeMemoria.escreverByte(arma2_contra3, poder2_contra3_4.to_bytes(1, byteorder='little'))

    def arma2Poder5(self):
        statusAgora = self.gerenciadorDeMemoria.lerByte(arma2_contra3)
        print(statusAgora)
        if (statusAgora != poder2_contra3_5):
            self.gerenciadorDeMemoria.escreverByte(arma2_contra3, poder2_contra3_5.to_bytes(1, byteorder='little'))
