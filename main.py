import discord
from discord.ext import commands
from bot_mantik import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has joined!')

@bot.command()
async def worldcup(ctx, year):
    await ctx.send(kazanan_takim(year))

@bot.command()
async def mvp(ctx, year):
    await ctx.send(mvp_oyuncu(year))


bot.run('Token')