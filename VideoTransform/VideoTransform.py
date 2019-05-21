import cv2
import numpy as np
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--video", help = "Path to input video file")
parser.add_argument("--image", help = "Path to input image file")
args = parser.parse_args()

cap = cv2.VideoCapture(args.video if args.video else 0)
ret, img = cap.read()
height, width, channels = img.shape

out = cv2.VideoWriter('output.avi',
	cv2.VideoWriter_fourcc('M','J','P','G'), 20, (width,height))

while(cap.isOpened()):
	ret, img = cap.read()

	if ret == True:
		img  = np.flip(img, axis=1)

		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

		lower_red = np.array([0,120,70])
		upper_red = np.array([10,255,255])
		mask1 = cv2.inRange(hsv,lower_red,upper_red)

		lower_red = np.array([170,120,70])
		upper_red = np.array([180,255,255])
		mask2 = cv2.inRange(hsv,lower_red,upper_red)

		mask1 = mask1+mask2

		mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
		mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
		mask2 = cv2.bitwise_not(mask1)

		test_img = cv2.imread(args.image, cv2.IMREAD_COLOR)
		background = cv2.resize(test_img, (width, height))
		background = np.flip(background,axis=1)

		res1 = cv2.bitwise_and(background,background,mask=mask1)
		res2 = cv2.bitwise_and(img,img,mask=mask2)

		final_output = cv2.addWeighted(res1,1,res2,1,0)
		out.write(final_output)

		cv2.imshow('Yay !!!',final_output)
		k = cv2.waitKey(10)
		if k == 27:
			break

	else:
		break

cap.release()
out.release()
 
cv2.destroyAllWindows() 
