import cv2
import numpy as np

# 检测红绿点坐标
def detect_red_and_green(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 将图像从 BGR 色彩空间转换为 HSV 色彩空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义红色和绿色的HSV范围
    lower_red = np.array([165, 100, 100])
    upper_red = np.array([179, 255, 255])
    lower_green = np.array([36, 100, 100])
    upper_green = np.array([86, 255, 255])

    # 根据阈值创建红色和绿色的掩码
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # 寻找红色和绿色区域的轮廓
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历红色区域的轮廓
    for contour in contours_red:
        # 获取轮廓的边界框坐标
        x, y, w, h = cv2.boundingRect(contour)
        # 在图像上绘制红色边界框
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # 在图像上标出红色区域的中心坐标
        cv2.putText(image, f'Red: ({x + w // 2}, {y + h // 2})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # 遍历绿色区域的轮廓
    for contour in contours_green:
        # 获取轮廓的边界框坐标
        x, y, w, h = cv2.boundingRect(contour)
        # 在图像上绘制绿色边界框
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # 在图像上标出绿色区域的中心坐标
        cv2.putText(image, f'Green: ({x + w // 2}, {y + h // 2})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 返回带有标记的图像
    return image

#使图像易于处理
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

    return blurred_image

#描绘四边矩形
def detect_quadrilaterals(image):
    # 边缘检测
    edges = cv2.Canny(image, 50, 150)

    # 轮廓检测
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)

    # 复制图像以避免修改原始图像
    annotated_image = image.copy()

    # 遍历轮廓
    for contour in contours:
        # 计算轮廓面积
        area = cv2.contourArea(contour)

        # 去除干扰部分的面积
        min_area = 500000
        max_area = 800000000000
        if min_area < area < max_area:
            # 进行轮廓逼近
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.01 * peri, True)

            # 如果逼近的轮廓有四个顶点，则认为是四边形
            if len(approx) == 4:
                # 在图像上绘制绿色的轮廓
                cv2.drawContours(annotated_image, [approx], -1, (0, 255, 0), 2)

                # 计算四边形的中心点
                M = cv2.moments(approx)
                if M['m00'] != 0:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])

                    # 在图像上标记中心点为蓝色
                    cv2.circle(annotated_image, (cx, cy), 5, (255, 0, 0), -1)
                    cv2.putText(annotated_image, f'({cx}, {cy})', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 0, 255), 2)

                # 在图像上标记四个顶点并打印坐标
                for point in approx:
                    x, y = point[0]
                    cv2.circle(annotated_image, (x, y), 5, (0, 0, 255), -1)
                    cv2.putText(annotated_image, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 0, 255), 2)

    return annotated_image



# 主函数
if __name__ == "__main__":
    image_path = 'week_9/src_1/img_3.jpeg'
    Upload_Str1 = 'week_9/out/out_3/1_Corner_Detection Image.jpeg'
    Upload_Str2 = 'week_9/out/out_3/2_Red_Green Detection.jpeg'
    Upload_Str3 = 'week_9/out/out_3/3_Final_Image.jpeg'

    # 图像预处理
    # image = cv2.
    processed_image = preprocess_image(image_path)

    # 检测四边形并标记特征
    annotated_image = detect_quadrilaterals(processed_image)

    # 检测红色和绿色区域并标记
    red_green_image = detect_red_and_green(image_path)
    
    # 将角点和红绿点标记同时显示在图像上
    Final_image = cv2.addWeighted(annotated_image,0.5,red_green_image,0.5,-1)

    # 保存图像
    cv2.imwrite(Upload_Str1, annotated_image)
    cv2.imwrite(Upload_Str2, red_green_image)
    cv2.imwrite(Upload_Str3, Final_image)
    
    # 显示结果
    cv2.imshow('Final Image',Final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()