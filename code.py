import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！GitHub（非公開）から実行されています🌸")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
