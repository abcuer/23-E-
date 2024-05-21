#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char** argv) {
    // 检查命令行参数
    if (argc != 2) {
        std::cerr << "Usage: display_image <image_path>" << std::endl;
        return -1;
    }

    // 读取图像
    cv::Mat image = cv::imread(argv[1], cv::IMREAD_COLOR);
    if (image.empty()) {
        std::cerr << "无法打开或读取图像!" << std::endl;
        return -1;
    }

    // 显示图像
    cv::namedWindow("Image", cv::WINDOW_NORMAL);
    cv::imshow("Image", image);

    // 等待用户按键，然后关闭窗口
    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}