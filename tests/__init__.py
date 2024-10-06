import test

from biometric_project.models.hand_capture import HandCapture


def testMain():
    pass

def testHandCapture():
    webcam_connection = WebcamConnection()
    hand_capture = HandCapture(webcam_connection)
    hand_capture.start_capture()
    pass

if __name__ == "__main__":
    testHandCapture()
