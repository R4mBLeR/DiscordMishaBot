import pprint
import discord
import random
import config
import asyncio
import requests
import xmltodict

from discord.ext import commands

nudes = [
    'https://cdn.discordapp.com/attachments/910552475604492299/942058373615079505/Screenshot_131.png',
    'https://cdn.discordapp.com/attachments/910552475604492299/942058371866042368/Screenshot_157.png',
    'https://cdn.discordapp.com/attachments/910552475604492299/942058372943978546/Screenshot_130.png',
    'https://cdn.discordapp.com/attachments/910552475604492299/942058373220810854/Screenshot_129.png',
    'https://cdn.discordapp.com/attachments/910552475604492299/942058373615079505/Screenshot_131.png',
    'https://cdn.discordapp.com/attachments/910552475604492299/942058373896106065/Screenshot_126.png',
    'https://cdn.discordapp.com/attachments/910552475604492299/942058374319710298/Screenshot_125.png',
    'https://cdn.discordapp.com/attachments/910552475604492299/942058374634274816/Screenshot_124.png',
    'https://cdn.discordapp.com/attachments/833415227554922516/933972072722473000/Screenshot_16.png.webp',
    'https://cdn.discordapp.com/attachments/833415227554922516/933808523291287552/unknown.png',
    'https://cdn.discordapp.com/attachments/833415227554922516/933808307624374272/unknown.png',
    'https://cdn.discordapp.com/attachments/833415227554922516/933803495486783578/j7srFlLaso0.png',
    'https://cdn.discordapp.com/attachments/833415227554922516/933803986681753722/WIN_20161204_11_37_20_Pro.jpg',
    'https://cdn.discordapp.com/attachments/833415227554922516/933803600847708241/esf6FmPSeBE.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388180529872998/Screenshot_5.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388180798279710/Screenshot_6.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388181138042960/Screenshot_7.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388181356138526/Screenshot_24.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388181532303360/Screenshot_25.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388181733638224/Screenshot_26.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388181918183434/Screenshot_27.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388182123675648/Screenshot_28.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388182375358474/Screenshot_36.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388182652162048/Screenshot_4.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388265569374258/Screenshot_29.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388265758101555/Screenshot_3.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388266051723264/Screenshot_30.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388266286612500/Screenshot_8.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388266500497448/Screenshot_9_2.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388266714427413/Screenshot_9.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388266936696892/Screenshot_2_2.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388267200954408/Screenshot_2.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388267377106964/Screenshot_21.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388324298006568/Screenshot_16.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388324545462332/Screenshot_19.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388324805533726/Screenshot_10_2.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388325069770802/Screenshot_10.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388325283676180/Screenshot_11_2.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388325497577472/Screenshot_11.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388325728260106/Screenshot_12.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388325917020200/Screenshot_13.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388326227406868/Screenshot_14.png',
    'https://cdn.discordapp.com/attachments/942001571863089152/942388327255007232/Screenshot_15.png',
]
flips = [
    'Орёл', 'Решка']
arr2 = [
    'скажи 300', 'Шуток не будет, если хотите, заставьте мишу добавить их написав ему ', 'иди нахуй, шуток не будет',
    'заходит однажды в бар чёрный и попугай']
arr = [
    'Да', 'Нет', 'Иди нахуй', 'Возможно', 'Думай сам', 'ты пидор', 'Типичный вопрос от Бобрика', 'Подумай сам',
    'Это сводный брат Бобрика', 'кринж', 'только не плачь', 'Бобрик лох', 'Хихихаха', 'Абобус', 'член жареный',
    'мне лень это обдумывать', 'миша клоун', 'негры пидорасы', 'Угар', 'шиза миши приехала',
    'АХАХАХХАХАХАХАХАХХАХАХААХАХАХАХАХА']

bot = commands.Bot(command_prefix='!')

safebooru = []
gelbooru = []
TIMEOUT = 30
ID_CHANNEL = 942182707205648416
ID_CHANNEL2 = 942458780002693201
POST_LIMIT = 1
tag = "girl"


