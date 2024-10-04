# chatbot.py

import config
import responses
from twitchio.ext import commands

# Twitch bot settings
bot = commands.Bot(
    token=config.OAUTH_TOKEN,
    client_id=config.CLIENT_ID,
    nick=config.BOT_NICK,
    prefix=config.COMMAND_PREFIX,
    initial_channels=[config.CHANNEL_NAME]
)

@bot.event
async def event_ready():
    print(f"Logged in as {bot.nick}")
    print(f"Connected to channels: {bot.connected_channels}")

@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == bot.nick.lower():
        return  # Ignore messages from the bot itself

    print(f"Message from {ctx.author.name}: {ctx.content}")

    # Check for custom commands
    custom_response = responses.handle_custom_commands(ctx.content)
    
    if custom_response:
        await ctx.channel.send(custom_response)

    # If no command, the bot could echo the message back or do nothing
    else:
        await ctx.channel.send(f"You said: {ctx.content}")

if __name__ == "__main__":
    print("Starting bot...")
    bot.run()
