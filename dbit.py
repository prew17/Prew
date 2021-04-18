import discord
import random
import os
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands.core import command
from itertools import cycle

client = commands.Bot(command_prefix = 'PP')
status = cycle(['PPhelp', 'Heres the link to invite the bot to your server :) https://discord.com/api/oauth2/authorize?client_id=822420271595126824&permissions=0&scope=bot'])

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.status.idle, activity=discord.Game('PPhelp'))
    print ('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} :wave: hope you have a good time!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round{client.latency * 1000}}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                  'It is decidedly so.',
                  'Most likely.',
                  'My reply is no.',
                  'My sources say no.',
                  'Outlook not so good.',
                  'Outlook good.',
                  'Reply hazy, try again.',
                  'Signs point to yes.']
    await ctx.send(f'Question: {Question}\nAnswer: {random.choice()}')

@client.command()
async def clear(ctx.amount:int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify the amount of messages to clear.')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unlaod_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(manage_messages=Ture)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(hours=48)
async def change_status()
    await client.change_presence(activity=dicsord.Game(next(status)))


client.run('By7J-744E4hofEsxGSq-IEXpdlD-vwrr')