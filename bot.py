import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTIxMDgyNjA0OTg2OTU4MjQwNg.GzUYoZ.LgZpsgC0yHDUhlP7XgswLF2eV9XpDFI0-HqccQ'
    client = discord.Client()
   
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    client.run(TOKEN)
run_discord_bot()