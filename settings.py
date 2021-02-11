startingMoney = 100
waitForYields = 5 * 60
priceIncreaseMultiplier = 1.1
initialPrices = {"selpak": 25,
"cam_silecegi": 200,
"cop_toplama_arabasi": 1000,
"motorlu_cop_toplama_arabasi": 5000,
"midye_tablası": 20000,
"tavuk_dönerci": 100000
}

yields = {"selpak": 10,
"cam_silecegi": 80,
"cop_toplama_arabasi": 400,
"motorlu_cop_toplama_arabasi": 2000,
"midye_tablası": 8000,
"tavuk_dönerci": 40000
}

def startingAccountMap():
  return {"money": startingMoney,
"selpak": 0,
"cam_silecegi": 0,
"cop_toplama_arabasi": 0,
"motorlu_cop_toplama_arabasi": 0,
"midye_tablası": 0,
"tavuk_dönerci": 0
}