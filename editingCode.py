#Keertana Subramani GT ID: 903156496
#keertana@gatech.edu
#Christine Type, Jeremiah Dir and I, Keertana Subramani, worked on this assignment alone, using only this semester's course materials

from Myro import *

listStar1 = []
for n in range(29):
    filename = 'pic{}.gif'.format(n+1)
    frame = loadPicture(filename)
    listStar1.append(frame)
## for frame in listStar1:
##     show( frame )
##     wait(.1) 
print ( "Done with Star List 1" )
listStar2 = loadPictures('star2.gif')
print ( "Done with Star List 2" )
listSpiral1 = loadPictures('spiral1.gif')
print ( "Done with Spiral List 1" )
listSpiral2 = loadPictures('spiral2.gif')
print ( "Done with Spiral List 2" )
#init("sim")
#setName('Scribblr-kun')

def seeing_Red():
    pic = takePicture()
    for pixel in getPixels(pic):
        setRed(pixel,255)
    show(pic)

#seeing_Red()

def fadeSpiral():
    pic = spiralMovie[29]
    for pixel in getPixels(pic):
        r,g,b = getRGB(pixel)
        setRed(pixel, r - 100)
        setBlue(pixel, b - 100)
        setGreen(pixel, g - 100) 
    spiralMovie.append(pic)
    
def fadeStar():
    pic = starMovie[29]
    for pixel in getPixels(pic):
        r,g,b = getRGB(pixel)
        setRed(pixel, r - 100)
        setBlue(pixel, b - 100)
        setGreen(pixel, g -100) 
    starMovie.append(pic)
        
#fade()
starMovie = []
def splitScreenStar():
    
    num = len(listStar1)
    for n in range (num):     # Split Screening a Movie
        pic1 = listStar1[n]
        pic2 = listStar2[n]
        pic3 = listStar2[n]
        
        heightPic3 = getHeight(pic3)
        widthPic3 = getWidth(pic3)
        for pixel in getPixels(pic3):
            xValue = getX(pixel)
            yValue = getY(pixel)
            if xValue > heightPic3 / 2: 
                pixelPic1 = getPixel(pic1, xValue, yValue)
                r,g,b = getRGB(pixelPic1)
                setRed(pixel,r)
                setBlue(pixel,b)
                setGreen(pixel,g)
            else:
                pixelPic2 = getPixel(pic2, xValue, yValue)
                r,g,b = getRGB(pixelPic2)
                setRed(pixel,r)
                setBlue(pixel,b)
                setGreen(pixel,g)
        starMovie.append(pic3)
    global starMovie      
#splitScreen()

spiralMovie = []
def splitScreenSpiral():
    
    num = len(listSpiral1)
    for n in range (num):     # Split Screening a Movie
        pic1 = listSpiral1[n]
        pic2 = listSpiral2[n]
        pic3 = listSpiral2[n]
        
        heightPic3 = getHeight(pic3)
        widthPic3 = getWidth(pic3)
        for pixel in getPixels(pic3):
            xValue = getX(pixel)
            yValue = getY(pixel)
            if xValue > heightPic3 / 2: 
                pixelPic1 = getPixel(pic1, xValue, yValue)
                r,g,b = getRGB(pixelPic1)
                setRed(pixel,r)
                setBlue(pixel,b)
                setGreen(pixel,g)
            else:
                pixelPic2 = getPixel(pic2, xValue, yValue)
                r,g,b = getRGB(pixelPic2)
                setRed(pixel,r)
                setBlue(pixel,b)
                setGreen(pixel,g)
        spiralMovie.append(pic3)  
    global spiralMovie    
#splitScreen() 
 
 
   
def overlaySpiral():
    letters = makePicture('Letters.jpg')
    #show ( letters)
    #show (pic)
    for pixelL in getPixels(letters):
        x = getX(pixelL)
        y = getY(pixelL)
        pixel = getPixel(frame, x , y )
        r,g,b = getRGB(pixelL)
        setRed(pixel, r)
        setGreen(pixel, g)
        setBlue(pixel, b) 
    #show(pic)
    spiralMovie.append(pic)   
    
def overlayStar():
    letters = makePicture('Letters.jpg')

    for pixelL in getPixels(letters):
        x = getX(pixelL)
        y = getY(pixelL)
        pixel = getPixel(frame, x , y )
        r,g,b = getRGB(pixelL)
        setRed(pixel, r)
        setGreen(pixel, g)
        setBlue(pixel, b) 
    #show(pic)
    starMovie.append(pic)   
    #overlay()  



print ( "Starting Star" )
splitScreenStar()
print ( " done with star")
print ( " Starting spiral" ) 
splitScreenSpiral()
print ("done with spiral")

print ( len ( spiralMovie )  )
#for frame in spiralMovie:
#    if  spiralMovie.index(frame) > 25:
#        overlaySpiral()
    
fadeSpiral()     
print ( " Done with Spiral, starting Star")        

for num in range (25,30):
    pic = starMovie[num]
    letters = makePicture('Letters.jpg')
    for pixelL in getPixels(letters):
        x = getX(pixelL)
        y = getY(pixelL)
        pixel = getPixel(pic, x , y )
        r,g,b = getRGB(pixelL)
        setRed(pixel, r)
        setGreen(pixel, g)
        setBlue(pixel, b) 
    #show(pic)
    starMovie.append(pic)   


for num in range (25,31):
    pic = spiralMovie[num]
    letters = makePicture('Letters.jpg')
    for pixelL in getPixels(letters):
        x = getX(pixelL)
        y = getY(pixelL)
        pixel = getPixel(pic, x , y )
        r,g,b = getRGB(pixelL)
        setRed(pixel, r)
        setGreen(pixel, g)
        setBlue(pixel, b) 
    #show(pic)
    spiralMovie.append(pic)   




fadeStar()
#if starMovie.index(frame) > 25:
#        overlayStar()
print ( len (starMovie) ) 
print ( len (spiralMovie) )       

print ( "I'm done!" )      
       
        
         
          
           
            
             
               
## def multipleExposure():
##     pic1 = makePicture('pic1.jpg')
##     turnLeft(1,1)
##     pic2 = makePicture('pic2.jpg')
##     pic3 = takePicture()
##     
##     red1 = []
##     red2 = []
##     red3 = []
##     
##     green1 = []
##     green2 = []
##     green3 = []
##     
##     blue1 = []
##     blue2 = []
##     blue3 = []
##     
##     for pixel1 in getPixels(pic1):
##         r,g,b = getRGB(pixel1)
##         red1.append(r)
##         green1.append(g)
##         blue1.append(b)
##     for pixel2 in getPixels(pic2):
##         r,g,b = getRGB(pixel1)
##         red2.append(r)
##         green2.append(g)
##         blue2.append(b)
##     
##     for i in range(len(red1)+1):
##         red3V = (red1[i-1] + red2[i-1]) / 2    
##         blue3V = (blue1[i-1] + blue2[i-1]) / 2
##         green3V = (green1[i-1] + green2[i-1]) / 2
##         
##         red3.append(red3V)
##         green3.append(green3V)
##         blue3.append(blue3V)
##         
##     #print (min(len(red3),len(green3),len(blue3))) Test Case
##     num = 1
##     for pixel in getPixels(pic3):
##         r = red3[num]
##         g = green3[num]
##         b = blue3[num]
##         
##         setRed(pixel,red3[num])
##         setGreen(pixel,green3[num])
##         setBlue(pixel,blue3[num])
##         
##         num += 1                                
##     show(pic3)
## #multipleExposure() #Test Case
        