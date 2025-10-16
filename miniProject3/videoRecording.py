import cv2
from datetime import datetime

# Open camera
camera = cv2.VideoCapture(0)

# Get frame size
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Codec and filename
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"

# Create VideoWriter object
recording = cv2.VideoWriter(filename, fourcc, 30, (frame_width, frame_height))

print("Press 'r' to start recording, 'q' to stop recording, and 'e' to exit.")

is_recording = False

while True:
    success, frame = camera.read()
    if not success:
        break

    # Show the camera window
    cv2.imshow("Camera", frame)

    # Read key once per loop
    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        is_recording = True
        print("Recording started...")

    elif key == ord('q'):
        is_recording = False
        print("Recording stopped.")

    elif key == ord('e'):
        print("Exiting program...")
        break

    # If recording, save the frame
    if is_recording:
        recording.write(frame)

# Release resources
recording.release()
camera.release()
cv2.destroyAllWindows()
print(f"Video saved as {filename}")
