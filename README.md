# Cloud-Computing
# API 

## Introduction
This is an image classification API that predicts the name of the food in the provided image. The API utilizes TensorFlow Lite to run a pre-trained model for image classification. The model has been trained on 9 different types of foods: Ayam Goreng, Ayam Pop, Daging Rendang, Dendeng Batokok, Gulai Ikan, Gulai Tambusu, Gulai Tunjang, Telur balado, and Telur dadar.

## Requirements
1. Python 3.x
2. Flask
3. TensorFlow Lite
4. Keras
5. Numpy

## Installation
1. Install Python 3.x from [here](https://www.python.org/downloads/).
2. Install the required libraries using the command below:
```
pip install -r requirements.txt
```
3. Clone this repository or download the files.
4. Navigate to the cloned/downloaded directory and run the following command to start the server:
```
python app.py
```

## Usage
1. Start the server by running `python app.py` command.
2. Send a POST request to `http://localhost:8080/process` with an image file attached as 'img' parameter in the request body.
For example, using cURL:
```
curl -X POST -F "img=@/path/to/image.jpg" http://localhost:8080/process
```
3. The server will respond with a JSON object containing the predicted name of the food, its description, and the name of the restaurant that serves it.

## Model Description
The model used in this API is a pre-trained TensorFlow Lite model for image classification. It has been trained on 9 different types of foods: Ayam Goreng, Ayam Pop, Daging Rendang, Dendeng Batokok, Gulai Ikan, Gulai Tambusu, Gulai Tunjang, Telur balado, and Telur dadar. The model takes an image as input and returns a list of probabilities for each class. The highest probability indicates the predicted class.

## Credits
This API has been developed using TensorFlow Lite and Keras by Little B.
