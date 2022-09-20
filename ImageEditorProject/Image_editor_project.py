#image editor project
from re import L
from PIL import Image,ImageEnhance,ImageFilter
import os 

path="C:\\Users\\jeeva\\Downloads"                                         
pathOut="C:\\Users\\jeeva\\oneDrive\\Desktop\\Python\\Python Projects"     

for filename in os.listdir(path):
    img=Image.open("C:\\Users\\jeeva\\Downloads\\download.jpg")
    #for opening any image use .show() command
    
    #sharpens image
    edit=img.filter(ImageFilter.SHARPEN)

    #enhances contrast
    factor=1.0
    enhancer=ImageEnhance.Contrast(edit)
    edit=enhancer.enhance(factor)
    
    #brightness control
    factor=0.0                  #this gives a black image
    brightness=ImageEnhance.Brightness(edit)
    edit=brightness.enhance(factor)

    #rotates image
    edit=img.rotate(90)         #rotates image from landscape to potrait and vice-versa

    #changes image color
    edit=img.convert('L')

    #saving the edited file
    file_name=os.path.splitext(filename)[0]
    edit.save("C:\\Users\\jeeva\\oneDrive\\Desktop\\Python\\Python Projects\\_edited.jpg")               
    