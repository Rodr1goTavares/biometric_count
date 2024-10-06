

from biometric_project.capture.hand_capture import HandCapture
from biometric_project.connection.webcam_connection import WebcamConnection


def main():
    runHandCapture()
    pass

def runHandCapture():
    webcam_connection = WebcamConnection()
    hand_capture = HandCapture(webcam_connection)
    hand_capture.start_capture()
    pass

if __name__ == "__main__":
    main()
