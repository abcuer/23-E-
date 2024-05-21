import cv2
import numpy as np

def preprocess_image(image):
    
    Denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    Enhanced_image = cv2.convertScaleAbs(Denoised_image, alpha=1, beta=30)
    canny_image = cv2.Canny(Enhanced_image, 50, 150)
    
    return canny_image

def detect_quadrilaterals(image):
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    quadrilaterals = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >2000:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.01 * peri, True)

            if len(approx) == 4:
                quadrilaterals.append(approx)

    return quadrilaterals
def draw_points(image, quadrilaterals):  
  
    annotated_image = image.copy()  
      
    for quad in quadrilaterals:  
        cv2.drawContours(annotated_image, [quad], -1, (255, 0, 0), 2)  
  
        for i, point in enumerate(quad):  
            x, y = point[0]  
            cv2.circle(annotated_image, (x, y), 5, (0, 0, 255), -1)  
            cv2.putText(annotated_image, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  
            print(f"角点{i+1} 坐标: ({x}, {y})")  
              
        # 标记四边形的中心点  
        M = cv2.moments(quad)  
        if M['m00'] != 0: 
            cx = int(M['m10'] / M['m00'])  
            cy = int(M['m01'] / M['m00'])  
            cv2.circle(annotated_image, (cx, cy), 5, (0, 0, 255), -1) 
            cv2.putText(annotated_image, f'({cx}, {cy})', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  
            print(f"中点 坐标: ({cx}, {cy})")  
  
    return annotated_image  

# 主函数
if __name__ == "__main__":
    image = cv2.imread('week_9\src\img_5.jpeg')

    processed_image = preprocess_image(image)
    quadrilaterals = detect_quadrilaterals(processed_image)
    Annotated_Image = draw_points(image, quadrilaterals)

    cv2.namedWindow('Annotated Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Annotated Image', Annotated_Image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
