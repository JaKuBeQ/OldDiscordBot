import nextcord as discord
from nextcord import channel
from nextcord import member
from nextcord import message
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
import random
import asyncio

client = commands.Bot(command_prefix = "$")
client.remove_command("help")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='$help'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
       await asyncio.sleep(1)
       await ctx.send("Podana komenda nie istnieje")

    if isinstance(error, commands.CommandOnCooldown):
       await asyncio.sleep(1)
       await ctx.send(f"Aby użyć ponownie tej komendy poczekaj {error.retry_after:.0f} sekund")

@client.command()
async def napisz(ctx, *, tekst):
    await ctx.message.delete()
    await asyncio.sleep(1)
    await ctx.channel.send(tekst)

@client.command()
async def clear(ctx, amount = 5): 
 if commands.has_permissions(manage_messages=True):
   await ctx.channel.purge(limit=amount+1)
   await asyncio.sleep(1)                                   
   await ctx.send(f"Usunięto: {amount} wiadomości", delete_after = 10)
        

@client.command()
async def simprate(ctx, member : discord.Member):
    simpowanie=random.randrange(0,100)
    await asyncio.sleep(1)
    await ctx.channel.send(f"{member.mention} jest simpem w {simpowanie}%")

@simprate.error
async def simprate_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("Nie ma podanej osoby")

@client.command()
async def iq(ctx, member : discord.Member):
    inteligencja=random.randrange(1,400)
    await asyncio.sleep(1)
    await ctx.channel.send(f"Inteligencja {member.mention} wynosi: {inteligencja} IQ")

@iq.error
async def iq_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("Nie ma podanej osoby")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await asyncio.sleep(1)
    await ctx.channel.send(f"Zbanowano {member.mention} na serwerze za {reason}")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("nie ma podanej osoby")

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, reason="No Reason"):
    await member.kick(reason=reason)
    await asyncio.sleep(1)
    await ctx.channel.send(f"Wyrzucono {member.mention} z serwera za {reason}")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("Nie ma podanej osoby")

@client.command()
@commands.has_permissions(administrator = True)
async def play(ctx, *, game):
    await client.change_presence(activity=discord.Game(name=game))

@play.error
async def play_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("Należy podać w co ma grać bot")

@client.command()
@commands.has_permissions(administrator = True)
async def watch(ctx, *, film):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=film))

@watch.error
async def watch_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("Należy podać co ma oglądać bot")

@client.command()
@commands.has_permissions(administrator = True)
async def listen(ctx, *, music):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=music))

@listen.error
async def listen_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("Należy podać co ma słuchać bot")

@client.command(aliases = ["losuj", "Roll", "ROLL"])
async def roll(ctx, min : int, max : int):
    if(min < max):
        numer = random.randrange(min, max)
        await asyncio.sleep(1)
        await ctx.channel.send(f"Wylosowana liczba: {numer}")
    else:
        await ctx.channel.send("Nie prawidłowe liczby")

@client.command(aliases = ["pomoc", "Help", "HELP"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def help(ctx):
    embed=discord.Embed(title="Kategorie", color=0x0aff95)
    embed.add_field(name="4fun", value="$fun", inline=False)
    embed.add_field(name="SocialMedia", value="$sociale", inline=False)
    embed.add_field(name="Moderator", value="$moderator", inline=False)
    await asyncio.sleep(1)
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def fun(ctx):
    embed=discord.Embed(title="Komendy 4fun" , color=0x0aff95)
    embed.add_field(name="$simprate", value="sprawdza w ilu {%} dana osoba jest simpem", inline=False)
    embed.add_field(name="$iq", value="określa inteligencję danej osoby", inline=False)
    embed.add_field(name="$napisz", value="wypisuje daną wiadomość za pomocą bota", inline=False)
    embed.add_field(name="$roll x y", value="losuje liczbę z zakresu x do y gdzie x oraz y podaje użytkownik", inline=False)
    await asyncio.sleep(1)
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def sociale(ctx):
    embed=discord.Embed(title="Wszystkie SocialMedia", color=0x0aff95)
    embed.add_field(name="$twitch", value="kanał Wegorz08", inline=False)
    embed.add_field(name="$twitch2", value="kanał Janczalkus", inline=False)
    await asyncio.sleep(1)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator = True)
async def moderator(ctx):
    embed=discord.Embed(title="Komendy administracyjne", color=0x0aff95)
    embed.add_field(name="$play", value="ustawia status bota na granie", inline=False)
    embed.add_field(name="$listen", value="ustawia status bota na słuchanie", inline=False)
    embed.add_field(name="$watch", value="ustawia status bota na oglądanie", inline=False)
    embed.add_field(name="$ban (osoba)", value="Banuje danego użytkownika na serwerze", inline=False)
    embed.add_field(name="$kick (osoba)", value="Wyrzuca danego użytkownika z serwera", inline=False)
    embed.add_field(name="$clear (ilosc)", value="usuwa daną ilość wiadomości na kanale", inline=False)
    await asyncio.sleep(1)
    await ctx.send(embed=embed)

client.run("ODc2ODg5MTE0NTc2ODM0NTgw.YRqooA.mjSvYZEf_vL8BqKp68WnLXngZbw")