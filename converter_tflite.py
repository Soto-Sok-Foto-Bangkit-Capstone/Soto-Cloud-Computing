import tensorflow as tf
from keras.models import load_model

import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

model = load_model("my_model.h5", compile=False)
model.compile(
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.0005),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()

with open("model.tflite", "wb") as f:
    f.write(tflite_quant_model)