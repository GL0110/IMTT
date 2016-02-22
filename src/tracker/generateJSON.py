import json

json_name = 'tracklets.json'

# assumes array of tracklet will be used
# TODO: potentially write directly to json rather than using array

def generateJSON(trackletArray):
    data = []
    for Tracklet in trackletArray:
        trackletData = {"frame": Tracklet.frame, "x": Tracklet.xPixel, "y": Tracklet.yPixel, "angle": Tracklet.angle, "id": Tracklet.id}
        data.append(trackletData)

    # writes json file
    with open(json_name, 'wb') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False, separators=(',', ': '))