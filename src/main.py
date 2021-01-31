import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='#',description="This is a Terra Bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="https://www.twitch.tv/juansguarnizo"))
    print("My bot is ready")

bot.run('ODA1NTU1ODEzNzU0MjA4Mjc4.YBcmUA.bNp3zH9AQ1IcpPUk1kq_ZpbZJ9U')