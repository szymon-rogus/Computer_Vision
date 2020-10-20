import cv2


def turn_by_angle(image, name):
    new_image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(name, new_image)


def flip(image, name, dist=1):
    new_image = cv2.flip(image, dist)
    cv2.imwrite(name, new_image)


def blur(image, name, size=(20, 20)):
    new_image = cv2.blur(image, size)
    cv2.imwrite(name, new_image)


def blur_and_flip(image, name, dist=1, size=(30, 30)):
    image = cv2.flip(image, dist)
    new_image = cv2.blur(image, size)
    cv2.imwrite(name, new_image)


def main():
    im1 = cv2.imread("images/A.jpg", cv2.IMREAD_GRAYSCALE)
    im2 = cv2.imread("images/E.jpg", cv2.IMREAD_GRAYSCALE)
    im3 = cv2.imread("images/F.jpg", cv2.IMREAD_GRAYSCALE)

    m1 = cv2.matchShapes(im1, im1, cv2.CONTOURS_MATCH_I2, 0)
    m2 = cv2.matchShapes(im1, im2, cv2.CONTOURS_MATCH_I2, 0)
    m3 = cv2.matchShapes(im1, im3, cv2.CONTOURS_MATCH_I2, 0)

    turn_by_angle(im1, "A4.jpg")
    turn_by_angle(im2, "E4.jpg")
    turn_by_angle(im3, "F4.jpg")

    flip(im1, "A1.jpg", 0)
    flip(im2, "E1.jpg")
    flip(im3, "F1.jpg")

    blur_and_flip(im1, "A3.jpg", 0)
    blur_and_flip(im2, "E3.jpg")
    blur_and_flip(im3, "F3.jpg")

    print("Shape Distances Between \n-------------------------")

    print("A0.png and A0.png : {}".format(m1))
    print("A0.png and E0.png : {}".format(m2))
    print("A0.png and F4.png : {}".format(m3))


if __name__ == "__main__":
    main()
