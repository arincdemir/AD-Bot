  
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
  if(msg.startswith('sa ')):
    await message.channel.send('as')
  if msg.startswith('?play orekto'):
    await message.channel.send('███░███░███░███░░███░█░█░████\n█░░░█░░░█░█░█░░█░█░░░█░█░░░█░\n███░███░█░█░███░░███░█░█░░█░░\n█░░░█░░░█░█░█░░█░░░█░█░█░█░░░\n███░█░░░███░█░░█░███░███░████')
  if(msg.startswith("-p ") or msg.startswith("-play ")):
    await message.channel.send("playsene lan")


#____________________dick part____________________#
  if(msg.startswith("dick size")):
    if(message.author.name == "Mustafa Dinç"):
      await message.channel.send("you should have a dick :(")
    elif(message.author.name == "Ömer Takkin"):
      await message.channel.send("oha!!!\n◯ ----------------------------------------\\ \n◯ ----------------------------------------/ ")
    elif(message.author.name == "serhatekli"):
      await message.channel.send("3")
    elif(message.author.name == "arincdemir"):
      await message.channel.send("8=====================================================>")
    else:
      dickSize=round(random.random()*20)
      dick = "8"
      while(dickSize!=0):
        dick += "="
        dickSize -= 1 
      dick += ">"
      await message.channel.send(dick)

#____________________finger game____________________#

  if(msg.startswith("finger game")):
    await message.channel.send("Parmak oyununa hoşgeldiniz, örnek hamle: 12 -> senin sol elin onun sağ eline vurucak (1=sol, 2=sağ)")
    P1_H1 = 1
    P1_H2 = 1
    P2_H1 = 1
    P2_H2 = 1  # we defined finger numbers of players
    gameStatus = 0  # 0: bitmedi , 1: sol kazandı 2: sağ kazandı

    while(gameStatus == 0):
        await message.channel.send("P1: " + str(P1_H1) + "   " + str(P1_H2) + "           " + "P2: " + str(P2_H1) + "   " + str(P2_H2))
        await message.channel.send("P1 hamleni yap krdşm")

        if(msg.startswith("11") and P1_H1!=0): #!!! arınç burada mesaj alma şeklimin işe yarıyacağına emin değilim
            P2_H1 += P1_H1
        elif(msg.startswith("12") and P1_H1!=0):
            P2_H2 += P1_H1
        elif(msg.startswith("21") and P1_H2!=0):
            P2_H1 += P1_H2
        elif(msg.startswith("22") and P1_H2!=0):
            P2_H2 += P1_H2
        else:
            await message.channel.send("yanlış hamle! hamlen gege. xd")

        if(P2_H1 >= 5):
            P2_H1 -= 5
        if(P2_H2 >= 5):
            P2_H2 -= 5
        
        if(P2_H1+P2_H2==0):
            gameStatus=1
            break
            

        await message.channel.send("P1: " + str(P1_H1) + "   " + str(P1_H2) + "           " + "P2: " + str(P2_H1) + "   " + str(P2_H2))
        await message.channel.send("P2 hamleni yap krdşm")

        if(msg.startswith("11") and P2_H1!=0):
            P1_H1 += P2_H1
        elif(msg.startswith("12") and P2_H1!=0):
            P1_H2 += P2_H1
        elif(msg.startswith("21") and P2_H2!=0):
            P1_H1 += P2_H2
        elif(msg.startswith("22") and P2_H2!=0):
            P1_H2 += P2_H2
        else:
            await message.channel.send("yanlış hamle! hamlen gege. xd")

        if(P1_H1 >= 5):
            P1_H1 -= 5
        if(P1_H2 >= 5):
            P1_H2 -= 5

        if(P1_H1+P1_H2==0):
            gameStatus=2
            break


    if(gameStatus==1):
        await message.channel.send("P1 sapladı. Eforsuz bir oyundu.")
    if(gameStatus==2):
        await message.channel.send("P2 sapladı. Eforsuz bir oyundu.")
#____________________end of finger part____________________#








        

    



    
  

keep_alive()
client.run(os.getenv("TOKEN"))