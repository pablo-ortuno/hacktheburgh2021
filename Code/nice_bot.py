import discord
from discord.ext import commands
import random

token = 'ODE4MDU1MDE2OTg3NjIzNDI0.YESfGg.2nbRyQZIqr4KXq2e9cJQI-rLe4s'

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print("Bot is ready")
    print("-----------------------------")

@client.event
async def on_member_join():
    await ctx.send("Hey! Welcome to the channel")
    await ctx.send("Send a picture of your setup with the caption $rate and I'll rate it")

@client.command()
async def rate(ctx):
        score = random.randint(50,100)
        await ctx.send('This setup has a score of ' + str(score))

client.run(token)
