
import cv2

camera = cv2.VideoCapture(0)

choice =  input("For Start Recording press 'r' and to quit recording press 'q' to exit press 'e'")

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'MP4V')


while True:
    success,frames = camera.read()

    if not success:
        break

    if choice.lower() == 'r':
        break

    