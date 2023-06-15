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

## Endpoints

The API has only one endpoint:

### `/process` [POST]

Processes the uploaded image and returns the predicted food name, description, and restaurant information.

#### Request Parameters

| Parameter | Data Type | Description |
| --------- | ---------| ----------- |
| `img`     | File     | The image file to be processed. |

#### Response

If the image processing is successful, the API will return a JSON object containing the following information:

| Field Name      | Data Type | Description                            |
| ---------------|----------|----------------------------------------|
| `nama_makanan`  | String   | The name of the predicted dish.        |
| `deskripsi`     | String   | A brief description of the dish.       |
| `nama_restoran` | String   | The name of a restaurant serving the dish. |

If there is an error in processing the image, the API will return an error message.

## Model

The API uses a Tensorflow Lite classification model to predict the name of the dish from an image. The model has been trained on the following classes:

- Ayam Goreng
- Ayam Pop
- Daging Rendang
- Dendeng Batokok
- Gulai Ikan
- Gulai Tambusu
- Gulai Tunjang
- Telur Balado
- Telur Dadar

The model outputs a probability score for each class. The class with the highest probability score is taken as the predicted class.

## Data

The API returns a brief description of the dish and restaurant information from JSON files `deskripsi_makanan.json` and `restoran.json`. These files contain descriptions and restaurant names for each dish class used in the model.

## Credits

This API is built using an open source Tensorflow Lite classification model by [TensorFlow](https://www.tensorflow.org/lite/models/image_classification/overview). The developer of this API is Little B.

## Model Description
The model used in this API is a pre-trained TensorFlow Lite model for image classification. It has been trained on 9 different types of foods: Ayam Goreng, Ayam Pop, Daging Rendang, Dendeng Batokok, Gulai Ikan, Gulai Tambusu, Gulai Tunjang, Telur balado, and Telur dadar. The model takes an image as input and returns a list of probabilities for each class. The highest probability indicates the predicted class.

## Credits
This API has been developed using TensorFlow Lite and Keras by Little B.
