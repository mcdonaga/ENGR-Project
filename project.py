import cv2

def Life2CodingRGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  # checks mouse moves
        colorsBGR = image[y, x]
        colorsRGB = tuple(reversed(colorsBGR))  # Reversing the OpenCV BGR format to RGB format
        print("RGB Value at ({},{}):{} ".format(x, y, colorsRGB))

# Set the image file path
image_file = "/Users/gavinmcdonald/Desktop/PYTHON/ENGR project/graph.jpg"

# Read the image file
image = cv2.imread(image_file)

# Check if the image was read successfully
if image is None:
    print("Could not read image file: {}".format(image_file))
else:
    # Create a window and set Mousecallback to a function for that window
    cv2.namedWindow('Life2CodingRGB')
    cv2.setMouseCallback('Life2CodingRGB', Life2CodingRGB)

    # Show the image and wait for key press
    while (1):
        cv2.imshow('Life2CodingRGB', image)
        if cv2.waitKey(10) & 0xFF == 27:  # wait for Esc key to be pressed
            break

    # Close all windows when done
    cv2.destroyAllWindows()
