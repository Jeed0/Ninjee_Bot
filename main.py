import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv(dotenv_path="config.env")


class Ninjee(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=discord.Intents.all())

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur!")

    async def on_message(self, message):
        if message.content.startswith("bonjour"):
            await message.channel.send("Bonjour a toi!")

    async def on_member_join(self, member):
        self.general_channel: discord.TextChannel = Ninjee.get_channel(os.getenv("GENERAL"))
        print(f" toto {os.getenv('GENERAL')}")
        await self.general_channel.send(content=f"Bienvenue a toi, ceci est un texte personnalisé!! Le vois-tu {member.display_name}?")


Ninjee = Ninjee()
Ninjee.run(os.getenv("TOKEN"))
