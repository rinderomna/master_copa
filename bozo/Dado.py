import Random as rd

class Dado() :
    def __init__(self, lado = 6) :
        self.lados = lado
        self.r = rd.Random()
        self.atual = 0
        self.rolar()


    def rolar(self) :
        self.atual = self.r.getIntRand(self.lados) + 1
        self.caminhoImagem = './bozo/diceImages/' + str(self.atual) + '.png'
        return self.atual