from math import copysign, log10

import cv2
import sys
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = []


def hu_calculation():
    showLogTransformedHuMoments = True
    counter = 0

    for i in range(1, len(sys.argv)):

        filename = sys.argv[i]

        im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        _, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)
        moment = cv2.moments(im)

        huMoments = cv2.HuMoments(moment)

        print("{}: ".format(filename), end='')

        for j in range(0, 7):
            if showLogTransformedHuMoments:
                y.append(-1 * copysign(1.0, huMoments[j]) * log10(abs(huMoments[j])))
                print("{:.5f}".format(-1 * copysign(1.0, huMoments[j]) * log10(abs(huMoments[j]))), end=' ')
            else:
                print("{:.5f}".format(huMoments[j]), end=' ')
        print()
        plt.plot(x, y, label=filename[7:9])
        y.clear()
        counter += 1
        if counter % 6 == 0:
            plt.legend()
            plt.show()
            plt.clf()


if __name__ == "__main__":
    hu_calculation()
