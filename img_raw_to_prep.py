import numpy as np
import cv2
import os
import re
import time
import shutil

def is_write_done(filename):
    #checking if the file is still being written by cam app
    file_stat = os.stat(filename);
    prev_size = file_stat.st_size;
    time.sleep(.5)
    file_stat = os.stat(filename);
    size = file_stat.st_size;
    return size == prev_size


LIB_DIR = 'libfiles/'
RAW_DIR = 'raw_img/'
PREP_DIR = 'prep_dir/'
OLD_DIR = 'old_img/'

#cascade face loading
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

regex_pattern = re.compile(".*\.JPG")
print ("Begin processing images")

while True:
    for FILENAME in os.listdir(RAW_DIR):
        print ("current file is " + FILENAME)
        
        if not regex_pattern.match(FILENAME):
            continue
        #wait until file is done
        while not is_write_done(RAW_DIR + FILENAME):
            print ("not done writing")
        
        #start analysis on file
        print("cropping " + FILENAME)
        raw_img = cv2.imread(RAW_DIR + FILENAME)
        gray = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            crop_img = raw_img[y: y+h, x : x+w]
            blur_img = cv2.GaussianBlur(crop_img, (5,5), 0)
            cv2.imwrite(PREP_DIR + FILENAME, blur_img )
        print ("finished analyzing " + FILENAME)
        shutil.move(RAW_DIR + FILENAME , OLD_DIR + FILENAME)
