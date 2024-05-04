import cv2 
import numpy as np
import Edge_Detection
import Red_Green

image_path = 'week_9/src_1/img_1.jpeg'
image = cv2.imread(image_path)

# 保存路径
Upload_Str1 = 'week_9/Code/Final_Code/second/Output_2/out_1/1_EdgeDetection_Image(1).jpeg'
Upload_Str2 = 'week_9/Code/Final_Code/second/Output_2/out_1/2_RedGreen_Image(1).jpeg'
Upload_Str3 = 'week_9/Code/Final_Code/second/Output_2/out_1/3_Final_Image(1).jpeg'

# 红绿点图像
RedGreen_image = Red_Green.detect_red_and_green(image_path)

# 角点和中点坐标图像
processed_image = Edge_Detection.preprocess_image(image_path)
quadrilaterals = Edge_Detection.detect_quadrilaterals(processed_image)
annotated_image = Edge_Detection.draw_points(image, quadrilaterals)

# 图像叠加
Final_image = cv2.addWeighted(annotated_image, 0.5, RedGreen_image, 0.5, 0)

# 保存图像
cv2.imwrite(Upload_Str1, annotated_image)
cv2.imwrite(Upload_Str2, RedGreen_image)
cv2.imwrite(Upload_Str3, Final_image)

# 显示结果
cv2.imshow('Final Image',Final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()