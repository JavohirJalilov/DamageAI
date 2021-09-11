import numpy as np
import cv2
import matplotlib.pyplot as plt
from image_inf import image_information
file_name = 'image_0000592'

img = cv2.imread(f"sample/images/{file_name}.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(image_information(file_name))
plt.imshow(img)
plt.show()
