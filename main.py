# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_render_template]
# [START gae_python3_render_template]
import datetime

from flask import Flask, render_template, request

from keras.models import load_model
import numpy as np

import tensorflow as tf

import json

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

class TensorflowLiteClassificationModel:
    def __init__(self, model_path, labels, image_size=224):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self._input_details = self.interpreter.get_input_details()
        self._output_details = self.interpreter.get_output_details()
        self.labels = labels
        self.image_size=image_size

    def run_from_filepath(self, image_path):
        img = tf.keras.utils.load_img(image_path, target_size=(224, 224))
        img = img.convert("RGB")
        x = tf.keras.utils.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        image = tf.keras.applications.mobilenet_v2.preprocess_input(x)

        return self.run(image)

    def run(self, image):
        """
        args:
          image: a (1, image_size, image_size, 3) np.array

        Returns list of [Label, Probability], of type List<str, float>
        """

        self.interpreter.set_tensor(self._input_details[0]["index"], image)
        self.interpreter.invoke()
        tflite_interpreter_output = self.interpreter.get_tensor(self._output_details[0]["index"])
        probabilities = np.array(tflite_interpreter_output[0])

        # create list of ["label", probability], ordered descending probability
        label_to_probabilities = []
        for i, probability in enumerate(probabilities):
            label_to_probabilities.append([self.labels[i], float(probability)])
        return probabilities

labels = ["Ayam Goreng", "Ayam Pop", "Daging Rendang", "Dendeng Batokok", "Gulai Ikan", "Gulai Tambusu", "Gulai Tunjang", "Telur balado", "Telur dadar"]

# Process image and predict label
def processImg(IMG_PATH):
    model = TensorflowLiteClassificationModel("model.tflite",labels )
    classes = model.run_from_filepath(IMG_PATH)

    highest_score_index = np.argmax(classes)
    highest_score = classes[highest_score_index]
    highest_score_label = labels[highest_score_index]

    # Untuk deskripsi makanan
    f_deskripsi = open('deskripsi_makanan.json')
    f_restoran = open('restoran.json')

    deskripsi = json.load(f_deskripsi)
    restoran = json.load(f_restoran)

    hasil_prediksi = {"nama_makanan" : highest_score_label,
                      "deskripsi" : deskripsi[highest_score_label],
                      "nama_restoran" : restoran[highest_score_label]}

    print(classes)
    print("Highest Score:", highest_score)
    print("Highest Score Label:", highest_score_label)

    return (hasil_prediksi)


app = Flask(__name__)


@app.route('/')
def root():
    return """
        API Prediksi Nama Makanan dari Foto
    """

# Process images
@app.route("/process", methods=["POST"])
def processReq():

    data = request.files["img"]
    data.save("img.jpg")

    resp = processImg("img.jpg")
    return resp


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
