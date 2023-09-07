import cv2
from pyzbar.pyzbar import decode
import time


# Function to decode and display QR code
def read_qr_code(image):
    # Decode QR code
    decoded_objects = decode(image)

    for obj in decoded_objects:
        # Extract QR code data
        qr_data = obj.data.decode('utf-8')
        print("QR Code Data:", qr_data)

        # Display the QR code data on the screen
        cv2.putText(image, qr_data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("QR Code Reader", image)
        cv2.waitKey(0)


def main():
    # Initialize the camera or read a video file
    cap = cv2.VideoCapture(0)  # Change to the appropriate camera index or video file path

    while True:
        # Read a frame from the camera or video file
        ret, frame = cap.read()

        if not ret:
            break

        # Detect and decode QR codes in the frame
        read_qr_code(frame)

        # Wait for 2 seconds before processing the next code
        time.sleep(2)

        # Close the displayed window if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()