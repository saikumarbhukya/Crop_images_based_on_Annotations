import cv2
import os
from pathlib import Path
import uuid
import glob
path='/home/zestiot/Desktop/Zestiot/PROJECTS/SAIL/SAIL_Preprocess/Small_Laddle_ROI'
images=Path('/home/zestiot/Desktop/Zestiot/PROJECTS/SAIL/SAIL_Preprocess/Small_Laddle')
#frames = images.glob("*.png")
for img in glob.glob("/home/zestiot/Desktop/Zestiot/PROJECTS/SAIL/SAIL_Preprocess/Small_Laddle/*.png"):
    cv_img = cv2.imread(img)
    img_resize=cv2.resize(cv_img,(260,374))
    img1=cv2.rectangle(img_resize,(2,3),(124,132),(255,0,0),2)
    img2=cv2.rectangle(img1,(121,1),(256,133),(255,0,0),2)
    img3=cv2.rectangle(img2, (74,266), (180,360), (255, 0, 0), 2)
    imgname = os.path.join(str(path)+ '.'+'{}.png'.format(str(uuid.uuid1())))
    cv2.imwrite(imgname, img3)
    cv2.waitKey()





