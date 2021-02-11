import discord
import os
from keep_alive import keep_alive
from replit import db
import time
import settings

client = discord.Client()

startingMoney = settings.startingMoney
waitForYields = settings.waitForYields
priceIncreaseMultiplier = settings.priceIncreaseMultiplier
initialPrices = settings.initialPrices
yields = settings.yields
startingAccountMap = settings.startingAccountMap

if(not "bank accounts" in db.keys()):
  db["bank accounts"] = {}
if(not "last yields" in db.keys()):
  db["last yields"] = {}
print(db["bank accounts"])
print(db["last yields"])

def startAccountForUser(user):
  userText = str(user)
  accounts = db["bank accounts"]
  accounts[userText] = startingAccountMap()
  db["bank accounts"] = accounts

def showAccountToUser(user):
  userText = str(user)
  return(str(db["bank accounts"][userText]))

def getPricesForUser(user):
  userText = str(user)
  prices = initialPrices.copy()
  account = db["bank accounts"][userText]
  for commodity in prices:
    prices[commodity] = round(prices[commodity] * priceIncreaseMultiplier**account[commodity])
  return prices

def getYieldsForUser(user):
  return yields

def registerBuy(message, user):
  userText = str(user)
  parts = message.split(" ")
  amount = int(parts[1])
  commodity = parts[2]
  prices = getPricesForUser(user)
  #todo this calculation does not account for the increase of price after one buy
  if(commodity in prices and prices[commodity] * amount <= db["bank accounts"][userText]["money"]):
    accounts = db["bank accounts"]
    accounts[userText]["money"] -= prices[commodity] * amount
    accounts[userText][commodity] += amount
    db["bank accounts"] = accounts
    return True
  else:
    return False

def collectYields(user):
  userText = str(user)
  account = db["bank accounts"][userText]
  total = 0
  for commodity in account:
    if(commodity == "money"):
      continue
    count = account[commodity]
    yieldPerCommodity = yields[commodity]
    total += count * yieldPerCommodity
  accounts = db["bank accounts"]
  accounts[userText]["money"] += total
  db["bank accounts"] = accounts
  return total
  
def timeForCollecting(user):
  userText = str(user)
  if(not userText in db["last yields"]):
    yieldsDB = db["last yields"]
    yieldsDB[userText] = time.time()
    db["last yields"] = yieldsDB
    return True
  else:
    if(time.time() - db["last yields"][userText] >= waitForYields):
      yieldsDB = db["last yields"]
      yieldsDB[userText] = time.time()
      db["last yields"] = yieldsDB
      return True
    else:
      return False

def findTimeToYield(user):
  userText = str(user)
  return (waitForYields - time.time() + db["last yields"][userText])

@client.event
async def on_ready():
  print(f"Logged in as : {client.user}")

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  msg = message.content
  if(msg.startswith("$hello")):
    await message.channel.send("Hello")
  elif(msg.startswith("$start account")):
    startAccountForUser(message.author)
    await message.channel.send("Created account")
  elif(msg.startswith("$show account")):
    reply = showAccountToUser(message.author)
    await message.channel.send(reply)
  elif(msg.startswith("$show prices")):
    reply = getPricesForUser(message.author)
    await message.channel.send(reply)
  elif(msg.startswith("$show yields")):
    reply = getYieldsForUser(message.author)
    await message.channel.send(reply)
  elif(msg.startswith("$buy")):
    ableToBuy = registerBuy(msg, message.author)
    if(ableToBuy):
      await message.channel.send("Bought successfully :)")
    else:
      await message.channel.send("Could not buy it :(")
  elif(msg.startswith("$collect yields")):
    reqTimeInMinutes = round(findTimeToYield(message.author) / 60)
    if(timeForCollecting(message.author)):
      earnings = collectYields(message.author)
      await message.channel.send(f"Collected: {earnings}$")
    else:
      await message.channel.send(f"You have to wait {reqTimeInMinutes} minutes.")


keep_alive()
client.run(os.getenv("TOKEN"))