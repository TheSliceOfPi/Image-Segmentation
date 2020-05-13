import cImage
import sys
import kmeans
import numpy as np

def getKMeans(FileImage,numK):
    newImg= cImage.EmptyImage(FileImage.getWidth(), FileImage.getHeight())
    pixMap=[]
    
    for x in range(FileImage.getWidth()):
        for y in range(FileImage.getHeight()):
            p=FileImage.getPixel(x,y)
            red=p.getRed()
            green=p.getGreen()
            blue=p.getBlue()
            pixMap.append([red,green,blue])
    np.array(pixMap)
    
        
    setData=kmeans.kmeans(numK,pixMap)
    iters=setData.kmeanstrain(pixMap)
    runFwd=setData.kmeansfwd(pixMap)
    i=0
    for x in range(FileImage.getWidth()):
        for y in range(FileImage.getHeight()):
            pos=int(runFwd[i])
            clust=iters[pos]
            pix=FileImage.getPixel(x,y)
            pix.setRed(int(clust[0]))
            pix.setGreen(int(clust[1]))
            pix.setBlue(int(clust[2]))
            newImg.setPixel(x,y,pix)
            i=i+1
        
        
    return newImg




def main():
    FileName=sys.argv[1]
    numK=int(sys.argv[2])
    FileImage=cImage.FileImage(FileName)
    newImg=getKMeans(FileImage,numK) #Run the parsing and KMean Alg
    #Places both images in the same window.
    myImageWin= cImage.ImageWin("Image Processing", 2*FileImage.getWidth(), FileImage.getHeight())
    
    FileImage.draw(myImageWin)
    newImg.setPosition(FileImage.getWidth(),0)
    newImg.draw(myImageWin)
    newImg.save("imgK.gif")
    myImageWin.exitOnClick()

main()
