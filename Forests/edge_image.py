import argparse
import numpy as np
import cv2
import matplotlib.pyplot as plt
 
def kernal(x,y):
  k = np.ones((x,y),dtype=np.uint8)
  return k

filename = 'DeepCrack/test_img/11142-2.jpg'

parser = argparse.ArgumentParser()
# parser.add_argument('-i', '--input', help='path to the input image', 
#                     required=True)
# args = vars(parser.parse_args())

image = cv2.imread(filename)
orig_image = image.copy()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.astype(np.float32) / 255.0

gray = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# carry out Canny edge detection
canny = cv2.Canny(blurred, 50, 200)
# initialize the structured edge detector with the model
edge_detector = cv2.ximgproc.createStructuredEdgeDetection('model.yml/model.yml')
# detect the edges
edges = edge_detector.detectEdges(image)
# edges = cv2.cvtColor(edges,cv2.COLOR_GRAY2RGB)
# add_img = np.hstack((orig_image[:,:,1],canny,edges)) 
# cv2.imwrite('result.jpg',edges)
plt.imshow(edges,cmap='gray')
plt.show()