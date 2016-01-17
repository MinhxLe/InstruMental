from PythonPackage.VectorMachine import VectorMachine
from MusicScrape import MusicScraper
import os
import time
import shutil

''' Infinitely loops the prep_dir and finds if there's a picture. If there is, predict it using svm'''
class Engine:
    def __init__(self, preloaded = True, pickleName = "PythonPackage/svmResults.pkl"):
        self.vm = VectorMachine()
        if preloaded:
            self.svm = self.vm.readFromPickle(pickleName)
        else:
            self.svm = None
            print("Idk man you're fucked")

    def isWriteDone(self, filename):
        #checking if the file is still being written by cam app
        file_stat = os.stat(filename);
        prev_size = file_stat.st_size;
        time.sleep(.5)
        file_stat = os.stat(filename);
        size = file_stat.st_size;
        return size == prev_size

    def runEngine(self, fromdir="prep_dir/", todir="trash_dir/", ext=".JPG"):
        while True:
            for f in os.listdir(fromdir):
                if not f.endswith(ext) and not f.endswith(ext.lower()):
                    print("Files not correct format")
                    continue
                try:
                    while not self.isWriteDone(fromdir+f):
                        print ("not done writing")
                    #wait until file is done

                    print(self.svm.predict([self.vm.getCompressedRaveledPic(fromdir, os.path.splitext(f)[0], ext, "", "")]))
                    shutil.move(fromdir+f, todir+f)
                except OSError:
                    print("Possible file corrupted : " + str(f) + ". We will proceed to remove it.")
                    os.remove(fromdir+f)


if __name__ == '__main__':
    eng = Engine()
    eng.runEngine()