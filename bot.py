from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import os
import replicate

load_dotenv()

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    description="Deneysel Robotikci Discord kanali botu",
    intents=intents,
)


@bot.command()
async def dream(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    msg = await ctx.send(f"“{prompt}”\n> Cevaplaniyor...")

    model = replicate.models.get("stability-ai/stable-diffusion")
    image = model.predict(prompt=prompt)[0]

    await msg.edit(content=f"“{prompt}”\n{image}")

@bot.command()
async def text(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    #msg = await ctx.send(f"“{prompt}”\n> Cevaplaniyor...")

    #model = replicate.models.get("stability-ai/stable-diffusion")
    #image = model.predict(prompt=prompt)[0]

    #await msg.edit(content=f"“{prompt}”\n{image}")
    #TODO Fill 
    pass 

bot.run(os.environ["DISCORD_TOKEN"])