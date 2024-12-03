
from discord.ext import commands
from apiNeeds import BOTTOKEN
import discord
import random



intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

botDiscord = commands.Bot(command_prefix='!', intents=intents,help_command=None,case_insensitive=True)

ecoFlag = 1
ecoWord = ""
@botDiscord.event
async def on_ready():
    print(f'Bot {botDiscord.user} preparado')

@botDiscord.event
async def on_member_join(member):
    canal = botDiscord.get_channel(1292470943972720663)
    await canal.send(f"Bienvenido {member.get_name} :D")

@botDiscord.event
async def on_member_remove(member):
    canal = botDiscord.get_channel(1292470943972720663)
    await canal.send(f"Adios {member.get_name} :(")


@botDiscord.command()
async def man(ctx):
    await ctx.send(
        "Comandos:\n"
        "!saludo --> Recibe un saludo por parte de un bot\n"
        "!man --> Muestra los comandos del bot\n"
    )

@botDiscord.command()
async def help(ctx):
    await ctx.send(
        "Comandos:\n"
        "!saludo --> Recibe un saludo por parte de un bot\n"
        "!man --> Muestra los comandos del bot\n"
    )

@botDiscord.command()
async def ayuda(ctx):
    await ctx.send(
        "Comandos:\n"
        "!saludo --> Recibe un saludo por parte de un bot\n"
        "!man --> Muestra los comandos del bot\n"
    )
@botDiscord.command()
async def saludo(ctx):
    i = random.randint(0,3)

    match i:
        case 0:
            await ctx.send(f"Hola {ctx.author}")
        case 1:
            await ctx.send("¡Holaaaaaaaaaa!")
        case 2:
            await ctx.send(f"¡Muy buenas {ctx.author}!")
        case _:
            SystemExit(0)

@botDiscord.command()
async def saludoEspecifico(ctx, nombre: str):
    await ctx.send(f"Hola {nombre}, te saluda {ctx.author}")

"""
@botDiscord.command()
async def eco(ctx, nombre:str):
    global ecoFlag
    global ecoWord

    if nombre != None and (ecoWord == nombre or ecoFlag >0):
        await ctx.send(f"ECOOOOOO (de {ctx.author}).\n¡Se ha hecho eco de {nombre} {ecoFlag} veces")
        ecoWord = nombre
        ecoFlag += 1

    elif ecoWord != nombre and ecoWord != "" :
        await ctx.send(f"No se puede hacer eco de una palabra diferente de {ecoWord}.\nPara poder reiniciar el eco usar ecoRestart")
"""
"""
@botDiscord.command(pass_context = True)
async def music(ctx, type:int):
    if type == None:
        await ctx.send("Para poner música tienes que poner un parámetro que indique el canal de voz")
        return
    voice_client = ctx.guild.voice_client



@botDiscord.command(pass_context = True)
async def stopMusic(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("Bot retirado de los canales de voz")
    else:
        await ctx.send("El bot no estaba en ningún canal de voz")

"""
@botDiscord.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("No estás en un canal de voz")


@botDiscord.command(pass_context = True)
async def leave(ctx):
    # Obtiene el cliente de voz actual
    voice_client = ctx.guild.voice_client

    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("Desconectado del canal de voz.")
    else:
        await ctx.send("El bot no está conectado a ningún canal de voz.")



botDiscord.run(BOTTOKEN
)