
#---------cut_every_frame--------------

""""import cv2
vidcap = cv2.VideoCapture('test.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1"""

#-------------cut_frame_every_second-------------

import cv2
import os

vidcap = cv2.VideoCapture('rtsp://dsoft:Dsoft@321@113.176.195.116:555/ch1/main/av_stream')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))
print(fps)
k = 627
os.chdir('D:\Dsoft\Imagee')
while success:
    success,image = vidcap.read()
    print('read a new frame:',success)
    if count%(0.001*fps) == 0 :
         if cv2.imwrite('C2_%d.jpg'%k,image):
             k += 1

         print('successfully written 10th frame')
    count+=1
    print (count)


#-----------------------------Draw Line ----------------------------------------------
""""import cv2
import numpy as np

cv2.namedWindow("preview")
vc = cv2.VideoCapture('rtsp://dsoft:Dsoft@321@113.176.195.116:555/ch1/main/av_stream')

#vc = cv2.VideoCapture('rtsp://dsoft:Dsoft@321@113.1760.195.116:554/ch1/main/av_stream')

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)


    height = np.size(frame, 0)
    width = np.size(frame, 1)
    print( height,width)

    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    else:
        cv2.line(img=frame, pt1=(350, 0), pt2=(width, height), color=(0, 255, 0), thickness=2, lineType=8, shift=0)

vc.release()
cv2.destroyWindow("preview")
#----------------------------------------------------------------------------------------------"""



