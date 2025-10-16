from discord.ext import commands
from termcolor import colored
import discord
import random
import json

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

mason = commands.Bot(command_prefix='?67?', intents=intents)

Mason67_1 = "/assets/1.jpeg"
Mason67_2 = "/assets/2.jpeg"
Mason67_3 = "/assets/3.jpeg"
Mason67_4 = "/assets/4.jpeg"
pic = None

Mason67_txt_1 = "67?!"
Mason67_txt_2 = "Six Seven!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
Mason67_txt_3 = "6-7!!!!!!!!!!!!!!!!"
Mason67_txt_4 = "67 Mason"
msg = None

rng = random.randint(1, 12)
if rng in [6, 2, 9]:
  pic = Mason67_1
  msg = Mason67_txt_1
elif rng in [1, 5, 11]:
  pic = Mason67_2
  msg = Mason67_txt_2
elif rng in [3, 12, 7]:
  pic = Mason67_3
  msg = Mason67_txt_3
elif rng in [4, 8, 10]:
  pic = Mason67_4
  msg = Mason67_txt_4

@bot.event
async def start():
  print(colored("Mason has arisen.", "green", attrs=["bold"]))
                      
@client.event
async def onmsg(msg):
  if msg.author == client.user:
    return
  if msg.content in ["67", "6-7", "Six Seven".lower()]:
    img = discord.File(pic)
    await = ctx.send(file=img)
    await message.channel.send(msg)

with open("config.json", "r") as r:
  read = json.load(r)
  
mason.run(read["token"])
