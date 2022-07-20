import Dado as dado
import time

class RolaDados :
    def __init__(self, n = 5) :
        self.dados = []
        for i in range(n) :
            self.dados.append(dado.Dado())
            time.sleep(0.5)
        
    
    def rolar(self, selecionados = None) :
        if selecionados == None:
            return
        selecionados = [int(i) for i in selecionados]
        selecionados = list(set(selecionados))

        for i in selecionados :
            try :
                self.dados[i] = dado.Dado()
                time.sleep(0.5)
            except ValueError :
                pass
    
    def getValoresDados(self) :
        valores = []
        for i in self.dados :
            valores.append(i.atual)
        
        return valores
    
