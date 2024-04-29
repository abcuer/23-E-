import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt

def Edge_Detection(image_path, threshold1=200, threshold2=250):
    img = cv.imread(image_path, 0)
    dst = cv.GaussianBlur(img, (17, 17), 0)

    # Canny 边缘检测
    edges = cv.Canny(img, threshold1, threshold2)

    # 找到所有非零像素点的坐标
    indices = np.where(edges != 0)
    edge_points = np.column_stack((indices[1], indices[0]))  # 每行代表一个边缘点的坐标 (x, y)

    # 打印边缘点的坐标
    for point in edge_points:
        print(f"Edge point: ({point[0]}, {point[1]})")

    # 保存坐标到文件
    np.savetxt('edge_points.txt', edge_points, fmt='%d')

    # plt.imshow(edges, cmap='gray')
    # plt.title('Edge_image'), plt.xticks([]), plt.yticks([])
    # plt.show()
    cv.imshow('Detected Colors', edges)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 测试封装的函数
Edge_Detection('week_9/src_1/img_1.jpeg')
