import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

BATCH_SIZE = 32
IMAGE_SIZE1 = 256
IMAGE_SIZE2 = 256
CHANNELS=3
EPOCHS=50

dataset = tf.keras.preprocessing.image_dataset_from_directory(
    "C:\\Users\\Admin\\Downloads\\project things\\Diseases\\Training",
    seed=123,
    shuffle=True,
    image_size=(IMAGE_SIZE1,IMAGE_SIZE2),
    batch_size=BATCH_SIZE
)

class_names = dataset.class_names

def predict(model, img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    plt.imshow(img)
    return predicted_class, confidence
