# -*- coding: utf-8 -*-
#test
from discord.ext import commands
import discord
import asyncio
import datetime
import random

bot = commands.AutoShardedBot(command_prefix='top!')
bot.remove_command('help')

@bot.listen()
async def on_ready():
    print("TOP Bot#3938 Iniciado com sucesso")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name='?TOP Bot beta!',type=0))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Activity(name='Meu comando é top!help ??',type=2))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Activity(name='Meu servidor: http://bit.ly/toprewards123 ?',type=1))
    await asyncio.sleep(10)

@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        text = message.content.replace(bot.user.mention, "")
        if len(text) == 0:
            await message.channel.send(f":speech_balloon: **|** Olá {message.author.mention}! Precisa de uma ajudinha?\n Use ``top!help`` para ver meus comandos")
            await ctx.invoke(command)

    # linha necessária para processar comandos via ext.commands caso este code esteja no arquivo main do bot
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        return await ctx.send(f':x: **|** Permissões insuficientes! - {error.missing_perms}')
    elif isinstance(error, commands.CommandNotFound):
        return
    else:
        raise error

@bot.command()
async def ping(ctx):
        embed = discord.Embed(color=0xEE4000)
        embed.add_field(name=":ping_pong: Pong!!",value=f":earth_americas:  **|** O meu ping está em {int(bot.latency * 1000)}ms",inline="True")
        await ctx.send(embed=embed)

@bot.command(name='help',aliases=['ajuda'])
async def _help(ctx):
        embed = discord.Embed(color=0x6495ED)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/568127356166996030/b4e4af55b6e026bd99d3eb3c1788cd97.png?size=128")
        embed.set_author(name='TOP Bot', icon_url="https://cdn.discordapp.com/avatars/568127356166996030/b4e4af55b6e026bd99d3eb3c1788cd97.png?size=128")
        embed.add_field(name=":radio:  | Sobre Mim",value="**Iae, sou o TOP Bot, atualmente possuo 16 comandos**",inline="True")
        embed.add_field(name=":robot:  | Prefixo",value="**Meu prefixo oficial é:** ``top!``",inline="True")
        embed.add_field(name=":gear:  | Utilitários",value="```ping | avatar | help | links | say | botinfo```",inline="True")
        embed.add_field(name=":cop:  | Moderação",value="```ban | unban | lock | unlock | clear```",inline="True")
        embed.add_field(name=":star2:  | Personalizados",value="```embed | roleta | spotify```",inline="True")
        embed.add_field(name=":grin:  | Diversão",value="```beijar | socar```",inline="True")
        await ctx.author.send(embed=embed)
        await ctx.send("?? **|** Enviei meus comandos em suas mensagens diretas!")

@bot.command()
async def beijar(ctx, member:discord.Member=None):
        imagens =  ["https://cdn.discordapp.com/attachments/551863767483416587/569346729867083816/beijo.gif", "https://cdn.discordapp.com/attachments/551863767483416587/569345834064543744/kiss.gif", "https://cdn.discordapp.com/attachments/551863767483416587/569346697851961364/love.gif"]
        variavel = random.choice(imagens)
        embed = discord.Embed(color=0xFFFF00)
        embed.add_field(name="?? **|** Beijinhos!",value=f"?? {ctx.author.mention} **beijou** {member.mention}",inline="True")
        embed.set_image(url=variavel)
        await ctx.send(embed=embed)

@bot.command()
async def socar(ctx, member:discord.Member=None):
        imagens =  ["https://pa1.narvii.com/5987/69b8a7cfb561a3db54a978ac001d359aba493d12_hq.gif", "http://4.bp.blogspot.com/-OA9Xb9JnKPE/VQHfk52ZB1I/AAAAAAAAAZU/RZgltfU5jzc/s1600/tumblr_mutqkyNO0I1swqhljo1_500.gif", "http://3.bp.blogspot.com/-MRZdD91rREc/VQHgYWksEZI/AAAAAAAAAZc/MYthMgy3JVI/s1600/LuffyVSLucci.gif"]
        variavel = random.choice(imagens)
        embed = discord.Embed(color=0xFFFF00)
        embed.add_field(name=":punch: **|** socos!",value=f":punch:  {ctx.author.mention} **Socou** {member.mention}",inline="True")
        embed.set_image(url=variavel)
        await ctx.send(embed=embed)

