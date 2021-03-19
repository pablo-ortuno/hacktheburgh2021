# The Nice Setup Bot
(Originally the ideatron3000)

## Goal
To create a discord bot which takes images of user's computer setups and returns a score. To do this I created a working model and then tried to implement it in Discord as a bot  

#### 1 - Model
For the model I used a total of 720 images scraped from the web. 400 images were given as setups and 320 images were given as not setups. It was split with 80 images each from google searchs:
  - computer desk setup
  - computer gaming setup
  - computer setup for programming
  - desk with two monitors
  - home office setup

  - office cubicles
  - open office space
  - music setup
  - work meeting

After doing some data processing I fitted the model using a 80/20 percent split in training and testing data. The results were not great and there are signs of overfitting. Probably due to the small amount of data used.

#### 2 - Implementation in Discord
To implement it in Discord I created a Discord bot and linked it to a dedicated server. Inside the bot, I ran a function that looked for images which caption started with "$rate". Then, it extracted the image as a url (default Discord method) and attempted to download it in order to test it against the model.
Thus, if we sent a picture to the server captioned "$rate my setup"

#### 3 - Issues
Once the bot had extracted the URL from the image, it attempted to download it. However, it was unable to due to some protection on the image and a lack of permissions. I could not find a solution to this.

#### 4 - Resolve
I then took my project in a different direction, and created a "Nice Setup Bot", where users still send a picture of their setups captioned with "$rate" and the bot returns a score for it. In this case, the bot doesn't bother looking at the image and just spits out a random number between 50 and 100, because all setups are nice and lovely, but some are objectively better than others
