import cv2
import numpy as np
import pickle
from sklearn.externals import joblib
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem
from PIL import Image

class VectorMachine:
    def evaluate_cross_validation(self, clf, X, y, K):
        # create a k-fold cross validation iterator
        cv = KFold(len(y), K, shuffle=True, random_state=0)
        # by default the score used is the one returned by score method of the estimator (accuracy)
        scores = cross_val_score(clf, X, y, cv=cv)
        print (scores)
        print ("Mean score: {0:.3f} (+/-{1:.3f})".format(
            np.mean(scores), sem(scores)))

    def trainSVM(self, lam, imList, labels):
        '''
        :param lam: lambda parameter for svm training
        :param imList: np.ndarray of images
        :param labels: np.ndarray of answers to the images
        :return: SVM object
        '''
        y = labels
        clf = svm.SVC(C=1,kernel="linear")
        clf.fit(imList, y)
        return clf

    def readImages(self, endInd, emoDict, path="", basewidth=100, imgType=".jpg", startInd=0):
        '''
        :param path: "~/Desktop/Whatever/YourPathHere"
        :param imgType: type of image ".jpg" for example
        :param startInd: start index of the images
        :param endInd: end index of the images
        :param basewidth: size of the image (basewidth x basewidth)
        :param emoDict: Emo dict must be in format:
            {"happy" : 0, "sad" : 1, "angry" : 2}
        :return: np.array, np.array  {X, y}
        '''
        images = np.zeros((1,basewidth**2))
        y = []
        for i in range(startInd, endInd):
            for key, val in emoDict.items():
                try:
                    img = Image.open(path+key+str(i)+imgType.lower())
                    img = img.resize((basewidth, basewidth))
                    img.save(path+key+str(i)+"compressed"+imgType.lower())
                    pic = cv2.imread(path+key+str(i)+"compressed"+imgType.lower(), 0)

                    images = np.append(images, [pic.ravel()], axis=0)
                    y.append(val)
                except OSError:
                    print("Cannot read " + key+str(i)+".jpg")
                    pass
        images = np.array(images[1:])

        return images, y

    def saveAsPickle(self, svm, fileName):
        '''
        :param svm: the svm object created by sklearn
        :param fileName: fileName must be a string with .pkl as the extension
        '''
        return joblib.dump(svm, fileName)

    def readFromPickle(self, fileName):
        return joblib.load(fileName)

if __name__ == '__main__':
    already_created = False
    emoDict = {"happy" : 0, "sad" : 1, "angry" : 2}
    vm = VectorMachine()
    X,y = vm.readImages(90, emoDict, path="../prep_dir/")
    if not already_created:
        print(X.shape)
        svm = vm.trainSVM(1, X, y)
        vm.evaluate_cross_validation(svm,X,y,5) # partition into 5 groups and cross validate

        #Now we pickle and preserve
        print(vm.saveAsPickle(svm, "svmResults.pkl"))

    else:
        svm = vm.readFromPickle("svmResults.pkl")
        vm.evaluate_cross_validation(svm,X,y,5)

