import cv2
import numpy as np


def draw(mask, color, frame_arg):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000:
            new_contour = cv2.convexHull(c)
            cv2.drawContours(frame_arg, [new_contour], 0, color, 3)


def capture():
    cap = cv2.VideoCapture(0)

    # Low colors
    low_yellow = np.array([25, 192, 20], np.uint8)  # ([H,S,V]) en V se usa 20 con colores cálidos/suaves
    low_red1 = np.array([0, 100, 20], np.uint8)  # Con el rojo, se declara 2 veces, por eso low_red y high red 1 y 2
    low_red2 = np.array([175, 100, 20], np.uint8)
    low_blue = np.array([100, 170, 20], np.uint8)
    low_green = np.array([55, 100, 20], np.uint8)
    low_pink = np.array([150, 150, 20], np.uint8)

    # High colors
    high_yellow = np.array([30, 255, 255], np.uint8)  # ([H,S,V]) en V se usa 255 con colores fuertes
    high_red1 = np.array([5, 255, 255], np.uint8)
    high_red2 = np.array([180, 255, 255], np.uint8)
    high_blue = np.array([120, 225, 255], np.uint8)
    high_green = np.array([60, 225, 255], np.uint8)
    high_pink = np.array([150, 255, 255], np.uint8)

    while True:
        comp, frame = cap.read()
        if comp == True:
            frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            yellow_mask = cv2.inRange(frame_HSV, low_yellow, high_yellow)
            red_mask1 = cv2.inRange(frame_HSV, low_red1, high_red1)
            red_mask2 = cv2.inRange(frame_HSV, low_red2, high_red2)
            red_mask = cv2.add(red_mask1, red_mask2)  # Este método unifica ambas mascaras
            blue_mask = cv2.inRange(frame_HSV, low_blue, high_blue)
            green_mask = cv2.inRange(frame_HSV, low_green, high_green)
            pink_mask = cv2.inRange(frame_HSV, low_pink, high_pink)

            draw(yellow_mask, [0, 255, 255], frame)  # usamos BGR
            draw(red_mask, [0, 0, 255], frame)
            draw(blue_mask, [255, 0, 0], frame)
            draw(green_mask, [0, 255, 0], frame)
            draw(pink_mask, [255, 0, 255], frame)

            cv2.imshow('Webcam', frame)

            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
                cap.release()
                cv2.destroyAllWindows()
