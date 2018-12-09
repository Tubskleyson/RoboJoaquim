from graphics import *
from time import *

def dist(a,b):

    return (sum([(a[i]-b[i])**2 for i in range(2)]))**.5

def soma(a,b):

    return [a[i] + b[i] for i in range(2)]

class Joaquim:

    def __init__(self,Win,lr,pos):


        self.x = pos.getX()
        self.y = pos.getY()

        self.pos = [self.x,self.y]

        self.obj = Rectangle(Point(self.x - lr / 2, self.y - lr / 2), Point(self.x + lr / 2, self.y + lr / 2))

        self.obj.draw(Win)
        self.obj.setFill("gray")

        self.coliders = []

        self.carga = 800


    def check(self):

        k = [[0,1],[1,0],[0,-1],[-1,0]]

        d = k[:]

        for i in self.coliders:

            x = i[0][0]
            y = i[0][1]

            l = i[1][0]/2
            h = i[1][1]/2

            for j in k:

                nx,ny = [self.pos[i]+j[i] for i in range(2)]



                cx = nx>x and nx-3<x+l or nx<x and nx+3>x-l or nx==x

                cy = ny<y and ny+3>y-h or ny>y and ny-3<y+h or ny==y


                if cx and cy:
                    if j in d: d.remove(j)

        return d






    def move(self,destin):

        if not destin:
            xd = 107
            yd = 3

        else:
            xd = destin.getX()
            yd = destin.getY()

        destino = (xd,yd)

        moves = [[0,0]]

        while dist(self.pos,destino)>10 and self.pos[0]!=xd or self.pos[1] != yd:

            direcoes_possiveis = self.check()

            to = []

            if self.pos[1]<yd: to += [[0,1]]
            elif self.pos[1]>yd: to += [[0,-1]]

            if self.pos[0]<xd: to += [[1,0]]
            elif self.pos[0]>xd: to += [[-1,0]]

            if not any(k in direcoes_possiveis for k in to) or any(soma(moves[-1],k)==[0,0] for k in to):

                nd = [i for i in direcoes_possiveis if not soma(moves[-1],i)==[0,0]]
                d = nd[0]

                self.pos = soma(self.pos,d)
                moves += [d]

                self.obj.move(*d)

                self.carga -= 1

            else:
                for i in to:

                    if i in direcoes_possiveis:

                        self.pos = soma(self.pos,i)
                        moves += [i]

                        self.obj.move(*i)

                        self.carga -= 1

                        break
            update(60)

        sleep(2)

        if not destin: self.carga = 800

        while moves != [[0,0]]:

            if self.carga <= 100: self.move(0)

            m = moves[-1]

            m[0] = -m[0]
            m[1] = -m[1]

            self.pos = soma(self.pos, m)

            self.obj.move(*m)

            self.carga -= 1

            moves = moves[:-1]

            update(60)