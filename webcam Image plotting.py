import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Arc

# code to get image coordinates from webcam 
'''
camera = cv2.VideoCapture(0)
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('test.jpg',image)
    break
    
camera.release()
cv2.destroyAllWindows()'''


img = mpimg.imread("enter file name here ")
print(img)
imgplot = plt.imshow(img)
plt.plot([65,65],[0,90], color="pink")
plt.show()

