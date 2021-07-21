################################################################
# The Purpose of The Following Program is to Create an Arena for Implementing the RRT Algorithm
#The following program uses the Matplotlib library to Plot the Output of the Arena. 
################################################################

import matplotlib.pyplot as plt
import random

class ENV: 
  def __init__(self,x, y, xmin,ymin, xmax, ymax):
    self.x = x
    self.y = y
    self.xmin = xmin
    self.ymin = ymin
    self.xmax = xmax 
    self.ymax = ymax
    

class RRT():
  
  def __init__(self,CNN):
    (x,y) = CNN   
    self.x = []
    self.x.append(x)
    self.y = []
    self.y.append(y)
    self.Parent = []
    self.Parent.append(0)
    
  def check_Euclidian(self,x,y):
    self.Xdis = x - self.Xrand
    self.Ydis = y - self.Yrand
    
    if(self.Xdis <0):
      self.Xdis = -1 * self.Xdis
    if(self.Ydis < 0): 
      self.Ydis = -1*self.Ydis
    
    if(self.Xdis>Step_size or self.Ydis > Step_size):
      return 0
    else: 
      return 1
  
  def bres(self, x1, y1, x2, y2):
    self.xa,self.ya = x1,y1
    self.dx = abs(x2 - x1)
    self.dy = abs(y2 - y1)
    self.gradient = self.dy/float(self.dx)
    
    if self.gradient >1:
      self.dx, self.dy = self.dy, self.dx
      self.xa,self.ya = self.ya, self.xa
      x1,y1 = y1,x1
      x2,y2 = y2,x2
      
    self.p = 2*self.dy-self.dx
    print("x = %s, y = %s" % (self.xa,self.ya))
    
    for k in range(int(self.dx)):
      if self.p > 0:
        self.ya = self.ya +1 if self.ya < y2 else self.ya
        self.p = self.p +2 * (self.dy - self.dx)
      else:
        self.p = self.p + 2 * self.dy 
      
      self.xa = self.xa+1 if self.xa < x2 else self.xa-1
      
      if (self.xa - x1 >= Step_size):
        break
    print("Xa = %s and Ya = %s",(self.xa,self.ya))
    return 0
  
  def last_node(self):
    return len(self.x)
  
  def Crt_New_cor(self):
    self.Xrand = random.uniform(E.xmin, E.xmax)
    self.Yrand = random.uniform(E.ymin, E.ymax)
    self.n = self.last_node()
    self.a = self.check_Euclidian(self.x[self.n-1],self.y[self.n-1])
    print("Xrand = %s and Yrand = %s", (self.Xrand,self.Yrand))
    if(self.a == 0):
      self.bres(self.x[self.n-1], self.y[self.n-1], self.Xrand, self.Yrand)
      self.add_node(self.n, self.xa, self.ya)
    else:
      self.add_node(self.n,self.Xrand, self.Yrand)
      return
    
  def add_node(self,n, xa, ya):
    self.x.insert(n, xa)
    self.y.insert(n, ya)

# Obstacles Coordinates
ObsX = [ 40, 40, 20, 20, 30, 30, 50, 50] 
ObsY = [ 80, 60, 60, 90, 20, 50, 50, 20]

Step_size = 5

Start_co = (10,10)

def plotting(E):
  
  # Plot the Arena
  plt.plot([0,0,100,100,0],[0,100,100,0,0],'k',lw=0.5)
  
  # draw obstacles
  num = int(len(E.x)/4)
  for i in range(1,num+1):
  	plt.plot([E.x[4*(i-1)],E.x[4*(i-1)+1],E.x[4*(i-1)+2],
  	E.x[4*(i-1)+3],E.x[4*(i-1)]],[E.y[4*(i-1)],E.y[4*(i-1)+1],
  	E.y[4*(i-1)+2],E.y[4*(i-1)+3],E.y[4*(i-1)]],'k',lw=2)
   
  plt.plot([S.x[0], S.x[1]], [S.y[0],S.y[1]], 'k', lw = 0.1)
  plt.axes([0,100, 0, 100])
  plt.show()

  return 0

E = ENV(ObsX, ObsY, 0, 100, 0, 100)  
S = RRT(Start_co)


def main():
  S.Crt_New_cor()
  plotting(E)
  return 0    
    
if __name__ == "__main__": 
  main()