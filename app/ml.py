import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

BATCH_SIZE = 32
IMAGE_SIZE = 256

dataset = tf.keras.preprocessing.image_dataset_from_directory(
    "C:\\Users\\Admin\\Desktop\\skin_dataset",
    seed=123,
    shuffle=True,
    image_size=(IMAGE_SIZE,IMAGE_SIZE),
    batch_size=BATCH_SIZE
)

class_names = dataset.class_names

def predict(model, img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence
