import discord
from discord.ext import commands
import openai

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def gpt(v):
    openai.api_key = "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"
    p = "Ты бот, который следит за экологией и переживаешь за окружающий мир, когда тебе задают вопрос, ты отвечаешь на него с уклоконом в экологию, вот такой вопрос -"
    p2 = "Заменяй свои слова смайликами, вот вопрос-"
    p3 = "Отвечай на вопрос на английском языке - "

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"'{v}'"}
        ])
    
    return completion.choices[0].message.content



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    t = gpt(message.content).split('.')
    for x in t:
        if x != "":
            await message.channel.send(x)


client.run("MTE2MjY4MzQ3MjU3NDQzMTMzNg.Gp58e_.NmtW1vLBVhWnqgNrGV54Q8x-nYRRcYLVma6TGw")