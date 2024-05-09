# opencv 读取视频流并显示

import cv2

cap = cv2.VideoCapture(0)

while(1):
    # 读取一帧
    ret, frame = cap.read()
    # 显示
    cv2.imshow('frame',frame)
    # 按q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break