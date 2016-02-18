Explores protocol buffers by generating "tracklets" which are paths composed of random coordinates. These tracklets are encoded in a protocol buffer and then plotted on top of a video using opencv.

Required components are in requirements.txt file. Install with

sudo pip install -r requirements.txt

Opencv must be installed separately. Please consult the documentation for opencv.

Be sure to supply your own video to run.
Execute by running

python trackletOverlay.py [video file name] [output video file name]
