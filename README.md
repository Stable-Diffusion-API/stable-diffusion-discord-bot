# AI Powered Art in a Discord Bot!


# Feature 

1. you can use negative prompt and height weight
2. You can use stable diffusion models
3. Blacklist Word - If someone speaks bad words, the bot will not work.

examples:  
`/dram prompt: a city street`  
and without people  
`/dream prompt: a city street negative_prompt: people`  

to change the model use:  
`models list` - [/dream prompt: a city street model: Midjourney] to get a list of models and then click to set it. 


## Setup

Bot uses [Stable Diffusion Api](https://stablediffusionapi.com/) as the backend.

You need a stable Diffusion API for this boat to run

Create a file called `.env` in the same folder as `main.py`. Inside the `.env` file,
create a line `BOT_TOKEN = xxxx`, where xxxx is your discord bot token.
create a line `API_KEY = xxxx`, where xxxx is your https://stablediffusionapi.com/settings/api api key.
Now, you can run the bot

`python main.py`


