import cv2 as cv


image = cv.imread("voiture.jpg")
stepSize = 10
windowSize = [112,92]
for y in range(0, image.shape[0], stepSize):
    for x in range(0, image.shape[1], stepSize):
        # Show crops
        cv.imshow("crop",image[y:y + windowSize[1], x:x + windowSize[0]])
        cv.waitKey(0)
        cv.destroyAllWindows()
