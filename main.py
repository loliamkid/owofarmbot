import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "-"

#use the .env feature to hide your token

keep_alive()
token = os.getenv("TOKEN")

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Help AutoOwO", color=420699, description=f"**{prefix}autoOwO**\nowoh, owo sell all, owo flip 500 and owo cash 50 seconds.\n\n**{prefix}stopautoOwO**\nstops autoOwO.")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/819971643157118987/845166279266271282/unknown-7.jpg")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def autoOwO(ctx):
	await ctx.message.delete()
	await ctx.send('auto OwO Magi is now **start**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('owoh')
			print(f"{Fore.GREEN}succefully owoh")
			await asyncio.sleep(15)
			await ctx.send('owo sell all')
			print(f"{Fore.GREEN}succefully sell")
			await ctx.send('owo flip 500')
			print(f"{Fore.GREEN}succefully owo flip 500")
			await asyncio.sleep(10)
			await ctx.send('owo cash')
			print(f"{Fore.GREEN}succefully cash")
			await asyncio.sleep(10)


@bot.command()
async def stopautoOwO(ctx):
	await ctx.message.delete()
	await ctx.send('auto OwO Magi is now **stop**!')
	global dmcs
	dmcs = False

@bot.event
async def on_ready():
  activity = discord.Game(name="OwO", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}

selfbot is ready!
''')

bot.run(token, bot=False)