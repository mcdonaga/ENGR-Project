import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

def Life2CodingRGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  # checks mouse moves
        colorsBGR = image[y, x]
        colorsRGB = tuple(reversed(colorsBGR))  # Reversing the OpenCV BGR format to RGB format
        cv2.rectangle(combined_image, (0, image.shape[0]), (image.shape[1], image.shape[0] + 50), (255, 255, 255), -1)  # draw a white rectangle to clear the previous text
        cv2.putText(combined_image, "RGB Value: {}".format(colorsRGB), (10, image.shape[0] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)  # display the RGB value
        cv2.imshow('RGB Values', np.zeros((50, 400, 3), dtype=np.uint8) + colorsBGR)  # create and display a new window showing the RGB value
        cv2.rectangle(rgb_image, (0, 0), (400, 50), (255, 255, 255), -1)
        cv2.putText(rgb_image, str(colorsRGB), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('RGB Values as Number', rgb_image)

# Create a Tkinter window
root = tk.Tk()
root.withdraw()

# Ask the user to select an image file
file_path = filedialog.askopenfilename()

# Read the image file
image = cv2.imread(file_path)

# Check if the image was read successfully
if image is None:
    print("Could not read image file: {}".format(file_path))
else:
    # Create windows and set Mousecallback to a function for the main window
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', Life2CodingRGB)
    cv2.namedWindow('RGB Values')
    cv2.namedWindow('RGB Values as Number')

    # Create an empty image for showing the RGB value as a number
    rgb_image = np.zeros((50, 400, 3), dtype=np.uint8) + 255

    # Show the image and wait for key press
    while (1):
        # Create a new image that is a combination of the original image and the rectangle with the text
        combined_image = cv2.vconcat([image, np.zeros((50, image.shape[1], 3), dtype=np.uint8) + 255])  # create a new image with a white rectangle at the bottom
        cv2.imshow('Image', combined_image)
        if cv2.waitKey(10) & 0xFF == 27:  # wait for Esc key to be pressed
            break

    # Close all windows when done
    cv2.destroyAllWindows()
