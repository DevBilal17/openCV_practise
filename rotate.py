import cv2

image = cv2.imread("image.png")

if image is None:
    print("Error: Image is not found")
else:
    (h,w) = image.shape[:2]
    center = (w//2,h//2)
    M = cv2.getRotationMatrix2D(center,-45,1)
    rotate = cv2.warpAffine(image,M,(w,h))
    cv2.imshow("Original Image",image)
    cv2.imshow("Resized Image",rotate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()