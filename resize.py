
import cv2

image = cv2.imread("image.png")

if image is None:
    print("Error: Image is not found")
else:
    resize = cv2.resize(image,(200,200))
    cv2.imshow("Original Image",image)
    cv2.imshow("Resized Image",resize)

    cv2.waitKey(0)
    cv2.destroyAllWindows()