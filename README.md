# it30380c-scripts

###This is my read me changes for my PROJECT 2

#The end goal of this project is to have a python script that is constantly reading the users computer screen while they play call of duty and if the word "downed" appeas on the screen the script will be able to detect that (meaning a user got a kill in call of duty) and then do something based on that detection.
#The idea behind this project is actaully going to entail 4 steps for full sucessfully completion of this project.
#Step 1 is to generate a window that is constantly running while the user plays call of duty
#step 2 is going to somehow screen shot that windows like ever 0.1 seconds and save that screen shot as an image file in a directory.
#step 3 is going to then input those screenshots and run word detection against them to detect if the word "downed" is ever appeard on any of those image files. 
#step 4 is then going to turn a mortor in the user room if the word "downed" ever gets detected.
#for this project i just wanted to focus on step 1, and get the windows working, i had to focus manily on the size and positioning of the winodws becuase the word "downed" appear in the same loaction for all call of duty players.


#Simply run the code with the following command while in the "Labs" Directory (C:\it30380c-scripts\Labs)
#youll know its working correctly if the commented code "actual target area" is what appears in the window that gets generate. this would be the location of the word "downed" 
#that hardest part of this was zeroing in on that loaction of the users sceren.

python Project2.py
