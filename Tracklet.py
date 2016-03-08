class Tracklet:

	def __init__(self, x, y, frame, timestamp, angle):
		self.x = x
		self.y = y
		self.frame = frame
		self.timestamp = timestamp
		self.angle = angle

	import json
	def encode(self)
		return json.dumps(self.__dict__)

	def decode(self, str)
		obj = json.loads(str)
		return Tracklet(obj[‘x’], obj[‘y’], obj[‘frame’], obj[‘timestamp’], obj[‘angle’])
