# -*- coding: utf-8 -*-

# APIラッパと非同期I/Oモジュールの読み込み
from discord.ext import commands
import discord
import asyncio

desc = '''This is Kaguya Runa.'''

# クライアント接続オブジェクト
client = commands.Bot(command_prefix='!', description = desc)

# 起動時の処理
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# 誰かが発言した時の処理
@client.command()
async def train():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    html = urlopen("http://www.nankai.co.jp/railinfo.html")
    soup = BeautifulSoup(html,"lxml")
    for i in soup.find("div",{"id":"kouyalineinfo"}).find("div"):
        await client.say(i.get_text())

@client.command()
async def tenki():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    html = urlopen("https://typhoon.yahoo.co.jp/weather/jp/warn/27/27216/")
    soup = BeautifulSoup(html,"lxml")
    for i in soup.find("div",{"id":"area_2721600"}).find("li"):
        await client.say("河内長野市で現在発表中の警報・注意報は「"
        + i.get_text()
        + "」だよおおおおおおお!!\n https://typhoon.yahoo.co.jp/weather/jp/warn/27/27216/")

@client.command()
async def call():
    await client.say("https://appear.in/meeting-santa")

# token にDiscordのデベロッパサイトで取得したトークンを入れてください
client.run("NDY3OTA5MTEwNDUzNzY0MTA2.DixejQ.H_GbUQoVgrKQ4Hv4bFiYb2MGQzo")
