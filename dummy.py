import os
import cv2
#cwd = os.getcwd()
#print(cwd)
#os.chdir('/home/zestiot/Desktop/Zestiot/PROJECTS/SAIL/sail_v4_all_areas(1)/sail_v4_all_areas/annotations')
#cwd = os.getcwd()
#print(cwd)
#for i in os.getcwd():
    #print(i)


small_laddle=[]
from pathlib import Path
folder_path='/home/zestiot/Desktop/Zestiot/PROJECTS/SAIL/SAIL_Preprocess/Big_Laddle/'

path = Path('/home/zestiot/Desktop/Zestiot/PROJECTS/SAIL/sail_v4_all_areas(1)/sail_v4_all_areas/annotations')
images = "/home/zestiot/Desktop/Zestiot/PROJECTS/SAIL/sail_v4_all_areas(1)/sail_v4_all_areas/images/"
entries = path.glob("*.txt")
for entry in entries:
    name = entry.name
    f = open(entry)
    for line in f.readlines():
        if line.split()[0] == '7':
            x,y,w,h = list(map(float,line.split()))[1:]
            x1,y1,x2,y2 = int((x-w/2)*1280),int((y-h/2)*720),int((x+w/2)*1280),int((y+h/2)*720)
            image = cv2.imread(f"{images}{name[:-3]}png")
            print(image)
            # print(f"{images}{name[:-3]}jpg")
            cropped = image[y1:y2,x1:x2]
            #print(cropped)
            #cv2.imwrite(f"{folder_path}{name[:-3]}png",cropped)
            cv2.waitKey(0)




