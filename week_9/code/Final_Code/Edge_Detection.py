import cv2
import numpy as np
import Red_Green

def preprocess_image(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 图像增强和对比度增强
    alpha = 1.5  # 对比度增强参数
    beta = 15  # 亮度增强参数
    enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    
    # 去噪
    denoised_image = cv2.fastNlMeansDenoisingColored(enhanced_image, None, 10, 10, 7, 21)

    # 高斯平滑
    blurred_image = cv2.GaussianBlur(denoised_image, (5, 5), 0)
    
    # 边缘检测
    canny_image = cv2.Canny(blurred_image, 50, 150)
    
    return canny_image

def detect_quadrilaterals(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 建立一个四边形列表
    quadrilaterals = []
    
    # 遍历轮廓
    for contour in contours:
        # 计算轮廓面积
        area = cv2.contourArea(contour)
        # 去除干扰部分的面积
        if area > 2000:
            # 对轮廓进行逼近
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.01 * peri, True)

            # 如果逼近的轮廓有四个顶点，则认为是四边形
            if len(approx) == 4:
                quadrilaterals.append(approx)

    return quadrilaterals
        
        
# def draw_points(image,quadrilaterals):        
#     annotated_image = image.copy()
#     for quad in quadrilaterals:
#         # 绘制轮廓
#         cv2.drawContours(annotated_image, [quad], -1, (0, 255, 0), 2)

#          # 在图像上标记四个端点并打印坐标
#         for i,point in enumerate(quad):
#             x, y = point[0]
#             cv2.circle(annotated_image, (x, y), 5, (0, 0, 255), -1)
#             cv2.putText(annotated_image, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 150, 255), 2)
            
#             # 计算四边形的中心点
#             M = cv2.moments(quad)
#             cx = int(M['m10'] / M['m00'])
#             cy = int(M['m01'] / M['m00'])

#             # 在图像上标记中心点为红色
#             cv2.circle(annotated_image, (cx, cy), 5, (0, 0, 255), -1)
#             cv2.putText(annotated_image, f'({cx}, {cy})', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 150, 255), 2)

#     return annotated_image
def draw_points(image, quadrilaterals):
    marked_image = np.array(image)

    for quad in quadrilaterals:
        # 绘制轮廓
        cv2.drawContours(marked_image, [quad], -1, (255, 0, 0), 2)

        # 绘制顶点并标记坐标
        for i, point in enumerate(quad):
            x, y = point[0]
            cv2.circle(marked_image, (x, y), 5, (0, 255, 0), -1)
            cv2.putText(marked_image, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # 计算中心点并标记坐标
        M = cv2.moments(quad)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(marked_image, (cx, cy), 5, (0, 0, 255), -1)
        cv2.putText(marked_image, f"({cx}, {cy})", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    return marked_image
# 主函数
if __name__ == "__main__":
    image_path = 'week_9\src_1\img_1.jpeg'

    # 图像预处理
    processed_image = preprocess_image(image_path)
    # 检测四边形并标记特征
    quadrilaterals = detect_quadrilaterals(processed_image)
    # 最终图像
    Annotated_Image = draw_points(image_path, quadrilaterals)
    # 显示结果
    cv2.imshow('Annotated Image', Annotated_Image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
