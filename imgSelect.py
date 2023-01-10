import glob
import cv2

import os
import sys
import shutil
import random

FORCE_WINDOW_HEIGHT=True
FORCE_WINDOW_WIDTH=True
RANDOM=True

DIRECTORY = "."
SIZE_H = 1500.0
SIZE_W = 1500.0

def isImage(filename):
    if(filename.endswith('.png') or
       filename.endswith('.jpeg') or
       filename.endswith('.jpg') or
       filename.endswith('.gif')):
        return True
    return False

def loadImage(filename):
    img = cv2.imread(file)
    if (img is None):
        return None
    h, w, c = img.shape
    if (h > SIZE_H or FORCE_WINDOW_HEIGHT):
        w = round(w*SIZE_H/h)
        h = round(SIZE_H)
    elif (w > SIZE_W or FORCE_WINDOW_WIDTH):
        h = round(h*SIZE_W/w)
        w = round(SIZE_W)
    print("open file: "+file)
    return cv2.resize(img, dsize=(w,h))

def checkDirectory(argv):
    if (len(argv) == 2):
        return argv[1]
    return DIRECTORY


#print(sys.argv)

directory = checkDirectory(sys.argv)
unstarDir = directory + 'unstar'

os.makedirs(unstarDir, exist_ok=True);

files = glob.glob(directory+"*")
files = [file for file in files if isImage(file)]

if (RANDOM):
    random.shuffle(files)

windowName = 'image'

print('files left:', len(files))
    
for file in files:
    if (not isImage(file)):
        break
    
    img = loadImage(file)
    if (img is None):
        print('can not read:',file)
        print('move to unstar directory :', file)
        shutil.move(file, unstarDir)
        continue
    
    cv2.imshow(windowName, img)
    while(True):
        key = cv2.waitKey(1)
        # ESC key pressed
        if (key == 27) :
            exit(0)
        elif (key != -1):
            # if key pressed "D"
            if (key == 100):
                print('move to unstar directory :', file)
                shutil.move(file, unstarDir)
            break
        # window closed
        if(cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1):
            exit(0)
        

