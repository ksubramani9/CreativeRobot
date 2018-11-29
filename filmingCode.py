#Keertana Subramani GT ID: 903156496
#keertana@gatech.edu
#Christine Type, Jeremiah Dir and I, Keertana Subramani, worked on this assignment alone, using only this semester's course materials

from Myro import *
init ('com4')


def takepic() :
    alist=[]
    for j in range(30):
     name='picspiral'+str(j)+'.gif'
     p=takePicture()
     savePicture(p,name)
     alist.append(p)
    
    p=savePicture(alist,'piclistfinalspiral.gif')
    

takepic()
    
    
    

 