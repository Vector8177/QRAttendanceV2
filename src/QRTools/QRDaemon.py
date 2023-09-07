import json

import cv2
from pyzbar.pyzbar import decode
import time

from src.UI.Dashboard.MembersFrame import MembersFrame


class QRDaemon:
    def __init__(self, member_list: MembersFrame):
        self.member_list = member_list

    # Function to decode and display QR code
    def read_qr_code(self, image):
        # Decode QR code
        decoded_objects = decode(image)

        for obj in decoded_objects:
            # Extract QR code data
            qr_data = obj.data.decode('utf-8')

            if self.member_list.check_signed_in(qr_data):
                self.member_list.sign_out(qr_data)
            else:
                with open("src/Data/MemberList.json") as f:
                    temp = json.load(f)
                    if not temp.get(qr_data) is None:
                        self.member_list.sign_in(qr_data)

            print("QR Code Data:", qr_data)

            # Display the QR code data on the screen
            cv2.putText(image, qr_data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("QR Code Reader", image)
            cv2.waitKey(0)

    def main(self):
        # Initialize the camera or read a video file
        cap = cv2.VideoCapture(0)  # Change to the appropriate camera index or video file path

        while True:
            # Read a frame from the camera or video file
            ret, frame = cap.read()

            if not ret:
                break

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
