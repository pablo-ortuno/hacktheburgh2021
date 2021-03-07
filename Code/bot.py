import discord
from discord.ext import commands
import numpy as np
import re
import tensorflow as tf
from tensorflow import keras

# Define the image seize and model to use for classification
img_height = 180
img_width = 180
model = keras.models.load_model('model')

# Bot Token - "ID of the bot"
token = 'ODE3OTM4MDQ3ODExMzIxODU3.YEQyKw.4ugeSWZtDb5XWrIeBbOFdBfL_Rw'
# Bot's client
client = commands.Bot(command_prefix = '!')
# Just so I know the bot is running
@client.event
async def on_ready():
    print("Bot is ready")
    print("-----------------------------")
# Some interaction
@client.event
async def on_member_join():
    await ctx.send("Hey, I'm the Setup Bot. Send a picture of your computer setup captioned !Setup and I'll rate it!")
# Main chunk of code
@client.command()
async def rate(ctx, *, setup):
    text = str(message.attachments[0]) #Pull out the attachment description
    m = re.search('url=(.+?).png', text) # Identify the URL for the image
    if m:
        url = str(m.group(1) + '.png')
        url = url[1:] #Modify and slice to get a working url

        path = tf.keras.utils.get_file(image_count, origin=url) #Downloads an image to the cache with the defined url
        img = keras.preprocessing.image.load_img(
            path, target_size=(img_height, img_width))
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) # Data normalization
        predictions = model.Predict(img_array) # Predict on the image
        score = tf.nn.softmax(predictions[0]) # Exctract the score

        await ctx.send('This setup has a score of {}'.format(100 * np.max(score)))
        # Finally, print the score
client.run(token)
