import discord
from discord import option
from discord.ext import commands

import asyncio
import string
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
key = os.getenv('KEY')
channel_id = os.getenv('CHANNEL_ID')

words = ['nsfw', 'nude', 'naked', 'pussy', 'vagina', 'dick', 'cock', 'penis', 'loli', 'shota', 'child',
         'children', 'xnxx', 'pron', 'hentai', 'asshole', 'sex', 'xxxx', 'xxx', 'pronhub', 'boob', 'boobs']

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.message_content = True

bot = commands.Bot(command_prefix="!s", case_insensitive=True, intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"/dream generate image\n"))


@bot.slash_command(name="dream", description="Ai Create Image")
@option("prompt", description="Enter a prompt for image")
@option("model", desciption="Choose Sytle Model(default is Deliberate)", choices=["Midjourney", "Anything", "Deliberate", "Dosmix", "Chillout Mix", "Waifu Diffusion", "Dreamlike Photoreal 2.0"], default="Deliberate")
@option("negative_prompt", description="Enter a negative prompt for image", default="bad quality, poor quality, NSFW")
@option("aspect_ratio", desciption="Choose aspect ratio for image(default is Square)", choices=["Portrait", "Landscape", "Square", "Desktop", "Mobile"], default="Square")
async def stablediffusion(ctx, prompt: str, model: str, negative_prompt: str, aspect_ratio: str):
    if ctx.channel.id == channel_id:
        search = prompt if True else ' '.join([prompt, negative_prompt])
        for word in words:
            for word2 in search.translate(str.maketrans('', '', string.punctuation)).split():
                if word.lower() == word2.lower():
                    await ctx.respond(f'You tried to use a banned word! ({word})')
                    return
        msg = f"```prompt:{prompt}\nNegative Prompt: {negative_prompt}\nModel: {model}\nAspect Ratio:{aspect_ratio}\n```"
        embed = discord.Embed(title="Please Wait Few Second",
                              color=discord.Color.blue(), description=msg)
        respn = await ctx.respond(embed=embed)
        if model == "Midjourney":
            id = "midjourney"
        elif model == "Anything":
            id = "anything-v3"
        elif model == "Deliberate":
            id = "deliberate-v2"
        elif model == "Dosmix":
            id = "dosmix"
        elif model == "Chillout Mix":
            id = "chilloutmix"
        elif model == "Waifu Diffusion":
            id = "waifu14"
        elif model == "Dreamlike Photoreal 2.0":
            id = "dreamlike"
        if aspect_ratio == "Square":
            width = 512
            height = 512
        elif aspect_ratio == "Portrait":
            width = 512
            height = 768
        elif aspect_ratio == "Landscape":
            width = 768
            height = 512
        elif aspect_ratio == "Mobile":
            width = 576
            height = 1024
        elif aspect_ratio == "Desktop":
            width = 1024
            height = 576
        data = {
            "key": key,
            "model_id": id,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "samples": "1",
            "num_inference_steps": "30",
            "safety_checker": "no",
            "enhance_prompt": "no",
            "seed": None,
            "guidance_scale": 7.5,
            "webhook": None,
            "track_id": None
        }
        try:
            response = requests.post(
                "https://stablediffusionapi.com/api/v3/dreambooth", data=json.dumps(data), headers={'Content-Type': 'application/json'})
            resp = response.json()
        except Exception as e:
            print(e)
        try:
            embeds = discord.Embed(
                color=discord.Color.green(), description=msg)
            embeds.set_image(url=resp['output'][0])
            await respn.edit_original_response(content=ctx.author.mention, embed=embeds)
        except Exception as e:
            print(e)
            fetch = resp['fetch_result']
            await asyncio.sleep(130)
            result = requests.post(fetch, data=json.dumps({'key': key}), headers={
                                   'Content-Type': 'application/json'})
            resultk = result.json()
            embeds = discord.Embed(color=discord.Color.red(), description=msg)
            embeds.set_image(url=resultk['output'][0])
            await respn.edit_original_response(content=ctx.author.mention, embed=embeds)

bot.run(token)
