class Track:

	def __init__(self, tracklets)
		self.tracklets = tracklets


	import json
	def encode(self)
		return json.dumps(self.__dict__)

	def decode(self, str)
		trackDict = json.loads(str)
		trackletArr = []
		for i in trackDict:
			trackletArr.append(Tracklet(trackDict[i[‘x’]], trackDict[i[‘y’]], trackDict[i[‘frame’]], trackDict[i[‘timestamp’]], trackDict[i[‘angle’]])
		return  Track(trackletArr)