@bot.command()
async def lock(ctx):
    role = ctx.guild.default_role
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await ctx.channel.set_permissions(overwrite=overwrite, target=role)

@bot.command()
async def unlock(ctx):
    role = ctx.guild.default_role
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await ctx.channel.set_permissions(overwrite=overwrite, target=role)

@bot.command()
async def links(ctx):
        embed = discord.Embed(color=0xFF00FF)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/568127356166996030/b4e4af55b6e026bd99d3eb3c1788cd97.png?size=128")
        embed.add_field(name=":book:  **|** Links",value="Você quer me convidar para o seu servidor no Discord? É bem simples, basta clicar [aqui](https://discordapp.com/api/oauth2/authorize?client_id=565687980371738668&permissions=0&scope=bot)\n\n Tem alguma sugestão, dúvida ou deseja reportar algum bug, entre em meu suporte clicando [aqui](https://discord.gg/GrbBBTx)",inline="True")
        await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, *, useravatar: discord.Member = None):
    if useravatar is None:
        user = ctx.author
    else:
        user = useravatar
    eavatar = discord.Embed(color=0x00ffff, title=f'Avatar de {user.name}')
    eavatar.set_image(url=user.avatar_url)
    eavatar.set_footer(icon_url=ctx.author.avatar_url,
                       text='Solicitado por {}'.format(ctx.author.name))
    await ctx.send(embed=eavatar)

@bot.command()
async def clear(ctx, quantidade: int):
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send('?? **Você não possui permissão para limpar o chat!**')
    if ctx.author.guild_permissions.manage_messages:
        try:
            await ctx.message.delete()
            await ctx.channel.purge(limit=quantidade)
            embed = discord.Embed(color=0x00ffff,
                                  description='**{}** Mensagens apagadas com Sucesso! '.format(quantidade))
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        finally:
            pass

@bot.command()
async def say(ctx, *words: str):
   await ctx.send(' '.join(words))

@bot.command()
async def botinfo(ctx):
        embed = discord.Embed(color=0xFF6A6A)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/568127356166996030/b4e4af55b6e026bd99d3eb3c1788cd97.png?size=128")
        embed.add_field(name="TOP Bot",value="Olá, sou TOP Bot, um bot simples do Discord!!",inline="True")
        embed.add_field(name="?? | Prefixo",value="Meu prefixo por padrão é: ``top!``",inline="True")
        embed.add_field(name="?? | Linguagem de programação",value="discord.py",inline="True")
        embed.add_field(name="?? | ID",value="``565687980371738668``",inline="True")
        embed.add_field(name=":clipboard: | Bot Tag",value="``#3938``",inline="True")
        embed.add_field(name=":construction_worker:  | Criador",value="Fui criado por <@403253658029916160>",inline="True")
        embed.add_field(name="?? | Criação",value="Fui criado em 21/04/2019, ás 12:00",inline="True")
        embed.add_field(name=":envelope_with_arrow: | Convite do Bot",value="[**Clique para me adicionar**](https://discordapp.com/api/oauth2/authorize?client_id=565687980371738668&permissions=8&scope=bot)")
        embed.add_field(name="? Servidor de Suporte",value="[**Clique para entrar**](https://discord.gg/GrbBBTx)")
        await ctx.send(embed=embed)

