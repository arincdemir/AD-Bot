  
import discord
import os
from keep_alive import keep_alive
from replit import db
import time
import settings
import random

client = discord.Client()



@client.event
async def on_ready():
  print(f"Logged in as : {client.user}")

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  msg = message.content
  if(msg.startswith('?play ege')):
    await message.channel.send('İşten yeni çıktım arkadaşlar kendimi gangıster gibi hissediyorum')
  if(msg.startswith('sa')):
    await message.channel.send('as')
  if msg.startswith('?play orekto'):
    await message.channel.send('███░███░███░███░░███░█░█░████\n█░░░█░░░█░█░█░░█░█░░░█░█░░░█░\n███░███░█░█░███░░███░█░█░░█░░\n█░░░█░░░█░█░█░░█░░░█░█░█░█░░░\n███░█░░░███░█░░█░███░███░████')
  if(msg.startswith("-p ") or msg.startswith("-play ")):
    await message.channel.send("playsene lan")


#____________________dick part____________________#
  if(msg.startswith("dick size")):
    if(message.author == "Pulsefire Musty"):
      await message.channel.send("you should have a dick :(")
    else:
      dickSize=round(random.random()*20)
      dick = "8"
      while(dickSize!=0):
        dick += "="
        dickSize -= 1 
      dick += ">"
      await message.channel.send(dick)
    



    
  

keep_alive()
client.run(os.getenv("TOKEN"))
