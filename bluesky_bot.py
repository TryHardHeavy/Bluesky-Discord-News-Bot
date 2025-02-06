#!/bin/python3

import os
import discord
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_API_TOKEN')
print(DISCORD_TOKEN)

class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        for guild in self.guilds:
           for channel in guild.text_channels:
              if "save-this" in channel.name:
                  self.channel_id = channel.id
        print(self.channel_id)
    
    
    
intents = discord.Intents.all()
intents.message_content = True

client = Client(intents=intents)
client.run(token=DISCORD_TOKEN)