@bot.command()
async def ban(ctx, members: commands.Greedy[discord.Member], *, motivo: str = None):
    if not ctx.author.guild_permissions.ban_members:
        return await ctx.send('**Você não possui permissão para executar este comando!**')
    try:
        if not motivo:
            motivo = ""
        for member in members:
            guild = ctx.guild.name
            author = ctx.author.mention
            embed = discord.Embed(color=0x020000,
                                  description='**O usuario(a) <@{}>  \n Foi banido por: {} \n\n {}**'.format(
                                      member.id, author, motivo))
            embed.set_footer(text=guild, icon_url=ctx.guild.icon_url)
            embed.set_thumbnail(url=member.avatar_url)
            await member.ban(delete_message_days=1, reason=motivo)
            await ctx.send(embed=embed)
            await ctx.message.delete()
    except IndexError:
        await ctx.send('**Você deve especificar um usuário para banir!**')
    except discord.Forbidden:
        await ctx.send(
            '**Não posso banir o usuário acima de mim ou não tenho permissão**!')
    finally:
        pass

@bot.command()
async def unban(ctx, id: int):
    try:
        user = await client.fetch_user_info(id)
        guild = ctx.guild
        try:
            author = ctx.author
            embed = discord.Embed(color=0x7fff00,
                                  description='**ID **({})\n-  \n <@{}> \n**ID **({}) \n **Desbanido(a) do servidor.**'.format(
                                      author.id, user.id, user.id))
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_author(name='{}'.format(str(author.name)), icon_url=author.avatar_url)
            await guild.unban(user)
            await ctx.send(embed=embed)
        except:
            await ctx.send('Provavelmente o usuário não está banido.')
    except:
        await ctx.send('ID Inválido.')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx, *, mensagem):
    await ctx.message.delete()
    vote = await ctx.send(embed=discord.Embed(color=0x97FFFF, description=mensagem))
    await vote.add_reaction("? ")
    await vote.add_reaction("? ")
    await ctx.send('Você não tem permissão')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def anuncio(ctx, *, mensagem):
    await ctx.message.delete()
    vote = await ctx.send(embed=discord.Embed(color=0xFF34B3, description=mensagem))
    await vote.add_reaction("? ")
    await vote.add_reaction("? ")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def embedi(ctx, *, mensagem):
    await ctx.message.delete()
    vote = await ctx.send(embed=discord.Embed(color=0x00FF00, description=mensagem))
    await vote.add_reaction("? ")
    await vote.add_reaction("? ")

@bot.command()
async def roleta(ctx, *, pergunta: str = None):
    from random import choice
    if not pergunta:
        return await ctx.send("Você deve perguntar algo.")
    else:
        resposta = choice(['Sim', 'Não', 'Talvez', 'Nunca', 'Claro', 'Sempre', 'Jamais', 'De vez em quando'])
        embed = discord.Embed(color=0x9B30FF)
        embed.add_field(name="Pergunta:", value='{}'.format(pergunta), inline=False)
        embed.add_field(name="Resposta:", value=resposta, inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def spotify(ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        act = member.activity
        if act is None or not act.type == discord.ActivityType.listening:
            if member == ctx.author:
                await ctx.send('Você não está ouvindo nada')
            else:
                await ctx.send('Esse usuário não está ouvindo nada')
        else:
            end = act.end - datetime.datetime.utcnow()
            end = str(act.duration - end)[2:7]
            dur = str(act.duration)[2:7]
            embed = discord.Embed(title=f'**Spotify - {member.name}**', color=act.color)
            embed.set_thumbnail(url=act.album_cover_url)
            embed.add_field(name='**Música**', value=f'[{act.title}](https://open.spotify.com/track/{act.track_id})')
            embed.add_field(name='**Artista**', value=act.artist)
            embed.add_field(name='**Álbum**', value=act.album)
            embed.add_field(name='**Duração**', value=end + ' - ' + dur)
            await ctx.send(embed=embed)

bot.run("NTY1Njg3OTgwMzcxNzM4NjY4.XLyThg.6lgsJXK5_teay1W5SmgDRDYgCIU")
