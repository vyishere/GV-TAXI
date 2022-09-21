import discord
from discord.ext import commands
intents = discord.Intents().all()
client = commands.Bot(command_prefix='gv', intents=intents)
                
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator}')
        
@client.command()
async def taxi(ctx):
    await ctx.send('GV TAXI')
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegOpusAudio('gvtaxi.wav'), after=lambda e: print('GV TAXI', e))

client.run('token')
