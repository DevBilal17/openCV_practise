import cv2

image = cv2.imread("image.png")

if image is None:
    print("Error: Image is not found")
else:
    cropped_image = image[50:200,100:400]
    cv2.imshow("Original Image",image)
    cv2.imshow("Cropped Image",cropped_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()