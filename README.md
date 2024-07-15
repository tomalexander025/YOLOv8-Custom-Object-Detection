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

#prediction
yolo task=predict mode=val conf=0.25 model="D:\\yolov8\\runs\\detect\\train\\weights\\best.pt" source="D:\\your\\images\\source\\location"
