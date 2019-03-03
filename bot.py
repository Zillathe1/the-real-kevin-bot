import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import requests
import os
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content.upper().startswith("!MEMES"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Would you like !Deepfried , !Dank , !Video ?" % (userID)) #responds with oof
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.upper().startswith('!DEEPFRIED'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> https://i.redd.it/40cr1aghvkj21.jpg" % (userID))

    if message.content.upper().startswith('!DANK'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> https://i.redd.it/wei2bi7lnjj21.png" % (userID))

    if message.content.upper().startswith('!MAKEMECRINGE'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> UWU *snuggles* u so warm" % (userID))

    if message.content.upper().startswith('!VIDEO'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> https://www.youtube.com/watch?v=6nAiCldUdBM WARNING EARRAPE" % (userID))

    if message.content.upper().startswith('!IAMTHEOWNER'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> I am kevin, also no your not, unless you are idk ¯\_(ツ)_/¯" % (userID))

    if message.content.upper().startswith('!UGANDAKNUCKLES'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Congrats, you found the easter egg, DM the server owner, ( @Zllathe1 ) with the easter egg for your prize." % (userID))

    if message.content.upper().startswith('!OOF'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> https://www.youtube.com/watch?v=f49ELvryhao." % (userID))

    if message.content.upper().startswith('!SHOW MEGODSFINESTWORK'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> https://www.coolmathgames.com/." % (userID))

    if message.content.upper().startswith('!SHOWMEGOD'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> https://pm1.narvii.com/7038/333c526fa54e7e52d00a6f870976bd2c1970cabar1-1200-675v2_hq.jpg" % (userID))

    if message.content.upper().startswith('!BRUH'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> https://media.giphy.com/media/VIOkcgpsnA2Zy/giphy.gif" % (userID))

    if message.content.upper().startswith('!SHAGGY'): #if user types
        userID = message.author.id #user id
        await client.send_message(message.channel, "<@%s> https://thumbs.gfycat.com/EvenActiveJellyfish-size_restricted.gif" % (userID)) #bot sends/ send to

    if message.content.upper().startswith('!PACERTEST'): #if user types
        userID = message.author.id #user id
        await client.send_message(message.channel, "<@%s> The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.!" % (userID)) #bot sends/ send to

    if message.content.upper().startswith('!TELLMEAJOKE'): #if user types
        userID = message.author.id #user id
        await client.send_message(message.channel, "<@%s> You" % (userID)) #bot sends/ send to

        
        
        
client.run(str(os.environ.get("NTUwNDU1ODgxMDYyNTQ3NDg2.D1tgPg.WtBknfvJnjyZYJb5MC8egdUPZgI"))) #bots token/ password thing
