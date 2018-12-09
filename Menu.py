from graphics import *
from button import *
from implementacao_1 import *
from implementacao_2 import *

class Janela:
    def __init__ (self,win):
        self.win=win
        self.implementacaoum=Button(win,Point(50,87),50,12,'implementação 1','lightgrey')
        self.implementacaoum.activate()
        self.implementacaodois=Button(win,Point(50,62),50,12,'implementação 2','lightgrey')
        self.implementacaodois.activate()
        self.implementacaotres=Button(win,Point(50,37),50,12,'implementação 3','lightgrey')
        self.implementacaotres.activate()
        self.sair=Button(win,Point(50,12),50,12,'sair','lightgrey')
        self.sair.activate()
    def resposta(self):
        while True:
            pt=self.win.getMouse()
            if self.implementacaoum.clicked(pt):
                main_1()
            if self.implementacaodois.clicked(pt):
                main_2()
            if self.implementacaotres.clicked(pt):
                return 'implementação 3'
            if self.sair.clicked(pt):
                return 'sair'
    def close(self):
        self.win.close()
def main():
    win=GraphWin('Implementação',400,600)
    win.setCoords(0,0,100,100)
    botao= Janela(win)
    botao.resposta()
    choice = botao.resposta()
    while True:
        choice = botao.resposta()        
        if choice =='sair':
            break
        if choice == 'implementação 1':
            main_1()
        if choice == 'implementação 2':
            main_2()
    botao.close()    
    win.close()
if __name__ == "__main__":  
    main()