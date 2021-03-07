import discord
from discord.ext import commands
import random

token = 'ODE4MDU1MDE2OTg3NjIzNDI0.YESfGg.G6sPX67cYBcHke9JlIMLQJNnEcA'

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
        score = random.randint(0,100)

        await ctx.send('This setup has a score of ' + str(score))

        if score <= 40:
            await ctx.send('That is not a great setup is it mate')

client.run(token)
