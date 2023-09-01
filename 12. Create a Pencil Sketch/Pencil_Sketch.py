import cv2

# ---------------------------------------------------------- #
# Read the image
image = cv2.imread("Advance/messi-world-cup-jpeg-6486-1689415854.jpg")
cv2.imshow("Messi", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ---------------------------------------------------------- #
# Create a new image by converting the original image to greyscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Messi", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ---------------------------------------------------------- #
# Invert the new grayscale image
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ---------------------------------------------------------- #
# Blur the image by using the Gaussian Function in OpenCV
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
# ---------------------------------------------------------- #
# Convert the image into a pencil sketch
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ---------------------------------------------------------- #
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)