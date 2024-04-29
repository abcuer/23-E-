# import numpy as np
# import cv2 as cv

# filename = 'week_9\src_1\img_1.jpeg'
# img = cv.imread(filename)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# find Harris corners
# gray = np.float32(gray)
# dst = cv.cornerHarris(gray, 2, 3, 0.04)
# dst = cv.dilate(dst, None)
# ret, dst = cv.threshold(dst, 0.01 * dst.max(), 255, 0)
# dst = np.uint8(dst)

# # find centroids
# ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

# # define the criteria to stop and refine the corners
# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# corners = cv.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)

# # Now draw them
# res = np.hstack((centroids, corners))
# res = np.intp(res)
# img[res[:, 1], res[:, 0]] = [0, 0, 255]  # Mark centroids as red
# img[res[:, 3], res[:, 2]] = [0, 255, 0]  # Mark refined corners as green

import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取图像
img = cv2.imread("week_9\src_1\img_1.jpeg")

#灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Harris角点检测函数
dst = cv2.cornerHarris(src = gray, blockSize = 2, ksize = 3, k = 0.04)

#图像中大于0.01*dst.max()的角点标记颜色
img[dst > 0.01*dst.max()] = (0,0,255)

#展示处理
# cv2.imshow('IMAGE',img)


# Save the modified image
cv2.imwrite('week_9\out\Harris_drawed_img.jpeg', img)



# 没有效果，不考虑此方案
