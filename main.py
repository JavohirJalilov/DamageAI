import numpy as np
import cv2
import matplotlib.pyplot as plt
from image_inf import image_information
file_name = 'image_0000592'

img = cv2.imread(f"sample/images/{file_name}.jpg")
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

size,data_contours = image_information(file_name)

for i in data_contours:
	x_min,y_min,x_max,y_max,classes = i
	img = cv2.rectangle(img,(x_min,y_min),(x_max,y_max),(0,0,255),3)

cv2.imwrite('result.jpg',img)
plt.imshow(img)
plt.show()
