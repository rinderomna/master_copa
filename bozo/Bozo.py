import PySimpleGUI as sg
import Placar
from RolaDados import *
from PIL import Image
from ParamBozo import ParamBozo as pr

sg.theme('DarkAmber')

class Bozo :
    def __init__(self) :
        self.lucro = 0
        self.mainWindow = False
        self.diceWindow = False
        self.addScoreWindow = False

        #dados = RolaDados()
        score = Placar.Placar()

        self.criarTelaPrincipal(score)

    def atualizarPlacar(self, score) :
        mostrarRodadas = 10 if self.qtdRodadas > 10 else self.qtdRodadas
        if(self.mainWindow != False) :
            self.mainWindow.close()
        colunas = score.getColunas()
        layout = [[sg.Text('Jogo de Bozó', font=pr.title_font)],
        [sg.Text('Quantidade de rodadas: '+ str(mostrarRodadas)+'/10')],
        [sg.Text('Placar: '+str(score.score))],
        [sg.Text('     '), sg.Column(colunas[0], element_justification='center'),
        sg.Column(colunas[1], element_justification='center'),
        sg.Column(colunas[2], element_justification='right')]]

        if(self.qtdRodadas <= 10) :
            layout.append([sg.Button("Rolar dados"), sg.Button('Encerrar e sair')])
        else :
            layout.append([sg.Button("Finalizar jogo")])

        self.mainWindow = sg.Window('Bozó', layout, font=pr.font)

    def atualizaTelaDados(self, dados, score) :
        layout = [
            [sg.Text("Quantidade de vezes roladas: " + str(self.qtdRoladas) + "/3")],
            [sg.Image(source=dados.dados[0].caminhoImagem),
             sg.Image(source=dados.dados[1].caminhoImagem),
             sg.Image(source=dados.dados[2].caminhoImagem),
             sg.Image(source=dados.dados[3].caminhoImagem),
             sg.Image(source=dados.dados[4].caminhoImagem),
            ]
            
        ]

        if(self.qtdRoladas < 3) :
            layout.append(
                [sg.Text(""),
                sg.Checkbox('Dado 1   ', key='0', default=False),
                sg.Checkbox('Dado 2   ', key='1', default=False),
                sg.Checkbox('Dado 3   ', key='2', default=False),
                sg.Checkbox('Dado 4   ', key='3', default=False),
                sg.Checkbox('Dado 5   ', key='4', default=False)         
                ]             
            )
            layout.append([sg.Button('Rolar dados')])
        else :
            posDisp = score.getDisponiveis()
            layout.append([
                [sg.Combo(posDisp, default_value=str(posDisp[0]), readonly=True, key='inserir'),
                sg.Button('Inserir no placar')],
                [sg.Text('Posições de 1 a 6: quantidade de dados com o número da posição')],
                [sg.Text('Posição 7: 3 de um mesmo tipo e 2 de um mesmo outro tipo')],
                [sg.Text('Posição 8: sequência')],
                [sg.Text('Posição 9: 4 de um mesmo tipo')],
                [sg.Text('Posição 10: 5 de um mesmo tipo')]]
            )

        if(self.diceWindow == False) :            
            self.diceWindow = sg.Window('Tela de dados', layout, font=pr.font, element_justification='c')
        else :
            self.diceWindow.close()
            self.diceWindow = sg.Window('Tela de dados', layout, font=pr.font, element_justification='c')

    def telaDados(self, score) :
        dados = RolaDados()
        self.qtdRoladas = -1
        while True :
            self.qtdRoladas += 1
            self.atualizaTelaDados(dados, score)
            event, values = self.diceWindow.read()
            #values é dict
            if(event == 'Rolar dados') :
                quais = []
                for i in values :
                    if(values[i] == True) :
                        quais.append((int(i)))
                dados.rolar(quais)
                continue
            elif(event == 'Inserir no placar'):
                posPlacar = int(values['inserir']) - 1
                score.inserirPlacar(posPlacar, dados)
                break
            
            if(event == sg.WIN_CLOSED or event == 'Exit') :
                break
        
        self.diceWindow.close()


    def criarTelaPrincipal(self, score) :
        self.qtdRodadas = 1
        self.qtdRoladas = 0

        while True :          
            self.atualizarPlacar(score)

            event, values = self.mainWindow.read()
            if(event == 'Rolar dados') :
                if(self.qtdRodadas <= 10) :
                    self.telaDados(score)
                    self.qtdRodadas += 1
                    self.qtdRoladas = 0
            elif(event == 'Finalizar jogo' or event == 'Encerrar e sair') :
                while True :
                    layout = [
                        [sg.Text('Fim de jogo! Placar final: ' + str(score.score))],
                        [sg.Button('Sair')]
                    ]
                    fimWindow = sg.Window('Fim', layout, font=pr.font, element_justification='c')
                    event, values = fimWindow.read()
                    if(event == sg.WIN_CLOSED or event == 'Exit' or event == 'Sair') :
                        self.lucro = score.score
                        fimWindow.close()
                        if(self.mainWindow) :
                            self.mainWindow.close()
                        return

            if(event == sg.WIN_CLOSED) :
                break

        


def main() :
    b = Bozo()
    print(b.lucro)


if __name__ == '__main__':
    main()