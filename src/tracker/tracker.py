import cv2
import numpy as np
import sys


# Keep track of current bounding box and location.
# Help assign to new bounding box when available.
class Track:
    def __init__(self, init_box):
        self.box = init_box
        self.pos = GetBBoxPos(self.box)
        self.pos_arr = [self.pos]

    def UpdatePosition(self, bbox):
        self.box = bbox
        self.pos = GetBBoxPos(self.box)
        self.pos_arr.append(self.pos)

    # Finds the closest box in the array and removes it from the array.
    # Array doesn't need to be returned, because they are mutable.
    def FindClosest(self, bbox_arr):
        min_i = 0
        min_dist = None
        for i in range(len(bbox_arr)):
            box = bbox_arr[i]
            box_pos = GetBBoxPos(box)
            dist = CalcDistance(self.pos, box_pos)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_i = i
        # Update box and position, then assign it to the track array.
        self.UpdatePosition(bbox_arr[min_i])
        # Delete box from array as it is now assigned to a track.
        del bbox_arr[min_i]


# Calculate euclidean distance between two points.
def CalcDistance(pos1, pos2):
    dx = (pos1[0] - pos2[0])**2
    dy = (pos1[1] - pos2[1])**2
    return int(np.sqrt(dx + dy))


# Get center coordinate of a bounding box.
def GetBBoxPos(bbox):
    x_arr = [coord[0] for coord in bbox]
    y_arr = [coord[1] for coord in bbox]
    min_x = min(x_arr)
    min_y = min(y_arr)
    max_x = max(x_arr)
    max_y = max(y_arr)
    y = int((max_y + min_y)/2)
    x = int((max_x + min_x)/2)
    return x, y


def ProcessFrame(frame):
    # inFrame = cv2.resize(inFrame, (0, 0), inFrame, imageScale, imageScale)
    blur = cv2.GaussianBlur(frame, (7, 7), 3)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY_INV, 31, 40) # + cv2.THRESH_OTSU)

    im, contours, heirarchy = cv2.findContours(binary, cv2.RETR_LIST,
                                               cv2.CHAIN_APPROX_NONE)
    # print(contours[1])
    outFrame = frame.copy()
    cv2.drawContours(outFrame, contours, -1, (255, 0, 0), -1)
    # cv2.namedWindow("Original vs Processed")
    tracks = []
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        box = np.int0(cv2.boxPoints(rect))
        # TODO(carden): Update code so that ProcessFrame will update tracks.
        tracks.append(Track(box))
        cv2.drawContours(outFrame, [box], 0, (0, 0, 255), 2)
    return outFrame, tracks


if __name__ == '__main__':
    show_image = False
    inVideoName = sys.argv[1]
    ##CODEC = cv2.CV_FOURCC('D', 'I', 'V', 'X') # MPEG-4 = MPEG-1A
    videoIn = cv2.VideoCapture(inVideoName)
    videoOut = None
    if not videoIn.isOpened():
        print("Error opening input video" + inVideoName)

    if len(sys.argv) > 2:
        outFileName = sys.argv[2]
        videoOut = cv2.VideoWriter(outFileName,
                               cv2.VideoWriter_fourcc('m', 'p', 'e', 'g'),
                               int(videoIn.get(cv2.CAP_PROP_FRAME_COUNT)),
                               (int(videoIn.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT))))
        if not videoOut.isOpened():
            print("Error opening output video" + outFileName)
    else:
        show_image = True

    while(videoIn.grab()):
        ret, inFrame = videoIn.retrieve()
        imageScale = .66
        outFrame, tracks = ProcessFrame(inFrame)
        if show_image:
            cv2.imshow('test', outFrame)
            key = cv2.waitKey(0)
            if key == 113:
                break
        # combinedImage = np.concatenate((inFrame, outFrame), axis=0)
        if videoOut is not None:
            videoOut.write(outFrame)

    if videoOut is not None:
        videoOut.release()
