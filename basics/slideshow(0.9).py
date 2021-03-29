# Slideshow
from os import listdir
import cv2


class SlideShow:
    def __init__(self, src='f:/TE_PBL/resource'):
        self.src = src
        self.types = ['.jpg', '.png']
        self.images = []

    def load(self):
        self.images.clear()  # reset
        # fetch the contents of the directory
        content = listdir(self.src)
        # filter
        for x in content:
            for y in self.types:
                if x.lower().endswith(y):
                    self.images.append(self.src + '/' + x)
                    break

    def play(self):
        # create a named window
        cv2.namedWindow('SLIDESHOW')
        for x in self.images:
            # print(x)
            img = cv2.imread(x)  # load the image in memory
            # print(type(img))
            img = cv2.resize(img, (1280, 720))  # resize the image to std HD size
            cv2.imshow('SLIDESHOW', img)  # render
            if cv2.waitKey(1000) == 27:  # accept a keypress in next  1000 milli seconds
                break
        # destroy the window
        cv2.destroyWindow('SLIDESHOW')


def main():
    ss = SlideShow()
    ss.load()
    ss.play()


main()
