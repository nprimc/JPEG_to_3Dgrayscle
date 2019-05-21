from PIL import Image
import pathlib


import numpy as np

def deli (l, n):
    for i in range (0, len(l), n):
        yield l[i:i+n]

image_folder = pathlib.Path ('C:\\Users\\np9659\\Desktop\\Image_folder') #path to the folder containing the images
image_name = input("Image name: ")
open_image = image_folder / image_name 


image = Image.open (open_image, 'r')
width, height = image.size

print ("Image size: %d x %d" % (width, height))

resize_factor = input("Resizing factor (decrease time): ")

#resizing the image
newWidth = int(width /int(resize_factor))
newHeight = int(height/int(resize_factor))

#print (width, height)

resizedImage = image.resize((newHeight, newWidth))
print (resizedImage)


pixel_values = list(resizedImage.getdata())


greyScale_values = [(0.33*x[0]+0.33*x[1]+0.33*x[2])/256 for x in pixel_values]



matrices = input("Name of the .txt file: ")



textfile = image_folder / matrike
x = np.arange(0,newWidth, 1)
y = np.arange(0, newHeight, 1)
z = list(deli(greyScale_values, newHeight))

i = 0

with open(textfile, 'w') as f:
    f.write("Z = [")
    for item in z:
        for zCoor in item:
            f.write("%s " % zCoor)
        i = i + 1
        if i<len(z):
            f.write("; \n")
    f.write("] \n")
    f.write("Y = [")
    for item in x:
        f.write ("%s " % item)
    f.write("] \n")
    f.write("X = [")
    for item in y:
        f.write ("%s " % item)
    f.write("] \n")
    f.write ("surf (X, Y, Z)")
        
