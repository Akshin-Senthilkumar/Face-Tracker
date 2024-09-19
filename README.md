Overview:
This project demonstrates a real-time face tracking system that uses OpenCV for face detection and Arduino to control servos based on the detected face coordinates. The system captures video from a webcam, detects faces using a Haar Cascade classifier, and sends the coordinates to an Arduino board to adjust servo positions accordingly.

Features:
Real-time face detection using OpenCV's Haar Cascade classifier.
Sends detected face coordinates to Arduino via serial communication.
Displays video with overlayed face rectangles and a central reference square.
Components
Hardware: Arduino, Servos
Software: Python (OpenCV, PySerial), Arduino IDE
Installation
Install Dependencies:

Ensure Python is installed on your system.
Install required Python libraries using pip:
bash
Copy code
pip install opencv-python pyserial
Prepare the Haar Cascade Classifier:

Download the Haar Cascade XML file from OpenCV's repository.
Place the XML file in your project directory and update the path in the code.
Arduino Setup:

Upload the provided Arduino sketch to your Arduino board using the Arduino IDE.
Usage
Run the Python Script:

Ensure the Arduino is connected to your computer and the correct serial port is specified in the script.
Execute the Python script:
bash
Copy code
python your_script_name.py
Interacting with the System:

The video feed will be displayed with rectangles around detected faces and a central reference square.
The Arduino will adjust the servos based on the detected face coordinates.
Stopping the Script:

Press 'q' in the video window to exit the application.
License
This project is licensed under the MIT License.

Acknowledgements
OpenCV for face detection functionality.
Arduino for servo control.
