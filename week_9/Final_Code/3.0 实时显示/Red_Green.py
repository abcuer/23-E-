import cv2
import numpy as np

def detect_color(hsv, lower_color, upper_color):
    
    # 根据阈值创建掩码
    mask_color = cv2.inRange(hsv, lower_color, upper_color)

    # 寻找绿色区域的轮廓
    contours_color, _ = cv2.findContours(mask_color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 计算绿色轮廓的中心位置
    if len(contours_color) > 0:
        # 找到最大的轮廓
        max_contour = max(contours_color, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        center_x = x + w // 2
        center_y = y + h // 2
    else:
        center_x, center_y = 0, 0

    # 输出中心坐标
    print('center_x:', center_x, 'center_y:', center_y)

    return center_x, center_y
# 检测绿点坐标 
def detect_green(image):

    # 将图像从BGR色彩空间转换为HSV色彩空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义绿色的HSV范围（可根据需要动态调整）
    lower_green = np.array([36, 100, 100])
    upper_green = np.array([86, 255, 255])
    
    return detect_color(hsv, lower_green, upper_green)
# 检测红绿点坐标
def detect_red(image):

    # 输入校验
    if not isinstance(image, np.ndarray) or image.shape[2] != 3:
        raise ValueError("输入的image必须是一个BGR图像")
    
    # 将图像从BGR色彩空间转换为HSV色彩空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 将图像从 BGR 色彩空间转换为 HSV 色彩空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义红色的HSV范围
    lower_red = np.array([165, 100, 100])
    upper_red = np.array([179, 255, 255])
    
    return detect_color(hsv, lower_red, upper_red)
def draw_points(image, center_x, center_y):
    
    # # 在图像上绘制红色边界框
    # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    # # 在图像上标出红色区域的中心坐标
    cv2.putText(image, f'point: ({center_x}, {center_y})', (center_x, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

def find_red_green(image):
    center_x, center_y = detect_red(image)
    draw_points(image, center_x, center_y)

    center_x, center_y = detect_green(image)
    draw_points(image, center_x, center_y)
    
    return image

if __name__ == '__main__': 

    image = cv2.imread('week_9/src/img_3.jpeg')
    image = find_red_green(image)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
