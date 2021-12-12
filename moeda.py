from random import randint

class Moeda:
    def __init__(self):
        pass


    def girarmoeda(self, rodadas):
        self.rodadas = rodadas
        self.cara = 0
        self.coroa = 1
        self.qtdcara = self.qtdcoroa = 0

        for i in range(rodadas):
            self.resultado = randint(self.cara, self.coroa)
            if self.resultado == 0:
                self.qtdcara += 1
            elif self.resultado == 1:
                self.qtdcoroa += 1


    def estatistica(self):
        print(f'CARA: {self.qtdcara} vezes. Proporção {(self.qtdcara / self.rodadas) * 100:.2f}%')
        print(f'COROA {self.qtdcoroa} vezes. Proporção {(self.qtdcoroa / self.rodadas) * 100:.2f}%')


rodadas = int(input('Rodadas: '))

moeda = Moeda()
moeda.girarmoeda(rodadas)
moeda.estatistica()
