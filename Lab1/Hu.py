from math import copysign, log10

import cv2
import sys


def hu_calculation():
    showLogTransformedHuMoments = True

    for i in range(1, len(sys.argv)):

        filename = sys.argv[i]

        im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        _, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)
        moment = cv2.moments(im)

        huMoments = cv2.HuMoments(moment)

        print("{}: ".format(filename), end='')

        for j in range(0, 7):
            if showLogTransformedHuMoments:
                print("{:.5f}".format(-1 * copysign(1.0, huMoments[j]) * log10(abs(huMoments[j]))), end=' ')
            else:
                print("{:.5f}".format(huMoments[j]), end=' ')
        print()


if __name__ == "__main__":
    hu_calculation()
