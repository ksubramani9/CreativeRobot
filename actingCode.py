#Keertana Subramani
#keertana@gatech.edu
#I worked on this homework with Christine Tye and Jeremiah Dir and referred to this semester's course materials.
from Myro import *


def spiral():
    for x in range(3,30,3):
        x=(x/10)
        forward(1,x)
        turnBy(90,'deg')
    stop()

def star(n):
    for x in range(5):
        forward(1,n)
        turnBy(-72,'deg')
        forward(1,n)
        turnBy(144,'deg')
    stop() 
    
    
    
    