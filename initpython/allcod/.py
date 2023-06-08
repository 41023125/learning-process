import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send("Hello World!")

bot.run("MTA4MjI1NTYzNjA3MjUwMTI4OQ.GlQy9i.f8fcNewU-Yu5pCkneWm9mos6ZE2Quso0St6iOQ")
