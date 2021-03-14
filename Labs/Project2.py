import numpy as np
from PIL import ImageGrab #the "from pil" portion i found from Stendex youtube channel! i also already have pillow installed from last week.
import cv2
import time

def screen_record(): 
    last_time = time.time()
    while(True):
        printscreen =  np.array(ImageGrab.grab(bbox=(1050,400,1450,500))) #l,t,r,b                    #test Target Area for window
        print('loop took {} seconds'.format(time.time()-last_time)) # the loop took time i aquired from Stendex youtube channel.
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'): #the 0xFF == ord # i aquired from Stendex Youtube Channel.
            cv2.destroyAllWindows()
            break

screen_record()

                                                                                                    #actual target area