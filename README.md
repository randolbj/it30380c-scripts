# it30380c-scripts

###This is my read me changes 

#LAB 7 DETAILS BELOW
#first we get into virtual env by doing the following in the terminal...

C:\venv\webscraping\Scripts\activate.ps1


#Then once we are in webscraping we type:

pip install pillow

#Next we download an image and save it in my python folder
I downloaded an image from google that is a unviersity of cincinnati logo

# i then created a file from inside my python directory called lab7.py 
# in this file i typed

from PIL import Image,ImageFilter
myImage = Image.open('C:\it30380c-scripts\Python\index.png') # i placed my file right inside my python directory and its called index.png
myImage.load

myImage.show()

#The above code is the first thing i did to my image with the pillow module i simply opened the image and confirmed this work. and it does :)

#the second taks im going to do with pillow is change my file type. im going to turn this png into a jpg with the below code
#due to the fact that you cannot open jpg with the windows photos app in my real code i changed the extension back to a png but i did confirm a new file with a .jpg extension was actually created. 
myImage.save('C:\it30380c-scripts\Python\index1.jpg')

#i confirmed the above task worked by looking back into my python folder and i found the new file called index1.jpg :)

#for my final trick of the night im going to rotate my png image with the below code:

myImage.rotate(90).save('C:\it30380c-scripts\Python\index_Rotated.png')

# i confirmed the above code worked by looking in my python folder and finding my index_rotated.png file and confirmed it was rotated.
