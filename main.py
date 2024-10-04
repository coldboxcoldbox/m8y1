import os
import discord
import random
from discord.ext import commands
from model import derevo

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description="ботяра", intents=intents)
@bot.command()
async def a(ctx):
    await ctx.send(f"Бот в сети")
@bot.command()
async def image_save(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"изображение сохранено: ./{attachment.filename}")
            name = derevo(f"./{attachment.filename}")
            await ctx.send("Этот лист принадлежит дереву...")
            link = "https://en.wikipedia.org/wiki/" + name
            await ctx.send(link)
            a = random.randint(1,3)
            if a == 1:
                await ctx.send("А вы знали что целые леса исчезают от вырубок лесов?")
            if a == 2:
                await ctx.send("А вы знали что в океанах от мусора страдают сотни морских существ?")
            if a == 3:
                await ctx.send("А вы знали что загрязнение воздуха сокращает жизнь на 15 лет?")
                 
    else:
        print("изображений не найдено")
bot.run("token")
