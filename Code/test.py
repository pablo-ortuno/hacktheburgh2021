import numpy as np
import os
import PIL
import tensorflow as tf
from tensorflow import keras

img_height = 180
img_width = 180

print("Hello")
model = keras.models.load_model('model')
print("World")

sunflower_path = r'C:\Users\pablo\github\ideatron3000\Data_tests\Image.jpeg'

img = keras.preprocessing.image.load_img(
    sunflower_path, target_size=(img_height, img_width)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(predictions)

print('Your setup has a score of {}'.format(100 * np.max(score)))




sunflower_path = tf.keras.utils.get_file('Red_sunflower', origin=url)
img = keras.preprocessing.image.load_img(
    sunflower_path, target_size=(img_height, img_width)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch
predictions = predict_(img_array)
score = tf.nn.softmax(predictions[0])

await channel.send('This setup has a score of {}'.format(100 * np.max(score)))
