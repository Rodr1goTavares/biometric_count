
from capture.hand_capture import HandCapture


def main():
    runHandCapture()
    pass

def runHandCapture():
    hand_capture = HandCapture()
    hand_capture.startCapture()
    pass

if __name__ == "__main__":
    main()
