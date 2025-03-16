import discord
from discord.ext import commands
from modules.helpers import *
import asyncio

client = commands.Bot(
    command_prefix=PREFIX,
    owner_ids=OWNER_IDS,
    intents=discord.Intents.all()
)

client.remove_command('help')

async def load_extensions():
    for filename in os.listdir(COG_FOLDER):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load_extensions()
    await client.start(TOKEN)

asyncio.run(main())
