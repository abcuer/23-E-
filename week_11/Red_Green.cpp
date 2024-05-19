#include <iostream>
#include <opencv2/opencv.hpp> // 导入OpenCV库
using namespace std;
int main()
{

    cv::Mat image = cv::imread("src/img_1.jpeg");

    // 检查图像是否成功加载
    if (image.empty()) {
        std::cerr << "Error: Could not read image file" << std::endl;
        return 1;
    }

    // 显示图像
    cv::imshow("Image", image);
    cv::waitKey(0);
    // cv::imwrite("out/img_1_red.jpeg", image);

    return 0;
}

