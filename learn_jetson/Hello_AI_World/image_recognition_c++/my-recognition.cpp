#include <jetson-inference/imageNet.h>  //识别
#include <jetson-utils/loadImage.h>     //加载

int main(int argc, char** argv)
{
    if(argc < 2){
        printf("my-recognition: expected imae filename as argument\n");
        printf("example usage: ./my-cognition my_image.jpg\n");
        return 0;
    }

    // 从命令行参数中找回文件名
    const char* imgFilename = argv[1];

    // 声明变量存储图像数据指针和尺寸
    uchar3* imgPtr = NULL;  // 共享cpu和gpu的指针
    int imgWidth = 0;       // 图像宽，像素
    int imgHeight = 0;      // 图像高，像素

    // 从硬盘加载图像
    if(!loadImage(imgFilename, &imgPtr, &imgWidth, &imgHeight)){
        printf("failed to load image '%s'\n", imgFilename);
        return 0;
    }

    // 用tensorrt加载googlenet识别网络
    imageNet * net = imageNet::Create(imageNet::GOOGLENET);

    // 检查网络模型被正确加载
    if(!net){
        printf("failed to load image recognition network\n");
        return 0;
    }

    // 存储分类置信度
    float confidence = 0.0;
    // 图像分类，返回对象索引
    const int classIndex = net->Classify(imgPtr, imgWidth, imgHeight, &confidence);

    // 解释结果
    if(classIndex >= 0){
        // 召回对象索引的名字/描述
        const char * classDescription = net->GetClassDesc(classIndex);
        // 打印分类结果
        printf("image is recognized as '%s' (class$%i) with %f%% confidence\n",
                classDescription, classIndex, confidence*100.0f);
    }
    else{
        // 分类错误
        printf("failed to classify image\n");
    }

    // free network
    delete net;
    return 0;
} 