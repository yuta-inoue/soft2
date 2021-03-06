#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;

int main(int argc, char* argv[])
{
	VideoCapture cap(0);
	if(!cap.isOpened())return -1;
	namedWindow("window1",1);
	CascadeClassifier cascade;			// カスケード分類器の取得
  string path = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml";
	if(!cascade.load(path))
		return -1;

	// カスケード分類器で顔の探索
	Mat frame;
	vector<Rect> faces;
	while(true){
		Mat input_image;
		cap >> frame;
		cvtColor(frame,input_image,CV_BGR2GRAY);
		equalizeHist(input_image,input_image);
		cascade.detectMultiScale(input_image,faces,1.3,2,CV_HAAR_SCALE_IMAGE,Size(50,50));
		vector<Rect>::const_iterator r = faces.begin();
		for(;r!=faces.end();++r){
			rectangle(frame,Point(r->x,r->y),Point(r->x+r->width,r->y+r->height),Scalar(0,0,200),3,1);
		}
		imshow("window1",frame);
		waitKey(0);						/* 入力待機 */
			return 0;
	}
}                                                                                                                                                                                                                                                                                                                                                                                                                         
