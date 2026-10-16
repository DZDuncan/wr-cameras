import os
import sys
import urllib.parse

import cv2

# Define connection credentials
IP = "192.168.1.108"
PORT = "554"          # Default RTSP port for Amcrest
USER = "admin"
PASSWORD = os.environ.get("PASSWORD")
if not PASSWORD:
	print("No password found... exiting!")
	sys.exit()

CHANNEL = "1"         # Channel 1 is standard
SUBTYPE = "0"         # 0 = Main Stream (High Res), 1 = Sub Stream (Low Res)

# Construct the standard Amcrest RTSP URL
encoded_password = urllib.parse.quote(PASSWORD, safe="")
rtsp_url = f"rtsp://{USER}:{encoded_password}@{IP}:{PORT}/cam/realmonitor?channel={CHANNEL}&subtype={SUBTYPE}"

# Initialize video capture
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open the video stream. Check credentials or network connectivity.")
    exit()

print("Press 'q' inside the video window to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Display the live stream
    cv2.imshow("Amcrest Live Stream", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
