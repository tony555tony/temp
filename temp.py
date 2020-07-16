import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('iu.jpg')#,cv2.IMREAD_GRAYSCALE)

aa = img[100:150,100:150]
img[10:60,10:60] = aa
img[:,:,0]=0
img[:,:,1]=2

cv2.imwrite('iuuuuu.jpg',img)
print(img)
cv2.imshow('iuiuiuiu',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()