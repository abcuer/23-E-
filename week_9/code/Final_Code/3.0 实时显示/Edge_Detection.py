import cv2
import numpy as np
import Red_Green
def preprocess_image(image):
    # image = cv2.imread(image_path)

    # 去噪
    Denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
  
    # 图像增强和对比度增强
    Enhanced_image = cv2.convertScaleAbs(Denoised_image, alpha=1, beta=30)
    
    # 边缘检测
    canny_image = cv2.Canny(Enhanced_image, 50, 150)
    
    return canny_image

def detect_quadrilaterals(image):
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 建立一个四边形列表
    quadrilaterals = []
    # 遍历轮廓
    for contour in contours:
        # 计算轮廓面积
        area = cv2.contourArea(contour)
        # 去除干扰部分的区域
        min_area = 50000
        max_area = 8000000000000
        if min_area < area < max_area:
            # 对轮廓进行逼近
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.01 * peri, True)

            # 如果逼近的轮廓有四个顶点，则认为是四边形
            if len(approx) == 4:
                quadrilaterals.append(approx)

    return quadrilaterals
        
        
# def draw_points(image, quadrilaterals):  
#     # image = cv2.imread(image_path)      

#     annotated_image = image.copy()
    
#     for quad in quadrilaterals:
#         # 绘制轮廓
#         cv2.drawContours(annotated_image, [quad], -1, (255, 0, 0), 2)

#         # 在图像上标记四个端点并打印坐标
#         for i,point in enumerate(quad):
#             x, y = point[0]
#             cv2.circle(annotated_image, (x, y), 5, (0, 0, 255), -1)
#             cv2.putText(annotated_image, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 0, 255), 2)
            
#             # 标记四边形的中心点
#             M = cv2.moments(quad)
#             cx = int(M['m10'] / M['m00'])
#             cy = int(M['m01'] / M['m00'])
#             cv2.circle(annotated_image, (cx, cy), 5, (0, 0, 255), -1)
#             cv2.putText(annotated_image, f'({cx}, {cy})', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 0, 255), 2)

#     return annotated_image

def draw_points(image, quadrilaterals):  
    # image = cv2.imread(image_path)  # 如果需要的话，取消注释这行代码并传入image_path  
  
    annotated_image = image.copy()  
      
    for quad in quadrilaterals:  
        # 绘制轮廓  
        cv2.drawContours(annotated_image, [quad], -1, (255, 0, 0), 2)  
  
        # 在图像上标记四个端点并打印坐标  
        for i, point in enumerate(quad):  
            x, y = point[0]  # 直接假设point是一个(x, y)的元组  
            cv2.circle(annotated_image, (x, y), 5, (0, 0, 255), -1)  
            cv2.putText(annotated_image, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 0, 255), 2)  
 
            # 在终端打印坐标  
            print(f"拐角{i+1} 坐标: ({x}, {y})")  
              
        # 标记四边形的中心点  
        M = cv2.moments(quad)  
        if M['m00'] != 0:  # 确保分母不为0  
            cx = int(M['m10'] / M['m00'])  
            cy = int(M['m01'] / M['m00'])  
            cv2.circle(annotated_image, (cx, cy), 5, (0, 255, 0), -1)  # 使用绿色表示中心点  
            cv2.putText(annotated_image, f'({cx}, {cy})', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  
              
            # 在终端打印中心点坐标  
            print(f"中点 坐标: ({cx}, {cy})")  
  
    return annotated_image  

# 主函数
if __name__ == "__main__":
    image = cv2.imread('week_9\src\img_5.jpeg')

    # 图像预处理
    processed_image = preprocess_image(image)
    # 检测四边形并标记特征
    quadrilaterals = detect_quadrilaterals(processed_image)
    # 最终图像
    Annotated_Image = draw_points(processed_image, quadrilaterals)
    # 显示结果
    cv2.imshow('Annotated Image', Annotated_Image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
