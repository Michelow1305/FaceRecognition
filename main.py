'''
pip install deepface
https://github.com/serengil/deepface
Read more at: https://viso.ai/computer-vision/deepface/

db_path="C:/Users/miche/Desktop/Python/FaceRecognition/db"
'''
from deepface import DeepFace
import cv2
import time
import MyPlot
import FileHandling

# Set the capture device to your webcam (usually 0)
cap = cv2.VideoCapture(0)

# Define the countdown interval (in seconds)
interval_seconds = 3

# Create a window to display the live camera feed
windowName = "Live Webcam Feed"
cv2.namedWindow(windowName)

i = 0
last_snapshot_time = time.time()

try:
    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Display the live webcam feed
        cv2.imshow(windowName, frame)

        # Check if it's time to take a snapshot
        if time.time() - last_snapshot_time >= interval_seconds:
            i += 1

            image_path = FileHandling.handleTemporaryImage(i, frame)

            # do some processing with DeepFace:
            objs = DeepFace.analyze(
                img_path=image_path,
                detector_backend='mtcnn',
                silent=True
            )
            print("\nProcessing done!\n")
            MyPlot.printDominantValues(objs)
            print("\nMaking plot...")
            MyPlot.plot_face_data(objs)

            # Update the last snapshot time
            last_snapshot_time = time.time()

        # Press 'q' to exit the stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            FileHandling.deleteImage(i)
            break

except FileNotFoundError:
    print("File you wanted to delete is not there, so, yea.... We got an error but whatever.")

# Release the webcam and close any open windows
cap.release()
cv2.destroyAllWindows()
