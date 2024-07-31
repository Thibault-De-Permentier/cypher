from PIL import Image

def imageMerging(firstImagePath, secondeImagePath, outputFilePath):
    firstImage = Image.open(firstImagePath)
    secondeImage = Image.open(secondeImagePath)
    if(firstImage.size == secondeImage.size):
        x, y = firstImage.size
    else:
        print("you stupid")
    for i in range(x):
        for j in range(y): 
            firstImageTuple = firstImage.getpixel((i,j))
            secondeImageTuple = secondeImage.getpixel((i,j))
            R = int(getBinaryAsStringBytesFormat(firstImageTuple[0])[:4]+getBinaryAsStringBytesFormat(secondeImageTuple[0])[:4],2)
            G = int(getBinaryAsStringBytesFormat(firstImageTuple[1])[:4]+getBinaryAsStringBytesFormat(secondeImageTuple[1])[:4],2)
            B = int(getBinaryAsStringBytesFormat(firstImageTuple[2])[:4]+getBinaryAsStringBytesFormat(secondeImageTuple[2])[:4],2)
            firstImage.putpixel((i,j),(R,G,B))
    firstImage.save(outputFilePath)
    firstImage.close()
    secondeImage.close()

    
def getBinaryAsStringBytesFormat(element):
    binary = bin(element)[2:]
    if(len(binary)!=8):
        binary = binary.zfill(8)
    return binary


def swapMergedImages(inputFilePath, outputFilePath):
    image = Image.open(inputFilePath)
    x, y = image.size
    for i in range(x):
        for j in range(y): 
            imageTuple = image.getpixel((i,j))
            currentR = getBinaryAsStringBytesFormat(imageTuple[0])
            currentG = getBinaryAsStringBytesFormat(imageTuple[1])
            currentB = getBinaryAsStringBytesFormat(imageTuple[2])
            reverseR = int(currentR[4:]+currentR[:4],2)
            reverseG = int(currentG[4:]+currentG[:4],2)
            reverseB = int(currentB[4:]+currentB[:4],2)
            image.putpixel((i,j),(reverseR,reverseG,reverseB))
    image.save(outputFilePath)
    image.close()
