import discord
import random

# Initialize the bot
intents = discord.Intents.all()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

# Your bot's token
TOKEN = 'YOUR_BOT_TOKEN'

# List of links to random images
random_images = [
    'LINK1',
    'LINK2',
    # Add your own links here
]

@client.event
async def on_ready():
    print(f'Bot {client.user} is ready for action')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!random_image'):
        random_image = random.choice(random_images)
        await message.channel.send(random_image)

# Run the bot
client.run(TOKEN)
