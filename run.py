# -*- coding: utf-8 -*-

# APIラッパと非同期I/Oモジュールの読み込み
from discord.ext import commands
import discord
import asyncio

desc = '''This is Kaguya Runa.'''

# クライアント接続オブジェクト
client = commands.Bot(command_prefix='!', description=desc)

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
    soup = BeautifulSoup(html, "lxml")
    for i in soup.find("div", {"id": "kouyalineinfo"}).find("div"):
        await client.say(i.get_text())


@client.command()
async def tenki():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    html = urlopen("https://typhoon.yahoo.co.jp/weather/jp/warn/27/27216/")
    soup = BeautifulSoup(html, "lxml")
    await client.say("URL: https://typhoon.yahoo.co.jp/weather/jp/warn/27/27216/")
    await client.say("河内長野市で現在発表中の警報・注意報は")
    for i in soup.find("div", {"class": "warnDetail_head"}, {"id": "area_2721600"}).find_all("li"):
        await client.say("「" + i.get_text() + "」")
    await client.say("だよおおおおおおお!!")


@client.command()
async def tenki_santa():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    html = urlopen("https://typhoon.yahoo.co.jp/weather/jp/warn/27/27214/")
    soup = BeautifulSoup(html, "lxml")
    await client.say("URL: https://typhoon.yahoo.co.jp/weather/jp/warn/27/27214/")
    await client.say("富田林市で現在発表中の警報・注意報は")
    for i in soup.find("div", {"class": "warnDetail_head"}, {"id": "area_2721400"}).find_all("li"):
        await client.say("「" + i.get_text() + "」")
    await client.say("だよおおおおおおお!!")


@client.command()
async def tenki_tomoki():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    html = urlopen("https://typhoon.yahoo.co.jp/weather/jp/warn/27/27100/")
    soup = BeautifulSoup(html, "lxml")
    await client.say("URL: https://typhoon.yahoo.co.jp/weather/jp/warn/27/27100/")
    await client.say("大阪市で現在発表中の警報・注意報は")
    for i in soup.find("div", {"class": "warnDetail_head"}, {"id": "area_2710000"}).find_all("li"):
        await client.say("「" + i.get_text() + "」")
    await client.say("だよおおおおおおお!!")


@client.command()
async def call():
    await client.say("https://appear.in/meeting-santa")

# token にDiscordのデベロッパサイトで取得したトークンを入れてください
client.run("token")
