import cv2

CAMERA = cv2.VideoCapture(0)

def releaseCameraAndDestroyWindows():
  cv2.destroyAllWindows()
  CAMERA.release()