import tensorflow as tf
from tensorflow import keras
import numpy as np

img_height = 180
img_width = 180
model = keras.models.load_model('model')

 #Downloads an image to the cache with the defined url
path = "Data_tests\Image.jpeg"

img = keras.preprocessing.image.load_img(path, target_size=(img_height, img_width))
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Data normalization
predictions = model.predict(img_array) # Predict on the image
score = tf.nn.softmax(predictions[0]) # Exctract the score

print('This setup has a score of {}'.format(100 * np.max(score)))
