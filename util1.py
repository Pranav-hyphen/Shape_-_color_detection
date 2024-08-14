import numpy as np
import cv2


def get_limits1(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        # print("1")
        lowerLimit = np.array([hue - 15, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        # print("2")
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 5, 255, 255], dtype=np.uint8)
    else:
        # print("3")
        lowerLimit = np.array([hue - 30, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 30, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
