import random
import discord
import os
import requests
from discord.ext import commands

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))

    n=""
    s=0
    for i in result:
        if i != "," and i != " ":
            n+=i
        if i==" ":
            s+=int(n)
            n=""
    s+=int(n)
    
    await ctx.send(result)
    await ctx.send(f"Сумма: {s}")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    ra=random.choice(os.listdir('images'))
    with open(f'images/{ra}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def pres(ctx, texts: str):

    f = open('texts/text.txt', 'r', encoding='utf-8')
    text = f.read()
    f.close()
    
    f = open('texts/text.txt', 'w', encoding='utf-8')
    f.write(texts)
    f.close()
    await ctx.send(text)

@bot.command()
async def sorti(ctx):
    rand=random.choice(os.listdir('sorti'))
    with open(f'sorti/{rand}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def recikle(ctx):
    rand=random.choice(os.listdir('pererobotka'))
    with open(f'pererobotka/{rand}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTE4OTk0MDE3MzUzMDczMDYzOA.GTbjJJ.x_CNOLaD_6zlT-jm0KOGWAyaHysfsa-OtvZgj8")