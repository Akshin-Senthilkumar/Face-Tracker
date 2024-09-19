import cv2
import serial
import time

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier('/path/to/haarcascade_frontalface_default.xml')

# Initialize video capture
cap = cv2.VideoCapture(0)  # Try index 0 if 1 doesn't work

# Initialize serial communication
try:
    ArduinoSerial = serial.Serial('/dev/tty.usbmodemXXXX', 9600, timeout=0.1)  # Update with correct port
except serial.SerialException as e:
    print(f"Error: {e}")
    exit()

# Allow time for the Arduino to initialize
time.sleep(1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)  # Mirror the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)  # Detect faces

    for (x, y, w, h) in faces:
        # Sending coordinates to Arduino
        string = 'X{0:d}Y{1:d}'.format((x + w // 2), (y + h // 2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))

        # Draw the center of the face and the face rectangle
        cv2.circle(frame, (x + w // 2, y + h // 2), 2, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # Draw a square region in the center of the screen
    cv2.rectangle(frame, (640 // 2 - 30, 480 // 2 - 30),
                  (640 // 2 + 30, 480 // 2 + 30),
                  (255, 255, 255), 3)

    cv2.imshow('img', frame)

    # Press 'q' to quit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
