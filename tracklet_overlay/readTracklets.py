import trackletOverlay_pb2 as tOverlay


protobuf_fName = 'tracklets.protobuf'
overlay = tOverlay.Overlay()


if __name__ == '__main__':
    try:
        f = open(protobuf_fName, 'rb')
        overlay.ParseFromString(f.read())
        f.close()
    except:
        print "could not open file: " + protobuf_fName
    for tracklet in overlay.tracklets:
        print tracklet.name
        print len(tracklet.pixels)
