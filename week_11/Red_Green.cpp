#include <opencv2/opencv.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <vector>

using namespace std;

// 定义颜色范围
struct ColorRange {
    cv::Scalar lower;
    cv::Scalar upper;
};

// 检测颜色并返回中心点
cv::Point2f detectColor(const cv::Mat& hsv, const ColorRange& color_range) {
    cv::Mat mask;
    cv::inRange(hsv, color_range.lower, color_range.upper, mask);

    vector<vector<cv::Point>> contours;
    cv::findContours(mask, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    cv::Point2f center(0, 0);
    if (!contours.empty()) {
        int max_area_idx = 0;
        double max_area = 0;
        for (size_t i = 0; i < contours.size(); ++i) {
            double area = cv::contourArea(contours[i]);
            if (area > max_area) {
                max_area = area;
                max_area_idx = i;
            }
        }

        if (max_area_idx >= 0) {
            const auto& contour = contours[max_area_idx];
            cv::Rect rect = cv::boundingRect(contour);
            center.x = rect.x + rect.width / 2.0;
            center.y = rect.y + rect.height / 2.0;
        }
    }

    return center;
}

// 绘制点
void drawPoints(cv::Mat& image, const cv::Point2f& center, const std::string& label) {
    cv::putText(image, label, center, cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(0, 0, 255), 2);
}

int main() {
    cv::Mat image = cv::imread("/home/nhmgs/cv2/week_11/src/img_3.jpeg");
    if (image.empty()) {
        cout << "未找到该图片" << endl;
        return -1;
    }

    cv::Mat hsv;
    cv::cvtColor(image, hsv, cv::COLOR_BGR2HSV);

    ColorRange green_range = {{36, 100, 100}, {86, 255, 255}};
    cv::Point2f green_center = detectColor(hsv, green_range);
    drawPoints(image, green_center, "Green point");

    ColorRange red_range = {{165, 100, 100}, {179, 255, 255}};
    cv::Point2f red_center = detectColor(hsv, red_range);
    drawPoints(image, red_center, "Red point");

    cv::namedWindow("image", cv::WINDOW_NORMAL);
    cv::imshow("image", image);
    // cv::waitKey(0);
    // cv::destroyAllWindows();

    return 0;
}