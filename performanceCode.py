#Keertana Subramani GT ID: 903156496
#keertana@gatech.edu
#Christine Type, Jeremiah Dir and I, Keertana Subramani, worked on this assignment alone, using only this semester's course materials


from Myro import *
from editingCode import *



## for frame in spiralMovie:
##     show(frame)
##     wait(.5)
    
for frame in spiralMovie:
    starMovie.append(frame)

for frame in starMovie:
    show(frame)
    wait(.5)

p = savePicture(starMovie,'finalmovie.gif')                        