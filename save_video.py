import cv2
import numpy as np
#Capture video from webcam
vid_capture = cv2.VideoCapture(0)
vidcap = cv2.VideoCapture('rtsp://dsoft:Dsoft@321@113.176.195.116:555/ch1/main/av_stream')
'''height = np.size(vidcap, 0)
width = np.size(vidcap, 1)
print(height, width)
print(vidcap.shape)'''

vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter("cam_video.mp4", vid_cod, 20.0, (640,480))
while(True):
     # Capture each frame of webcam video
     ret,frame = vid_capture.read()
     cv2.imshow("My cam video", frame)
     output.write(frame)
     # Close and break the loop after pressing "x" key
     if cv2.waitKey(1) &0XFF == ord('x'):
         break
# close the already opened camera
vid_capture.release()
# close the already opened file
output.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()