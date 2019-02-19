import cv2
from common.videocapture import CAMERA
from preprocessor.wheelcontrollerpreprocessor import process
import numpy as np



kernel = np.ones((3, 3),np.uint8)
def camtest(applyPreprocessing=None):
  while True:
    ret, frame = CAMERA.read()
  
    #Grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Denoise
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    # frame = cv2.fastNlMeansDenoising(frame, None, 20, 20)
    
    
    #Binarize
    frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
              cv2.THRESH_BINARY,11,2)

    
    #Afterbinarization denoise
    # frame = cv2.erode(frame, kernel, iterations = 1)
    frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame', frame)
    cv2.waitKey(60)
