import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config.env")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Ninjee est en ligne!!")

@bot.command(pass_context=True, name='del')
async def delete(ctx, number_of_messages: int):
    messages = [message async for message in ctx.channel.history(limit=number_of_messages + 1)]
    # deprecated  -> messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()
    for each_message in messages:
        await each_message.delete()

bot.run(os.getenv("TOKEN"))