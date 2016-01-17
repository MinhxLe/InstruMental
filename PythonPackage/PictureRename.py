import os

class PictureRename:
    def renameFile(self, directory, prefix, ext):
        count = 0
        for i in os.listdir(directory):
            if i.endswith(ext.lower()):
                os.rename(directory+i, directory+prefix+str(count)+"." + ext)
                count += 1

if __name__ == '__main__':
    test = PictureRename()
    test.renameFile("../raw_img/", "happy", "JPG")
