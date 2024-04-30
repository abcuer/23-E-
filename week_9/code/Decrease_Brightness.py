import cv2
import numpy as np

def decrease_brightness_contrast(image, brightness_factor, contrast_factor=1.0):
    # 确保亮度因子在0到1之间
    brightness_factor = max(0, min(1, brightness_factor))

    # 将图像转换为浮点数以便进行运算
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    # 调整亮度
    v = cv2.convertScaleAbs(v, alpha=brightness_factor, beta=0)

    # 如果需要调整对比度，可以这样做（可选）
    # 对比度调整通常通过以下公式实现：f(x) = alpha * x + beta
    # 但对于8位图像，我们通常在0-255范围内进行调整
    # s = cv2.convertScaleAbs(s, alpha=contrast_factor, beta=128*(1-contrast_factor))
    # 但是在这个例子中，我们保持对比度不变

    # 合并通道
    final_hsv = cv2.merge((h, s, v))
    image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    return image

# 读取图片
image = cv2.imread('week_9/src_2/img_5.png')

# 尝试不同的亮度因子，找到能够凸出黑色线的最佳值
dimmed_image = decrease_brightness_contrast(image, 0.5)  # 可以调整这个值

# 显示图片
cv2.imshow('Original Image', image)
cv2.imshow('Dimmed Image', dimmed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


