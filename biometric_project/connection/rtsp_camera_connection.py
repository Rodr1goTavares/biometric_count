import cv2

from biometric_project.connection.connection import Cv2Connection


class RTSPCameraConnection(Cv2Connection):
    
    def __init__(self, rtsp_url):
        self._rtsp_url = rtsp_url
        self._cv2_connection = None
        pass
    
    def open_and_get_cv2(self):
        self._cv2_connection = cv2.VideoCapture(self._rtsp_url)
        return self._cv2_connection
    
    def is_opened(self):
        return self._cv2_connection.isOpened()
    
    def close_cv2(self):
        self._cv2_connection.release()
        self._cv2_connection.destroyAllWindows()
        pass
        
    