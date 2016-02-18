import cv2
import cv
import numpy as np
import trackletOverlay_pb2 as tOverlay
from generateTracklets import generateTracklets
import sys


def generateOverlayFile(overlay, fname, size):
    f = open(fname, 'wb')
    numTracklets = 10
    numPixels = 10
    generateTracklets(overlay, numTracklets, numPixels, f, size)


def readOverlayFile(overlay, fname, size):
    try:
        f = open(fname, 'rb')
        overlay.ParseFromString(f.read())
        f.close()
    except:
        print "File {0} could not be opened. Generating a new one."\
                .format(fname)
        generateOverlayFile(overlay, fname, size)


def drawX(frame, x, y):
    size = 3
    topLeft = (x-size, y-size)
    topRight = (x+size, y-size)
    botLeft = (x-size, y+size)
    botRight = (x+size, y+size)
    cv2.line(frame, topLeft, botRight, color=(255, 0, 0))
    cv2.line(frame, topRight, botLeft, color=(255, 0, 0))


def drawPath(frame, tracklet):
    lastPixel = None
    for pixel in tracklet.pixels:
        drawX(frame, pixel.x, pixel.y)
        if lastPixel is None:
            lastPixel = pixel
        else:
            cv2.line(frame, (lastPixel.x, lastPixel.y),
                     (pixel.x, pixel.y), color=(255, 0, 0))
            lastPixel = pixel


if __name__ == '__main__':
    overlay = tOverlay.Overlay()
    protobuf_fname = 'tOverlay.protobuf'
    vid_fname = sys.argv[1]
    out_fname = sys.argv[2]
    CODEC = cv.CV_FOURCC('D','I','V','X') # MPEG-4 = MPEG-1
    size = (480, 360)

    readOverlayFile(overlay, protobuf_fname, size)

    # read in a video file and draw overlay
    if not vid_fname == '':
        cap = cv2.VideoCapture(vid_fname)
    else:
        print "please supply the input video file name at the commmand line."

    if not out_fname == '':
        writer = cv2.VideoWriter( out_fname,
                            CODEC,
                            30,
                            size,
                            True)
    else:
        print "please supply the output video file name at the command line."


    if not cap.isOpened():
        print "could not open video"
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            for tracklet in overlay.tracklets:
                drawPath(frame, tracklet)
            cv2.imshow('video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if writer is not None: writer.write(frame)
        else:
            print 'Video ended'
            break
    if cp.isOpened(): cap.release()
    if writer.isOpened(): writer.release()
    cv2.destroyAllWindows()

