import cv2
import redgreen

# 检测红色和绿色区域并标记
processed_image = redgreen.detect_red_and_green('week_9\src_1\img_1.jpg')

# 显示带有标记的图像
cv2.imshow('Detected Colors', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



