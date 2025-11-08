import pyttsx3
import random
import requests
from googletrans import Translator
translator = Translator()
# =============================
# FUNCIÓN: OBTENER CLIMA
# =============================
def get_weather(city: str) -> str:
    """
    Obtiene la información del clima desde la API pública wttr.in.
    Devuelve una cadena con el estado del clima y la temperatura actual.
    """
    base_url = f"https://wttr.in/{city}?format=%C+%t"  # Formato: "Condición + Temperatura"
    response = requests.get(base_url)
    if response.status_code == 200:
        # Retorna el texto limpio (sin espacios adicionales ni saltos de línea)
        return response.text.strip()
    else:
        # Si ocurre un error con la API, devuelve un mensaje de error
        return "No se pudo obtener la información del clima."
import discord
from discord.ext import commands
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
@bot.command(name='weather')
async def weather(ctx, city: str):
    """Obtiene el clima de una ciudad específica."""
    weather_info = get_weather(city)
    await ctx.send(f'El clima en {city} es: {weather_info}')
    print(f'El clima en {city} es: {weather_info}')
    speak(f'El clima en {city} es: {weather_info}')
    print("completed the dialogue")
@bot.command(name='fact')
async def get_fact(ctx:str) -> str:
    """
    Recupera un dato curioso aleatorio desde la API.
    Retorna:
        str: El texto del dato en inglés o un mensaje de error.
    """
    base_url = "https://uselessfacts.jsph.pl/random.json"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        if data.get!= None:
             translated = translator.translate(data["text"],src='en',dest='es')
             await ctx.send(f'Dato curioso: {translated.text}')
             speak(f'Dato curioso: {translated.text}')
             return translated.text
        else: await ctx.send(f'Dato curioso: {data.get("text", "Could not retrieve the fact.")}'),speak(f'Dato curioso: {data.get("text", "Could not retrieve the fact.")}')
        print(data)  # Para depuración
        
        fact_text = data.get("text", "Could not retrieve the fact.")  # Obtiene el texto directamente
        return fact_text  # Devuelve el texto tal como lo envía la API
    else:
        return "Could not retrieve a fact. Please try again."

bot.run('DISCORD_BOT_TOKEN')








