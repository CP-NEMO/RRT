################################################################
# The Purpose of The Following Program is to Create an Arena for Implementing the RRT Algorithm
#The following program uses the Matplotlib library to Plot the Output of the Arena. 
################################################################

import matplotlib.pyplot as plt


class ENV: 
  def __init__(self,x, y, xmin,ymin, xmax, ymax):
    self.x = x
    self.y = y
    self.xmin = xmin
    self.ymin = ymin
    self.xmax = xmax 
    self.ymax = ymax
    
    

# Obstacles Coordinates
ObsX = [ 40, 40, 20, 20, 30, 30, 50, 50] 
ObsY = [ 80, 60, 60, 90, 20, 50, 50, 20]



def plotting(E):
  
  # Plot the Arena
  plt.plot([0,0,100,100,0],[0,100,100,0,0],'k',lw=0.5)
  
  # draw obstacles
  num = int(len(E.x)/4)
  for i in range(1,num+1):
  	plt.plot([E.x[4*(i-1)],E.x[4*(i-1)+1],E.x[4*(i-1)+2],
  	E.x[4*(i-1)+3],E.x[4*(i-1)]],[E.y[4*(i-1)],E.y[4*(i-1)+1],
  	E.y[4*(i-1)+2],E.y[4*(i-1)+3],E.y[4*(i-1)]],'k',lw=2)
   
  plt.axes([0,100, 0, 100])
  plt.show()

  return 0

def main():
  E = ENV(ObsX, ObsY, 0, 100, 0, 100)  
  plotting(E)
  return 0    
    
if __name__ == "__main__": 
  main()