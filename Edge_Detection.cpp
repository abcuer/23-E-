#include <opencv2/opencv.hpp>
#include <iostream>

cv::Mat preprocessImage(const cv::Mat& image) {
    cv::Mat denoisedImage;
    cv::fastNlMeansDenoisingColored(image, denoisedImage, 10, 10, 7, 21);
    cv::Mat enhancedImage;
    cv::convertScaleAbs(denoisedImage, enhancedImage, 1, 30);
    cv::Mat cannyImage;
    cv::Canny(enhancedImage, cannyImage, 50, 150);
    return cannyImage;
}

std::vector<std::vector<cv::Point>> detectQuadrilaterals(const cv::Mat& image) {
    std::vector<std::vector<cv::Point>> contours;
    std::vector<cv::Vec4i> hierarchy;
    cv::findContours(image, contours, hierarchy, cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE);
    std::vector<std::vector<cv::Point>> quadrilaterals;
    for (const auto& contour : contours) {
        double area = cv::contourArea(contour);
        if (area > 2000) {
            std::vector<cv::Point> approx;
            cv::approxPolyDP(contour, approx, 0.01 * cv::arcLength(contour, true), true);
            if (approx.size() == 4) {
                quadrilaterals.push_back(approx);
            }
        }
    }
    return quadrilaterals;
}

cv::Mat drawPoints(cv::Mat image, const std::vector<std::vector<cv::Point>>& quadrilaterals) {
    cv::Mat annotatedImage = image.clone();
    for (const auto& quad : quadrilaterals) {
        cv::drawContours(annotatedImage, quad, -1, cv::Scalar(255, 0, 0), 2);
        for (int i = 0; i < quad.size(); ++i) {
            cv::circle(annotatedImage, quad[i], 5, cv::Scalar(0, 0, 255), -1);
            std::cout << "角点" << i + 1 << " 坐标: (" << quad[i].x << ", " << quad[i].y << ")" << std::endl;
        }
        cv::Moments M = cv::moments(quad);
        if (M.m00 != 0) {
            int cx = static_cast<int>(M.m10 / M.m00);
            int cy = static_cast<int>(M.m01 / M.m00);
            cv::circle(annotatedImage, cv::Point(cx, cy), 5, cv::Scalar(0, 0, 255), -1);
            std::cout << "中点 坐标: (" << cx << ", " << cy << ")" << std::endl;
        }
    }
    return annotatedImage;
}

int main(int argc, char** argv) {
    cv::Mat image = cv::imread("week_9/src/img_1.jpeg");
    if (image.empty()) {
        std::cerr << "无法读取图像文件!" << std::endl;
        return -1;
    }

    cv::Mat processedImage = preprocessImage(image);
    std::vector<std::vector<cv::Point>> quadrilaterals = detectQuadrilaterals(processedImage);
    cv::Mat annotatedImage = drawPoints(image, quadrilaterals);

    cv::namedWindow("Annotated Image", cv::WINDOW_NORMAL);
    cv::imshow("Annotated Image", annotatedImage);
    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}