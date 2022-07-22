import PySimpleGUI as sg
from ParamBozo import ParamBozo as pr

class Placar :
    def __init__(self) :
        self.posicoes = [-1] * 10
        self.score = 0

    def getColunas(self) :
        posImprimir = []
        for i in range(10) :
            if(self.posicoes[i] != -1) :
                posImprimir.append(str(self.posicoes[i]))
            else :
                posImprimir.append('[' + str(i + 1) + ']')

        coluna1 = [[sg.Text(posImprimir[0])], [sg.Text(posImprimir[1])], [sg.Text(posImprimir[2])]]
        coluna2 = [[sg.Text(posImprimir[3])], [sg.Text(posImprimir[4])], [sg.Text(posImprimir[5])], [sg.Text(posImprimir[9])]]
        coluna3 = [[sg.Text(posImprimir[6])], [sg.Text(posImprimir[7])], [sg.Text(posImprimir[8])]]
        
        return [coluna1, coluna2, coluna3]
    
    def getDisponiveis(self) :
        disp = []
        for i in range(10) :
            if(self.posicoes[i] == -1) :
                disp.append(i + 1)

        return disp  

    def inserirPlacar(self, posicao, dados) :
        vetDados = dados.getValoresDados()

        pontos = 0
        if posicao >= 0 and posicao <= 5 :

            pontos = self.contaDados(posicao, vetDados) * (posicao + 1)
        elif posicao == 6 :
            if(self.checkFull(vetDados)) :
                pontos = 15
        elif posicao == 7 :
            if(self.checkSeq(vetDados)) :
                pontos = 20
        elif posicao == 8 :
            if(self.checkQuadra(vetDados)) :
                pontos = 30
        else :
            if(self.checkQuina(vetDados)) :
                pontos = 40

        self.score += pontos
        self.posicoes[posicao] = pontos

    def contaDados(self, posicao, dados) :
        count = 0
        for i in dados :
            if i == posicao + 1 :
                count += 1
        return count

    def checkFull(self, dados) :
        lista = sorted(dados)
        return (lista[0] == lista[1] and lista[1] == lista[2] and lista[3] == lista[4]) or (lista[0] == lista[1] and lista[2] == lista[3] and lista[3] == lista[4])


    def checkSeq(self, dados) :
        lista = sorted(dados)
        return (lista[0] + 1 == lista[1] and lista[1] + 1 == lista[2] and lista[2] + 1 == lista[3] and lista[3] + 1 == lista[4])


    def checkQuadra(self, dados) :
        lista = sorted(dados)
        return (lista[0] == lista[1] and lista[1] == lista[2] and lista[2] == lista[3]) or (lista[1] == lista[2] and lista[2] == lista[3] and lista[3] == lista[4])


    def checkQuina(self, dados) :
        lista = sorted(dados)
        return lista[0] == lista[4]




