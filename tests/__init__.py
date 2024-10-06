import test

from biometric_project.models.hand_capture import HandCapture


def testMain():
    pass

def testHandCapture():
    hand_capture = HandCapture()
    hand_capture.startCapture()
    pass

if __name__ == "__main__":
    testHandCapture()