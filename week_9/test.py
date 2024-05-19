# import cv2

# img = cv2.imread("week_9\src\img_3.jpeg")
# h,w,c = img.shape
# print(f'高度：{h}')
# print(f'宽度：{w}')
# print(f'通道：{c}')

import cv2

# 加载图像
img = cv2.imread('week_9\src\img_1.jpeg')

# 设定目标大小，宽度为640像素，高度自动计算
target_size = (640, -1)  # -1 表示高度自动计算

# 使用cv2.resize调整图像大小
resized_img = cv2.resize(img, target_size)

# 显示原始图像和缩放后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()