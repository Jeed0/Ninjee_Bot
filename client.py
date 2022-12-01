import os
import discord

from dotenv import load_dotenv
load_dotenv(dotenv_path="config.env")

default_intents = discord.Intents.all()
default_intents.members = True

client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Ninjee est en ligne!!")

@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("Pong!", delete_after=5)

@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(
        "GENERAL")
    await general_channel.send(content=f"Bienvenue a toi, ceci est un texte personnalisé!! Le vois-tu {member.display_name}?")

@client.event
async def on_message(message):
    if message.content.startswith("bonjour"):
        await message.channel.send("Bonjour a toi!")

client.run(os.getenv("TOKEN"))
