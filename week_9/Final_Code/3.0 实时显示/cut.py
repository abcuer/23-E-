import cv2
import numpy as np
import Edge_Detection

def find_max_perimeter_contour(contours, max_allowed_perimeter, min_allowed_perimeter):
    # 输入参数校验
    if not contours or max_allowed_perimeter <= 0:
        raise ValueError("输入的轮廓列表不能为空, 且最大允许周长必须为正数。")

    # 初始化最大周长及对应轮廓变量, 以及标志位表示是否找到符合条件的轮廓
    max_perimeter = 0
    vertices = None

    # 遍历轮廓列表
    for cnt in contours:
        # 将当前轮廓近似为四边形
        approx = cv2.approxPolyDP(cnt, 0.09 * cv2.arcLength(cnt, True), True)

        # 确保转换后的形状为四边形
        if len(approx) == 4:
            # 计算四边形周长
            perimeter = cv2.arcLength(approx, True)
            perimeter_allowed = (perimeter <= max_allowed_perimeter) and (perimeter >= min_allowed_perimeter)
            
            if perimeter_allowed and perimeter > max_perimeter:
                # 计算四边形角度
                cosines = []
                for i in range(4):
                    p0 = approx[i][0]
                    p1 = approx[(i + 1) % 4][0]
                    p2 = approx[(i + 2) % 4][0]
                    v1 = p0 - p1
                    v2 = p2 - p1
                    cosine_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
                    angle = np.arccos(cosine_angle) * 180 / np.pi
                    cosines.append(angle)

                # 若当前轮廓周长在允许范围内、大于当前最大周长且角度大于等于N度
                if all(angle >= 30 for angle in cosines):
                    max_perimeter = perimeter
                    vertices = approx.reshape(4, 2)

    # 检查是否找到符合条件的轮廓
    if vertices is None:
        # 返回空列表代替None, 或可选择抛出异常
        return None
    else:
        return vertices

def roi_cut(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [vertices], (255, 255, 255))
    masked_image = cv2.bitwise_and(image, mask)

    return masked_image

def find_point(image):

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    def find_max_contours(mask):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            # 找到最大的轮廓
            largest_contour = max(contours, key=cv2.contourArea)
            # 找到最大轮廓的外接矩形
            x, y, w, h = cv2.boundingRect(largest_contour)  
            
            center_x = x + w / 2  # 计算中心点 x 坐标
            center_y = y + h / 2  # 计算中心点 y 坐标

            point = [x, y, w, h, center_x, center_y]
            # print(point)
            return point
        else:
            return [0,0,0,0,0,0]
        

if __name__ == '__main__':
    image = cv2.imread('week_9\src\img_2.jpeg')
    # 预处理图像
    image = Edge_Detection.preprocess_image(image)
    # 检测四边形
    point = find_point(image)
    # 绘制四边形
    image = Edge_Detection.draw_points(image, point)
    # 提取 ROI
    roi= roi_cut(image, point)

    cv2.imshow('image', roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

