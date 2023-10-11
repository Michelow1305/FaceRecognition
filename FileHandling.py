import cv2
from cv2 import Mat
import os

# Define the directory where you want to save the snapshots
save_directory = "snapshots/"


def handleTemporaryImage(i: int, frame: Mat):
    # Save the snapshot to a file
    image_path = f"{save_directory}snapshot_{i}.png"
    cv2.imwrite(image_path, frame)

    print(f"Snapshot saved!")

    # delete the previous image
    deleteImage(i-1)
    return image_path


def deleteImage(i: int):
    image_path = f"{save_directory}snapshot_{i}.png"
    if os.path.exists(image_path):
        os.remove(image_path)
