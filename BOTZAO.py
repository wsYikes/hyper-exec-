import discord
from discord.ext import commands
import asyncio
import discord.ext
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions



TOKEN = 'Nzc0NDAyNDQ1OTg3NDE0MDY4.X6XQeg.dIoRmgSGK_faiFmGIoG66_in_L8'

client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('bot está ok.')

@client.event
async def on_message(message):
    if message.content.startswith('hyper!exec'):
        embedVar = discord.Embed(title="HyperExec", description=" ", color=0x0B54F0)
        embedVar.add_field(name="Download Bellow", value="https://cdn.discordapp.com/attachments/774288630171566110/774407602535661578/HyperExec_v1.0.exe", inline=False)
        embedVar.add_field(name="Look other products", value="Enjoy :D", inline=False)
        embedVar.set_footer(text='Made By Icon#9677 & delamura#0001',icon_url="https://cdn.discordapp.com/attachments/774288630171566110/774402985366388776/jJoThFZI_400x400.jpg")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/774288630171566110/774402985366388776/jJoThFZI_400x400.jpg")
        await message.channel.send(embed=embedVar)

client.run(TOKEN)
