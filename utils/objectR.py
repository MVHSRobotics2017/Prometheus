import cv2
import numpy as np
MIN_MATCH_COUNT = 30 #needs to have at least 30 matches

FLANN_INDEX_KDTREE = 0
detector = cv2.SIFT() #Use SURF for faster detection but it is less accurate
flannParam = dict(algorithm=FLANN_INDEX_KDTREE,tree=5)
flann = cv2.FlannBasedMatcher(flannParam,{})

trainingImg = cv2.imread('C:\Users\magic killer\Desktop\python_projects\objectr\Trainingdata\hdbucketti.jpg', 0)
trainKP, trainDecs = detector.detectAndCompute(trainingImg, None)

cam=cv2.VideoCapture (0)
while True:
	ret, QeryImgBGR = cam.read()
	QueryImg = cv2.cvtColor(QeryImgRGB,cv2.COLOR_BGR2GRAY) #he image detected from the webcam is converted in grayscale for accuracy purposes
	queryKP, queryDesc = detector.detectAndCompute(QueryImg, None) #This line gets the keypoints on the image
	matches = flann.kmnMatch(queryDesc, trainDecs, k = 2) #finds matches between training image and dectected image
	
	goodMatch = []
	for m,n in matches:
		if (m.distance<0.75*n.distance):
			goodMatch.append(m)

			if(len(goodMatch)>MIN_MATCH_COUNT): #if the minimum amount is reached of good matches
				tp = [] #training keypoint
				qp = [] #query keypoint
				for m in goodMatch:
					tp.append(trainKP[m.trainIdx].pt) #gets the index of the keypoint
					qp.append(queryKP[m.queryIdx].pt)
				tp, qp = np.float32(tp, qp) #converts numpylist to numbpy float
