import cv2
import numpy as np
import sys


if __name__ == '__main__':
    inVideoName = sys.argv[1]
    outFileName = sys.argv[2]
    ##CODEC = cv2.CV_FOURCC('D', 'I', 'V', 'X') # MPEG-4 = MPEG-1A
    videoIn = cv2.VideoCapture(inVideoName)
    videoOut = cv2.VideoWriter(outFileName,
                               cv2.VideoWriter_fourcc('m', 'p', 'e', 'g'),
                               int(videoIn.get(cv2.CAP_PROP_FRAME_COUNT)),
                               (int(videoIn.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    if not videoIn.isOpened():
        print("Error opening input video" + inVideoName)
    if not videoOut.isOpened():
        print("Error opening output video" + outFileName)

    while(videoIn.grab()):
        ret, inFrame = videoIn.retrieve()
        imageScale = .66
        # inFrame = cv2.resize(inFrame, (0, 0), inFrame, imageScale, imageScale)
        blur = cv2.GaussianBlur(inFrame, (7, 7), 3)
        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        binary = cv2.adaptiveThreshold(gray, 255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY_INV, 31, 40)
                                       ## + cv2.THRESH_OTSU)

        im, contours, heirarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        # print(contours[1])
        outFrame = inFrame.copy()
        cv2.drawContours(outFrame, contours, -1, (255, 0, 0), -1)
        # cv2.namedWindow("Original vs Processed")
        for contour in contours:
            rect = cv2.minAreaRect(contour)
            box = np.int0(cv2.boxPoints(rect))
            cv2.drawContours(outFrame, [box], 0, (0, 0, 255), 2)
        # combinedImage = np.concatenate((inFrame, outFrame), axis=0)
        videoOut.write(outFrame)

    videoOut.release()
