from model.wheelcontrollermodel import INPUT_HEIGHT, INPUT_WIDTH, INPUT_CHANNELS
import cv2
import numpy as np

def process(frame):
  # frame = (frame * 255).astype(np.uint8)
  # frame = cv2.GaussianBlur(frame, (5, 5), 0)
  # frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
  #           cv2.THRESH_BINARY,11,2)
  # frame = frame / 255.0
  
  # return frame.reshape(INPUT_WIDTH, INPUT_HEIGHT, INPUT_CHANNELS)
  return frame