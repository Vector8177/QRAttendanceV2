import json
from queue import Queue

import cv2
import time

from src.Constants import Constants
from src.UI.Dashboard.MembersFrame import MembersFrame


class QRDaemon:
    def __init__(self, member_list: MembersFrame, img_q: Queue):
        self.member_list = member_list
        self.qr_code_detector = cv2.QRCodeDetector()
        self.img_q = img_q

    # Function to decode and display QR code
    def read_qr_code(self, image):
        # Decode QR code
        data, bbox, _ = self.qr_code_detector.detectAndDecode(image)

        if data:
            if self.member_list.check_signed_in(data):
                self.member_list.sign_out(data)
            else:
                with open(Constants.JSON_PATH) as f:
                    temp = json.load(f)
                    if not temp.get(data) is None:
                        self.member_list.sign_in(data)

            print("QR Code Data:", data)

            # Display the QR code data on the screen

            cv2.waitKey(0)

    def main(self):
        # Initialize the camera or read a video file
        cap = cv2.VideoCapture(0)  # Change to the appropriate camera index or video file path

        while True:
            # Read a frame from the camera or video file
            ret, frame = cap.read()

            if not ret:
                break
            if self.img_q.not_full:
                self.img_q.put(frame)

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect and decode QR codes in the frame
            self.read_qr_code(gray_frame)

            # Wait for 2 seconds before processing the next code
            time.sleep(2)

            # Close the displayed window if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()