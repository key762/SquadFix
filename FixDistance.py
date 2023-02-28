import cv2
import os
from shutil import copyfile, rmtree


def checkDistance():
    for i in os.listdir('./img'):
        old_path = os.path.join('./img/' + i)
        num = getPix(old_path, 2, 1272)
        if num == 765:
            copyfile(old_path, getNewPath(i, 100))
            print(old_path + "------->  100m")
        else:
            num2 = getPix(old_path, 3, 1271)
            if num2 != 0:
                copyfile(old_path, getNewPath(i, 300))
                print(old_path + "------->  300m")
            else:
                num3 = getPix(old_path, 4, 1271)
                if num3 == 765:
                    copyfile(old_path, getNewPath(i, 300))
                    print(old_path + "------->  300m")
                else:
                    copyfile(old_path, getNewPath(i, 900))
                    print(old_path + "------->  900m")


def getNewPath(filename, distance):
    return os.path.join('./res/' + str(distance) + '/' + filename)


def getPix(img_path, y, x):
    img = cv2.imread(img_path)
    blue = int(img[y, x, 0])
    green = int(img[y, x, 1])
    red = int(img[y, x, 2])
    return blue + green + red


def cleanOldFile():
    rmtree('./res/100')
    rmtree('./res/300')
    rmtree('./res/900')
    os.mkdir('./res/100')
    os.mkdir('./res/300')
    os.mkdir('./res/900')


if __name__ == '__main__':
    cleanOldFile()
    checkDistance()
