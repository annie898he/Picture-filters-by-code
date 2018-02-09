######################################################################
# Author: Annie He
# Username: hea
# Date: 4/6/16
# Assignment: A15
# Purpose: To learn more about lists of lists and deep copies and also
# to enhance a larger module (ppm.py)
######################################################################
# Acknowledgements:
    # Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
    # working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter

# You need to acknowledge having modified this code and all other code you modify or use for assistance.
#   To do so, you will indicate something like:
#   Modified from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://cs.berea.edu/csc226/tasks/yourusername-L3-ppm.py and
#   http://cs.berea.edu/csc226/tasks/ppm.py
######################################################################

import time
from ppm import *
# Be sure you work with a single ppm object at a time

def main():
    # The following interaction is just for testing.  You will improve this.

    wn = PPM_set_up()  # To use the PPM class, this must appear at the beginning of your program: send to the initialzer.

    print("\nWelcome to the PPM introduction!\n")

    ppmdefault=PPM(wn) # uses default file
    ppmdefault.PPM_display()
    print("---")

    #allows the user to input a file and choose which way he/she would like to change it
    filename=raw_input("Please input name of PPM-P3 file: ")
    ppmobject=PPM(wn, filename)
    choice = raw_input("Here are your choices: \n 1 = make red \n 2 = greyscale \n 3 = flip horizontal \n 4 = rotate clockwise \n 5 = make purple \n 6 = flip vertically \n")
    if choice == str(1):
        ppmobject.PPM_make_red()
    elif choice == str(2):
        ppmobject.PPM_greyscale()
    elif choice == str(3):
        ppmobject.PPM_flip_horizontal()
    elif choice == str(4):
        ppmobject.PPM_rotateclockwise()
    elif choice == str(5):
        ppmobject.PPM_make_purple()
    elif choice == str(6):
        ppmobject.PPM_flip_vertical()
    
    ppmobject.PPM_display()

    print("---")

#    ppmtestlist=PPM(wn) # uses default file
#     #The following is a very small image list which differs from the default image
#    testlist=[[[0, 0, 255], [0, 255, 0], [0, 30, 30]],
#    [[40, 40, 40], [50, 50, 50],[60, 60, 60]]]
#    ppmtestlist.PPM_updatefrompixellist(testlist, "very_small.ppm")
#    ppmtestlist.PPM_display()

    print("\nPush the Quit button to exit all files.")

    PPM_render(wn) # needed to render all of the images you have instantiated

main()