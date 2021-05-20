import discord
import os
from keep_alive import keep_alive
from replit import db
import time
import settings

client = discord.Client()



@client.event
async def on_ready():
  print(f"Logged in as : {client.user}")

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  msg = message.content
  if(msg.startswith("-p ")):
    await message.channel.send("playlesene lan")
  


keep_alive()
client.run(os.getenv("TOKEN"))