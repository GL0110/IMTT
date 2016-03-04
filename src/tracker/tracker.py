import cv2
import numpy as np
import sys


def ProcessFrame(scene_img, time_index):
    # Perform background subtraction.

    # Update current tracks with ICP.
    for track in active_tracks:
        current_track_model_points = models
        data_points = track.UpdatePosition(data_points,
                                           current_track_model_points,
                                           MODEL_TO_DATA_THRESH,
                                           SEPARATION_TRESH,
                                           ICP_MATCH_DISTANCE_THRESH,
                                           ICP_MAX_ITER,
                                           ICP_TRANSFORMATION_EPSILON,
                                           ICP_EUCLIDEAN_DIST,
                                           icp_max_worst_score.value)

    # Add new tracks.
    # Data points associated with tracks were removed in previous update step.
    # Create new tracks for remaining points.
    # Each point gets assigned a track.
    for i in range(len(data_points) - 1 - (fewest_num_of_model_points * .01 \
                                           * MODEL_TO_DATA_THRESH)):
        current_track_model_points = models
        new_target_point = data_points[i]
        track = Track(time_index, new_target_point, num_of_tracks,
                      ICP_MATCH_DISTANCE_THRESH, SEPARATION_TRESH,
                      RESOLUTION_FRACTION_MULTIPLIER)
        data_points = track.UpdatePosition(data_points,
                                           current_track_model_points,
                                           MODEL_TO_DATA_THRESH,
                                           SEPARATION_TRESH,
                                           ICP_MATCH_DISTANCE_THRESH,
                                           ICP_MAX_ITER,
                                           ICP_TRANSFORMATION_EPSILON,
                                           ICP_EUCLIDEAN_DIST,
                                           icp_max_worst_score.value)
        if track.WasBirthed():
            active_tracks.append(track)
            num_of_tracks += 1

    for i in range(len(active_tracks)):
        if active_tracks[i].GetNumZombieFrames() > TRACK_DEATH_TRESH:
            active_tracks[i].end()
            inactive_tracks.append(active_tracks[i])
            # Remove current index from active_tracks in a way that doesn't
            # cause an issue with the loop.
        

    # Delete old tracks.
    # Iterate over tracks that were not updated this round and delete.
    # A track is not updated if the number of frame drops cross a treshold.


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

        im, contours, heirarchy = cv2.findContours(binary, cv2.RETR_LIST,
                                                   cv2.CHAIN_APPROX_NONE)
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
