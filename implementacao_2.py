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

        self.ls = [x-l/2,x+l/2,y-h/2,y+h/2]

        self.p1 = (x-l/2,y-h/2)
        self.p2 = (x+l/2,y+h/2)

        self.Balcao=Rectangle(Point(x-l/2,y-h/2),Point(x+l/2,y+h/2))
        self.Balcao.draw(Win)
        self.Balcao.setFill('brown')






class Robot:
    def __init__(self,Win,lr,cr,mesa):
        self.mesa = mesa
        self.lr=lr
        self.cr=cr
        x=cr.getX()
        y=cr.getY()
        self.Robot=Rectangle(Point(x-lr/2,y-lr/2),Point(x+lr/2,y+lr/2))
        self.Robot.draw(Win)
        self.Robot.setFill('Gray')

        self.carga = 800

    def segue(self,coords):

        self.Robot.move(*coords);



    def checkpoint(self):

        if self.carga<100: self.charge()

        l = []

        while 1:


            cr = self.Robot.getCenter()
            xz = cr.getX()
            yz = cr.getY()

            if yz == 30: break

            if xz<50: l += [[1,0]]

            else: l += [[0,1]]

            self.Robot.move(*l[-1])

            self.carga -= 1

            print(self.carga)



            update(60)
            self.luzinha.segue(l[-1])

        return l

    def charge(self):

        cr = self.Robot.getCenter()
        xz = cr.getX()
        yz = cr.getY()

        k = []

        self.luzinha.Robot.setFill('red')

        while  yz>30:

            k += [[0,-1]]
            yz -= 1

            self.Robot.move(*k[-1])
            update(60)
            self.luzinha.segue(k[-1])

        while xz<66:

            k += [[1, 0]]
            xz += 1

            self.Robot.move(*k[-1])
            update(60)
            self.luzinha.segue(k[-1])

        while yz>3:

            k += [[0, -1]]
            yz -= 1

            self.Robot.move(*k[-1])
            update(60)
            self.luzinha.segue(k[-1])

        while xz<97:

            k += [[1, 0]]
            xz += 1

            self.Robot.move(*k[-1])
            update(60)
            self.luzinha.segue(k[-1])






        sleep(4)
        self.carga = 800
        self.luzinha.Robot.setFill('green')

        while k:


            m = k[-1]

            m[0] = -m[0]
            m[1] = -m[1]

            self.Robot.move(*m)

            k = k[:-1]

            update(60)
            self.luzinha.segue(m)







    def move(self,destino):
        xd=destino.getX()
        yd=destino.getY()


        l = self.checkpoint()

        align_x = 0

        td = xd

        if xd == 50: td += 20

        while 1:

            if self.carga<100: self.charge()

            cr=self.Robot.getCenter()
            xz=cr.getX()
            yz=cr.getY()



            if not align_x:

                try: d = (td-xz)//abs(td-xz)
                except: d = 1

                if xz==34 or xz==66: align_x = 1
                else: l+=[[d,0]]


            if align_x:

                if yz>=yd: break
                else: l += [[0,1]]


            self.Robot.move(*l[-1])
            update(60)
            self.luzinha.segue(l[-1])

            self.carga -= 1

            print(self.carga)




        for i in range(6):

            if self.carga<100: self.charge()

            d = (xd - xz) // abs(xd - xz)
            l += [[d,0]]

            self.Robot.move(*l[-1])
            update(60)
            self.luzinha.segue(l[-1])
            self.carga -= 1

            print(self.carga)



        sleep(2)

        while l:

            if self.carga<100: self.charge()

            m = l[-1]

            m[0] = -m[0]
            m[1] = -m[1]

            self.Robot.move(*m)

            l = l[:-1]

            update(60)
            self.luzinha.segue(m)

            self.carga -= 1

            print(self.carga)














class Mesas:
    def __init__(self,win):        
        self.win=win
        self.mesas=[]
    def desenha_mesas(self):


        i = 0

        for j in range(18,83,32):
            for k in range(42,94,17):
                self.mesas += [Button(self.win,Point(j,k),10,10,str(i+1),'cyan')]
                self.mesas[-1].activate()
                i+=1


        self.sair=Button(self.win,Point(7, 93),10,10,'voltar','lightgrey')
        self.sair.activate()

    def pedido(self,pt):
       for i in self.mesas:
           if i.clicked(pt):
               return i.getCenter()
def main_2():
    Win=GraphWin('Robo',600,600)
    Win.setCoords(0,0,100,100)

    bancada=Balcao(Win,40,10,Point (21,11))
    mesa=Mesas(Win)

    docstation = Robot(Win, 6, Point(97, 3), bancada)
    docstation.Robot.setFill('green')

    robo = Robot(Win, 6, Point(18, 3),bancada)

    carga = Robot(Win, 1, Point(18, 3),bancada)
    carga.Robot.setFill('green')

    robo.luzinha = carga



    mesa.desenha_mesas()
    while True:
        pt=Win.getMouse()
        if mesa.pedido(pt):
            robo.move(mesa.pedido(pt))
            sleep(3)
            robo.move(mesa.pedido(pt))
        if mesa.sair.clicked(pt):
            break
    Win.getMouse()
    Win.close()