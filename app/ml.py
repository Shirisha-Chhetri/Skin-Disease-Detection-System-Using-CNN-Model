import tensorflow as tf
from tensorflow.keras import models, layers
import matplotlib.pyplot as plt
from .models import UserUploadedImage

BATCH_SIZE = 32
IMAGE_SIZE = 256
CHANNELS=3
EPOCHS=50

def get_recommendation_for_book(image_id):
    dataset = tf.keras.preprocessing.image_dataset_from_directory(
    "Training",
    seed=123,
    shuffle=True,
    image_size=(IMAGE_SIZE,IMAGE_SIZE),
    batch_size=BATCH_SIZE

    class_names = dataset.class_names
    
)