'''
Capture images from webcam and track the puck's position in relation to the
AprilTags.
'''
from collections import deque
# from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import camera
import apriltag

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
ap.add_argument("-p", "--puck", default="green",
	help ="color of the puck in use, 'green' or 'blue'")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points.

## Color range is found from range_detector_hsv.py
if args.get("puck") == "green":
	puckLower = (16, 83, 76)
	puckUpper = (82, 219, 204)
if args.get("puck") == "blue":
	puckLower = (74, 71, 0)
	puckUpper = (134, 255, 71)
pts = deque(maxlen=args["buffer"])


# set up apriltags
apriltag_options = apriltag.DetectorOptions(families="tag16h5")
detector = apriltag.Detector(apriltag_options)

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	vs = camera.Camera()
# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])

# allow the camera or video file to warm up
time.sleep(2.0)

#so apriltag doesn't run every time
counter = 0

# keep looping until we press q or video ends
while True:
	# grab the current frame
	frame = vs.get_frame()
	last_time = time.time()
	# handle the frame from VideoCapture or VideoStream
	frame = frame[1] if args.get("video", False) else frame # <-- see if this line works
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, puckLower, puckUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	if counter % 100 == 0:
		time_start = time.time()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		results = detector.detect(gray)
		time_end = time.time()
		# print(f"Apriltag detection in: {time_end - time_start}")

	for r in results:
		(ptA, ptB, ptC, ptD) = r.corners
		ptB = (int(ptB[0]), int(ptB[1]))
		ptC = (int(ptC[0]), int(ptC[1]))
		ptD = (int(ptD[0]), int(ptD[1]))
		ptA = (int(ptA[0]), int(ptA[1]))
		(cX, cY) = (int(r.center[0]), int(r.center[1]))
		cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

		cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
		cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
		cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
		cv2.line(frame, ptD, ptA, (0, 255, 0), 2)

	   #print(dir(r))
		tag_id = r.tag_id
		cv2.putText(frame, str(tag_id), (ptA[0], ptA[1] - 15),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


	# find contours in the mask and initialize the current
    # (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		# only proceed if the radius meets a minimum size
		print(last_time - time.time(), center)
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
	# update the points queue
	pts.appendleft(center)
	# print(pts)

	# loop over the set of tracked points
	for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue
		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
	counter += 1
# if we are not using a video file, stop the camera video stream
vs.release()
# close all windows
cv2.destroyAllWindows()
