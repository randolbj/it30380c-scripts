from PIL import Image,ImageFilter
myImage = Image.open('C:\it30380c-scripts\Python\index.png')
myImage.load


#below shows my downlaoded image
myImage.show()


## below im going to try and change the file type of an image. in this case from a png to a jpg. 

myImage.save('C:\it30380c-scripts\Python\index_NewType.png')


#below rotates my image then saves the output as index_Rotated.png
myImage.rotate(90).save('C:\it30380c-scripts\Python\index_Rotated.png')