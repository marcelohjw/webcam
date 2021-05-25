import cv2

# This is how i can capture video from the webcam.
cap = cv2.VideoCapture(0)
print("Starting webcam capture...")

while True:
    success, img = cap.read()

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)