import cv2

# SIFT with adjusted parameters
sift = cv2.SIFT_create(nfeatures=100, contrastThreshold=0.04, edgeThreshold=10.0)  # Adjust parameters as needed

# Feature matching
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

img1 = cv2.imread("Images/Cat.jpg")
img2 = cv2.imread("Images/Cat.jpg")  # Provide a different image for matching

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

gauss1 = cv2.GaussianBlur(gray1, (7, 7), 2)
gauss2 = cv2.GaussianBlur(gray2, (7, 7), 2)

keypoints_1, descriptors_1 = sift.detectAndCompute(gauss1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(gauss2, None)

matches = bf.match(descriptors_1, descriptors_2)
matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(gauss1, keypoints_1, gauss2, keypoints_2, matches[:10], gauss2,
                       flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
cv2.imshow("sift", img3)
cv2.waitKey(0)
