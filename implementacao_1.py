from graphics import *
from time import *
from button import *
class Balcao:
    def __init__(self,Win,l,h,c):
        self.l=l
        self.h=h
        self.c=c
        x=c.getX()
        y=c.getY()
        self.Balcao=Rectangle(Point(x-l/2,y-h/2),Point(x+l/2,y+h/2))
        self.Balcao.draw(Win)
        self.Balcao.setFill('brown')
class Mesas:
    def __init__(self,win):        
        self.win=win
        self.mesas=[]
        self.sair=[]
    def desenhamesas(self):
        self.mesa=Button(self.win,Point(50,50),10,5,'1',"black")
        self.mesa.activate()
        self.mesas.append(self.mesa)
        self.sair=Button(self.win,Point(7, 93),10,10,'voltar','lightgrey')
        self.sair.activate()
    def pedidomesa(self,pt):
        for i in self.mesas:
            if i.clicked(pt):
                return i.getCenter()
class Robot:
    def __init__(self,Win,lr,cr):
        self.lr=lr
        self.cr=cr
        x=cr.getX()
        y=cr.getY()
        self.Robot=Rectangle(Point(x-lr/2,y-lr/2),Point(x+lr/2,y+lr/2))
        self.Robot.draw(Win)
        self.Robot.setFill('Grey')
    def retornacr(self):
        return self.cr.clone()
    def move(self,destino):
        xd=destino.getX()
        yd=destino.getY()-3
        xa=self.cr.getX()
        xb=self.cr.getY()
        a,b=1,1
        ma,mb=0,1
        while ((ma+mb)!=0):
            cr=self.Robot.getCenter()
            xz=cr.getX()
            yz=cr.getY()
            if (xz==xd) and (yz==7) and a==1:
                ma,mb=0,1
                a=2
            elif (yz>=yd-self.lr/2) and a==2:
                sleep(1)
                ma,mb=0,-1
                a=3
            elif (xz==xa) and (yz==xb) and a==3:
                ma,mb=0,0
            self.Robot.move(ma,mb)
            update(60)
def main_1():
    Win=GraphWin('Robo',600,600)
    Win.setCoords(0,0,100,100)
    bancada=Balcao(Win,20,5,Point (50,3))
    robo=Robot(Win,2.5,Point (50,7))
    mesa=Mesas(Win)
    mesa.desenhamesas()
    while True:
        pt=Win.getMouse()
        if mesa.pedidomesa(pt):
            robo.move(mesa.pedidomesa(pt))
        if mesa.sair.clicked(pt):
            break
    Win.getMouse()
    Win.close()