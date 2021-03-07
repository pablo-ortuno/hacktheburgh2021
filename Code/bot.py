import discord
from discord.ext import commands
import numpy as np
import re
import tensorflow as tf
from tensorflow import keras

img_height = 180
img_width = 180
model = keras.models.load_model('model')

image_count = 1

token = 'ODE3OTM4MDQ3ODExMzIxODU3.YEQyKw.SXkfJRC8XGkrnxPKiipgFF5mfAQ'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is ready")
    print("-----------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Fuck you")

@client.event
async def on_message(message):
    if message.content.startswith('$rate'):
        channel = message.channel
        text = str(message.attachments[0])
        m = re.search('url=(.+?).png', text)
        if m:
            url = str(m.group(1) + '.png')
            url = url[1:]

            path = tf.keras.utils.get_file(image_count, origin=url)
            img = keras.preprocessing.image.load_img(
                path, target_size=(img_height, img_width)
            )
            img_array = keras.preprocessing.image.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0) # Create a batch
            predictions = predict_(img_array)
            score = tf.nn.softmax(predictions[0])

            await channel.send('This setup has a score of {}'.format(100 * np.max(score)))
            image_count += 1

client.run(token)
