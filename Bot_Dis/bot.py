import discord

import Dictionary

import config

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        msg = message.content.lower()
        answer = open('dictionary/answer_greet.txt', 'r')
        # if message.content.startswith("привет"):
        #     await message.channel.send(answer.read())
        if msg in Dictionary.Greeting:
            await message.channel.send(answer.read())

client = MyClient()
client.run(config.TOKEN)