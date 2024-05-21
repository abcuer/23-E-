import cv2
import numpy as np

def detect_color(hsv, lower_color, upper_color):

    mask_color = cv2.inRange(hsv, lower_color, upper_color)
    contours_color, _ = cv2.findContours(mask_color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_color) > 0:
        max_contour = max(contours_color, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        center_x = x + w // 2
        center_y = y + h // 2
    else:
        center_x, center_y = 0, 0
    print('center_x:', center_x, 'center_y:', center_y)

    return center_x, center_y

def detect_green(image):

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([36, 100, 100])
    upper_green = np.array([86, 255, 255])
    
    return detect_color(hsv, lower_green, upper_green)

def detect_red(image):
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([165, 100, 100])
    upper_red = np.array([179, 255, 255])
    
    return detect_color(hsv, lower_red, upper_red)
def draw_points(image, center_x, center_y):
  
    cv2.putText(image, f'point: ({center_x}, {center_y})', (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

def find_red_green(image):
    center_x, center_y = detect_red(image)
    draw_points(image, center_x, center_y)
    center_x, center_y = detect_green(image)
    draw_points(image, center_x, center_y)
    
    return image

if __name__ == '__main__': 

    image = cv2.imread('week_9/src/img_2.jpeg')
    image = find_red_green(image)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