@bot.event
async def on_ready():
    print('Егор выпущен на охоту')
    channel = bot.get_channel(ID_CHANNEL)
    channel2 = bot.get_channel(ID_CHANNEL2)
    while True:
        await asyncio.sleep(TIMEOUT)
        print('SEARCH IMAGES:')

        Responce = requests.get('https://safebooru.org/index.php?page=dapi&s=post&q=index&limit=1')
        obj = xmltodict.parse(Responce.text, force_list={'post'})
        try:
            tags = obj["posts"]["post"][0]['@tags']
        except KeyError:
            print('Safebooru: Error')
            tags=" "
        if tag not in tags:
            print('Safebooru: Image not found')
        else:
            file_url = obj["posts"]["post"][0]['@file_url']
            if file_url not in safebooru:
                safebooru.append(file_url)
                embed = discord.Embed(color=0xbb1bf5)
                embed.set_image(url=file_url)
                await channel2.send(embed=embed)
                print('Safebooru: Image ', file_url, 'sended')

        Responce = requests.get('https://gelbooru.com/index.php?page=dapi&s=post&q=index&limit=1')
        obj = xmltodict.parse(Responce.text, force_list={'post'})
        try:
            tags = obj["posts"]["post"][0]['tags']
        except KeyError:
            print('Gelbooru: Error')
            tags=" "
        if tag not in tags:
            print('Gelbooru: Image not found')
        else:
            file_url = obj["posts"]["post"][0]['file_url']
            if file_url not in gelbooru:
                gelbooru.append(file_url)
                embed = discord.Embed(color=0x00ff00)
                embed.set_image(url=file_url)
                await channel.send(embed=embed)
                print('Gelbooru: Image ', file_url, 'sended')


@bot.event
async def on_message(message):
    if message.content.lower().startswith('бот'):
        await message.channel.send(random.choice(arr))
    if message.content == '300':
        await message.channel.send('отсоси у тракториста')
    await bot.process_commands(message)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    logschannel = bot.get_channel(943178689972158514)
    embed = discord.Embed(title=f'{str(message.author)} send message:', description=f'<#{int(message.channel.id)}> {message.content}', color=0x00ff00)
    try:
        embed.set_image(url=message.attachments[0].url)
    except IndexError:
        pass
    await logschannel.send(embed=embed)
    await bot.process_commands(message)


@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return
    logschannel = bot.get_channel(943178689972158514)
    embed = discord.Embed(title=f'{str(message.author)} delete message:', description=f'<#{int(message.channel.id)}> {message.content}', color=0xff0000)
    try:
        embed.set_image(url=message.attachments[0].url)
    except IndexError:
        pass
    await logschannel.send(embed=embed)
    await bot.process_commands(message)


@bot.command(name="anime")
async def pic(ctx, arg1: str):
    payload = {'limit': '1000', 'tags': arg1}
    Res = requests.get('https://safebooru.org/index.php?page=dapi&s=post&q=index', params=payload)
    obj = xmltodict.parse(Res.text)
    Number = random.randrange(0, 1000)
    file_url = obj["posts"]["post"][Number]['@file_url']
    embed = discord.Embed(title='Вот твоя картинка:', color=0xbb1bf5)
    embed.set_image(url=file_url)
    await ctx.send(embed=embed)


@bot.command(name="gif2")
async def pic(ctx, Tag: str):
    payload = {'q': Tag, 'key' : "O4UDCVI14VWL"}
    response = requests.get("https://g.tenor.com/v1/search?limit=50", params=payload )
    data = response.json()
    gif=random.choice(data["results"])
    url=gif['media'][0]['gif']['url']
    embed = discord.Embed(title=gif['content_description'], color=0x0de023)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(name="img")
async def pic(ctx, Tag: str):
    payload={'q': Tag, 'client_id': 'f0ede4c83da06ee'}
    response = requests.get("https://api.imgur.com/3/gallery/search/viral/all/1?", params=payload)
    data = response.json()
    pic=random.choice(data["data"])
    url=pic["images"][0]["link"]
    embed = discord.Embed(title=pic['title'], color=0x0de023)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(name="flip")
async def flip(ctx):
    await ctx.send(random.choice(flips))


@bot.command(name="spam")
async def spam(ctx, member: discord.Member, amount: int, *, message):
    if amount < 9999999999:
        await ctx.send('Спам начался')
        for i in range(amount):
            await member.send(message)


@bot.command(name="ping")
async def ping(ctx, amount: int, *, message):
    for i in range(amount):
        await ctx.send(message)


@bot.command(name="secretcommand")
async def clown(ctx):
    await ctx.send('Бобрик пидорас ёбаный')


@bot.command(name="bot")
async def rofl(ctx):
    await ctx.send(random.choice(arr))


@bot.command(name="шутка")
async def rofl(ctx):
    await ctx.send(random.choice(arr2))


@bot.command(name="info")
async def info(ctx):
    await ctx.send('Привет, это бот миши, он может делать многое')


@bot.command(name="clear")
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)


@bot.command(name="mute")
async def mute(ctx):
    await ctx.send('сам себя замуть клоун')


@bot.command(name="misha")
async def cringe(ctx):
    await ctx.send(random.choice(nudes))


@bot.command(name="sasha")
async def cringe(ctx):
    embed = discord.Embed(title="Саша, 12 лет, пошлый", description="Секс по вызову", color=0x00ff00)
    embed.set_image(url="https://cdn.discordapp.com/attachments/833415227554922516/933803542446223410/qp-UzyxoKvc.png")
    await ctx.send(embed=embed)

bot.run(config.settings['TOKEN'])
