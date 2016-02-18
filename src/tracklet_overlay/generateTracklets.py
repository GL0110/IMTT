import trackletOverlay_pb2 as tOverlay
from random import randint


protobuf_name = 'tracklets.protobuf'


def generatePixels(tracklet, a, b, numPixels):
    for i in range(0, numPixels):
        x = randint(a, b)
        y = randint(a, b)
        pixel = tracklet.pixels.add()
        pixel.x = x
        pixel.y = y

def generateTracklets(overlay, numTracklets, numPixels=10,
                      f=None, size=(0, 255)):
    for i in range(0, numTracklets):
        a = randint(0, min(size))
        b = randint(0, min(size))
        # make sure a <= b
        a, b = min(a, b), max(a, b)
        tracklet = overlay.tracklets.add()
        tracklet.name = "tracklet_" + str(i)
        tracklet = generatePixels(tracklet, a, b, numPixels)

    if f is not None:
        f.write(overlay.SerializeToString())
        f.close()


if __name__ == '__main__':
    f = open(protobuf_name, 'wb')

    # get random pixel arrays and assign them to tracklets
    overlay = tOverlay.Overlay()
    numTracklets = 10
    numPixels = 3
    generateTracklets(overlay, numTracklets, numPixels, f)



