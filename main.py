import discord

# instantiate a discord client
client = discord.Client()

@client.event
async def on_ready():
  print(f'You have logged in as {client}')
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('lol'):
    await message.channel.send('xd')
  
  def getCryptoPrices(crypto):
    URL ='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    r = requests.get(url=URL)
    data = r.json()



BOT_TOKEN = 'MTAwMjA1NDY4MTc1OTA2MDAyOA.GGbtJs.VdrSY2av8FVSx9JqoTHtBMXWSJwUpXNKUrbO44'
client.run(BOT_TOKEN)
