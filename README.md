# YOLOv8-Custom-Object-Detection

1 Step: First Step is to create the folder and install the libraries
	pip install ultralytics
	pip install OpenCV

2 Step: After creating the env, open Labelimg or Roboflow for data annotation. 

3 Step: After completing the data annotation task. After this create 3 folders. 
						   1- Train (in that create 2 folders as Images and labels) upload the images with its label file to train the model.
			     			   2- Test (Testing data)
			    			   3- Validation (in that create 2 folders as Images and labels) upload the images with its label file from validation of the model.

4 Step: Paste the images to train folder where we have to separate the image and the xml file to Images and Label folder respectively.

5 Step: Open CMD, activate the env, then add the code.

CODE FOR THE TESTING OUT THE MODEL IS:

#train
yolo task=detect mode=train model=yolov8n.pt data="D:\\your\\file_location\\data.yaml" epochs=10 imgsz=640

#validation
yolo task=detect mode=val model="D:\\yolov8\\runs\\detect\\train\\weights\\best.pt" data="D:\\your\\file_location\\data.yaml"

Now open the py file and upload the test video to detect.




https://github.com/user-attachments/assets/b52f843d-c237-4b09-9f1b-cfe2d0dcdfd2



IF YOU WANT TO SIMPLY JUST DETECT THE OBJECT USING " yolov8n.pt " 

USE THIS CODE: 

from ultralytics import solutions

# Pass a model as an argument
solutions.inference(model="yolov8n.pt")

### Make sure to run the file using command `streamlit run <file-name.py>`
