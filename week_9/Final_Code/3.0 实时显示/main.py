import cv2   
import numpy as np  
import Edge_Detection  
import Red_Green  
  
# reading the video (请确保2是正确的摄像头索引或修改为对应的索引)  
source = cv2.VideoCapture(1)  
  
# 确保摄像头打开成功  
if not source.isOpened():  
    print("打开视频流或文件出错！")  
    exit()  
  
# 运行循环  
while True: 
      
    # extracting the frames  
    ret, img = source.read()  
  
    # 检查是否成功读取帧  
    if not ret:  
        print("无法接收帧(视频流结束?)。退出……") 
        break  
  
     # 红绿点图像  
    RedGreen_image = Red_Green.find_red_green(img)  

    # 角点和中点坐标图像  
    # processed_image = Edge_Detection.preprocess_image(img)  
    # quadrilaterals = Edge_Detection.detect_quadrilaterals(processed_image)  
    # annotated_image = Edge_Detection.draw_points(img, quadrilaterals)  
  
    # 图像叠加  
    # Final_image = cv2.addWeighted(annotated_image, 0.5, RedGreen_image, 0.5, 0)  

    Final_image = RedGreen_image

  
    # 视频展示  
    cv2.imshow("Final_image", Final_image)  
    #time.sleep(0.02)
    
    # 如果按下'q'键退出循环  
    key = cv2.waitKey(20)  # 等待1毫秒，然后继续  
    if key == ord("q"):  
        break  
  
# closing the window  
cv2.destroyAllWindows()  
source.release()