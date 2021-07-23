# RRT

Rapidly-exploring random tree is an algorithm which is necessery for learning basic path planning just like A* and D* algorithm. 

This Repository Include the step by step procedure to implement the RRT algorithm

1. The main file is RRT.py
2. Other files include "Create_env.py", that is The attempt to create an environment for implementing the RRT algorithm and the "First_STOCHASTIC_Step.py" that is the creation of the first branch of the tree.



# RRT.py Running procedure

The RRT.py is the main file that contains all the information required to run and simulate the algorithm. 

For running that file you will be requiring the following files:

Python 3.6+ version
Matplotlib
pip3

After downloading the file and fulfilling the requirements you can just run the file in any code editor that supports Python and run the file. 

First, the file will ask you for the coordinates for the end goal.
Then it will ask you for the coordinates of the starting point.

### NOTE: 
         Make sure to give it the free zone coordinates and not the area’s coordinates inside obstacles.The Area of the arena is in between (0, 100) and (100, 0).

Obstacles coordinates are as follows:
X = [40,40,60,60,70,70,80,80,40,40,60,60]
Y = [52,100,100,52,40,60,60,40, 0,48,48, 0]

Respectively. 


