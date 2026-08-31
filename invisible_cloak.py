

import cv2
import numpy as np
import time


def capture_background(cap, num_frames=60):
    """Warm up the camera and average several frames into a clean background plate."""
    print("Capturing background... step out of frame.")
    time.sleep(2)  # give you time to step away
    backgrounds = []
    for _ in range(num_frames):
        ret, frame = cap.read()
        if ret:
            frame = np.flip(frame, axis=1)  # mirror, feels more natural
            backgrounds.append(frame)
        else:
            time.sleep(0.05)
    if not backgrounds:
        raise RuntimeError("Could not read from camera to capture background.")
    background = np.median(backgrounds, axis=0).astype(np.uint8)
    print("Background captured.")
    return background


def make_cloak_mask(hsv_frame, color="red"):
    """
    Build a binary mask isolating the cloak color.
    'red' wraps around the HSV hue circle (0-10 and 170-180), so it needs
    two ranges OR'd together. 'blue' is a single contiguous range.
    """
    if color == "red":
        lower1 = np.array([0, 120, 70])
        upper1 = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv_frame, lower1, upper1)

        lower2 = np.array([170, 120, 70])
        upper2 = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv_frame, lower2, upper2)

        mask = mask1 | mask2

    elif color == "blue":
        lower = np.array([94, 80, 2])
        upper = np.array([126, 255, 255])
        mask = cv2.inRange(hsv_frame, lower, upper)

    elif color == "pink":
        lower = np.array([130, 40, 60])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(hsv_frame, lower, upper)

    elif color == "yellow":
        lower = np.array([18, 60, 60])
        upper = np.array([40, 255, 255])
        mask = cv2.inRange(hsv_frame, lower, upper)

    else:
        raise ValueError("color must be 'red', 'blue', 'pink', or 'yellow'")

    # Clean up the mask: remove small noise, fill small holes, smooth edges.
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)
    mask = cv2.medianBlur(mask, 5)
    return mask


def main(cloak_color="red"):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam (index 0).")

    background = capture_background(cap)

    print("Cloak effect running. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = np.flip(frame, axis=1)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cloak_mask = make_cloak_mask(hsv, color=cloak_color)
        inverse_mask = cv2.bitwise_not(cloak_mask)

        # Where the cloak is: use background pixels.
        cloak_area = cv2.bitwise_and(background, background, mask=cloak_mask)
        # Everywhere else: use the live frame.
        visible_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)

        final_output = cv2.addWeighted(cloak_area, 1, visible_area, 1, 0)

        cv2.imshow("Invisible Cloak", final_output)
        cv2.imshow("Mask (debug)", cloak_mask)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Switch to "red", "blue", or "pink" for other cloth colors.
    main(cloak_color="yellow")