
class Tracklet:

    def __init__(self, frame, xPixel, yPixel, angle, id):
        self.id = id
        self.xPixel = xPixel
        self.yPixel = yPixel
        self.angle = angle
        self.frame = frame
