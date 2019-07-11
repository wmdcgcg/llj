import discord
from discord.ext import commands
import logging
import json
with open("xavier.json") as f:
    xavier = json.load(f)
with open("based.json") as f:
    based = json.load(f)
import random

logging.basicConfig(level="INFO")
bot = commands.Bot(command_prefix="l?", description="a good girl and a terrible boy, or maybe the other way around (WIP)")

@bot.command()
async def test(ctx):
    await ctx.send("robot noise")

@bot.group(invoke_without_command=True)
async def quote(ctx):
    await ctx.send("i can quote! use <prefix>quote and the subcommand xra or lilb")

@quote.command(name="xra")
async def quote_xra(ctx):
    await ctx.send(random.choice(xavier))

@quote.command(name="lilb")
async def quote_lilb(ctx):
    await ctx.send(random.choice(based))

bot.run("secret ;3")
