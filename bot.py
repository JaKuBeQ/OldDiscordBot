import nextcord as discord
from nextcord import channel
from nextcord import member
from nextcord import message
from nextcord.ext import commands
from nextcord.ext.commands import bot, has_permissions
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

    if isinstance(error, commands.CommandOnCooldown):
       await asyncio.sleep(1)
       await ctx.send(f"Aby użyć ponownie tej komendy poczekaj {error.retry_after:.0f} sekund")

@client.command(aliases = ["author", "Autor", "twórca", "stworzyciel"])
async def autor(ctx):
    await asyncio.sleep(1)
    await ctx.channel.send("discord - JakubeQ#6751")
    await ctx.channel.send("instagram - ""https://www.instagram.com/j4kub3qq/")
    await ctx.channel.send("github - ""https://github.com/JaKuBeQ")

@client.command()
async def hug(ctx, *, member : discord.Member):
    huglinki = ["https://c.tenor.com/9e1aE_xBLCsAAAAM/anime-hug.gif", "https://c.tenor.com/xgVPw2QK5n8AAAAM/sakura-quest-anime.gif", "https://c.tenor.com/xIuXbMtA38sAAAAM/toilet-bound-hanakokun.gif", "https://c.tenor.com/F1VUry86n7kAAAAM/hug-anime.gif", "https://c.tenor.com/VqazOH8fQ8gAAAAM/anime-hug.gif", "https://c.tenor.com/EnfEuWDXthkAAAAM/hug-couple.gif", "https://c.tenor.com/83QLplerW8sAAAAM/anime-hug.gif", "https://c.tenor.com/nmzZIEFv8nkAAAAM/hug-anime.gif", "https://c.tenor.com/Qw4m3inaSZYAAAAM/crying-anime-kyoukai-no-kanata-hug.gif", "https://c.tenor.com/o1jezAk92FUAAAAM/sound-euphonium-hug.gif", "https://c.tenor.com/ljXMDMzMaxcAAAAS/cute-anime.gif", "https://c.tenor.com/ncblDAj_2FwAAAAM/abrazo-hug.gif", "https://c.tenor.com/uIBg3BLATf0AAAAM/hug-darker.gif", "https://c.tenor.com/-0nQoPY5sZ0AAAAM/anime-hug-hug.gif", "https://c.tenor.com/jDJlRRFUge4AAAAM/anime-cute.gif", "https://c.tenor.com/OyOv9Q4MVnkAAAAM/hug-hugs.gif", "https://c.tenor.com/BbGzltHMpJgAAAAM/anime-hug-anime.gif", "https://c.tenor.com/QgMN5YC19xkAAAAM/noragami-kofuku.gif", "https://c.tenor.com/q5GWONzp2h0AAAAM/abra%C3%A7o-hug.gif", "https://c.tenor.com/FJaQ1MKAtowAAAAM/idk-what-anime-this-is-from-but-its-anime-girls-hugging.gif", "https://c.tenor.com/3gh8AG7nCp0AAAAM/ily-i-love-you.gif", "https://c.tenor.com/_Ip7XSmd8M8AAAAM/clannad-after-story-anime.gif", "https://c.tenor.com/1aQeiWOHmuMAAAAM/hug-anime.gif", "https://c.tenor.com/jpXDGO1PcvwAAAAM/anime-hug.gif", "https://c.tenor.com/C_cR0aoT83oAAAAM/anime-lovelovelove.gif"]
    await ctx.send(f"You hugged {member.mention}")
    await ctx.send(f"{random.choice(huglinki)}")

@hug.error
async def hug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("Nie ma podanej osoby")

@client.command()
async def kill(ctx, *, member : discord.Member):
    killlinki = ["https://c.tenor.com/Ce8ZMfAcjdoAAAAM/anime.gif", "https://c.tenor.com/1dtHuFICZF4AAAAM/kill-smack.gif", "https://c.tenor.com/CQorucEqd_cAAAAM/kill-me-baby.gif", "https://c.tenor.com/Wq-Un4pZq50AAAAM/giant-scissor.gif", "https://c.tenor.com/blYwpMNaaCUAAAAM/nichijou-uppercut.gif", "https://c.tenor.com/Ze50E1rW44UAAAAM/akudama-drive.gif", "https://c.tenor.com/Mn4W4D899WEAAAAM/ira-gamagoori-attack.gif", "https://c.tenor.com/WxLl5mre8pYAAAAM/anime-kill.gif", "https://c.tenor.com/Re9dglY0sCwAAAAM/anime-wasted.gif", "https://c.tenor.com/muad6BkGQDMAAAAM/anime-death.gif", "https://c.tenor.com/E4Px9kJOQ5wAAAAM/anime-kid.gif", "https://c.tenor.com/FKwVjGlrp1YAAAAM/higurashi-sotsu.gif", "https://c.tenor.com/-Y2S7j2QhkEAAAAM/higurashi-sotsu.gif"]
    await ctx.send(f"You killed {member.mention}")
    await ctx.send(f"{random.choice(killlinki)}")

@kill.error
async def kill_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("Nie ma podanej osoby")

@client.command()
async def slap(ctx, *, member : discord.Member):
    slaplinki = ["https://c.tenor.com/iDdGxlZZfGoAAAAM/powerful-head-slap.gif", "https://c.tenor.com/PeJyQRCSHHkAAAAM/saki-saki-mukai-naoya.gif", "https://c.tenor.com/E3OW-MYYum0AAAAM/no-angry.gif", "https://c.tenor.com/UDo0WPttiRsAAAAM/bunny-girl-slap.gif", "https://c.tenor.com/eU5H6GbVjrcAAAAM/slap-jjk.gif", "https://c.tenor.com/rVXByOZKidMAAAAM/anime-slap.gif", "https://c.tenor.com/1-1M4PZpYcMAAAAM/tsuki-tsuki-ga.gif", "https://c.tenor.com/pHCT4ynbGIUAAAAM/anime-girl.gif", "https://c.tenor.com/OuYAPinRFYgAAAAM/anime-slap.gif", "https://c.tenor.com/1lemb3ZmGf8AAAAM/anime-slap.gif", "https://c.tenor.com/CvBTA0GyrogAAAAM/anime-slap.gif", "https://c.tenor.com/hNa8BhraaXsAAAAM/anime-nagatoro.gif", "https://c.tenor.com/klNTzZNDmEgAAAAM/slap-hit.gif", "https://c.tenor.com/fy60RaCWq08AAAAM/shikamaru-temari.gif", "https://c.tenor.com/WcYvM-SqPkoAAAAM/baka-slap.gif", "https://c.tenor.com/Op1oKmvsluwAAAAM/cop-craft-tilarna.gif", "https://c.tenor.com/CawKRw6kPtoAAAAM/tokyo-revengers-anime.gif", "https://c.tenor.com/HTHoXnBc400AAAAM/in-your-face-slap.gif", "https://c.tenor.com/DTVNVJrDdJIAAAAM/my-collection-anime.gif", "https://c.tenor.com/3yVUWwGWLpEAAAAM/darker-than-black-dtb-hei.gif", "https://c.tenor.com/Z7OrR3PfW6IAAAAM/kekkaishi-slap.gif", "https://c.tenor.com/n7LKoJVrwM8AAAAM/anime-punch.gif", "https://c.tenor.com/pE1jto7_4AcAAAAM/higurashi-sotsu.gif"]
    await ctx.send(f"You slapped {member.mention}")
    await ctx.send(f"{random.choice(slaplinki)}")

@slap.error
async def slap_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(1)
        await ctx.send("Nie ma podanej osoby")

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
    embed.add_field(name="$hug", value="przytula daną osobę ", inline=False)
    embed.add_field(name="$slap", value="uderza daną osobę", inline=False)
    embed.add_field(name="$kill", value="zabija daną osobę", inline=False)
    await asyncio.sleep(1)
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def sociale(ctx):
    embed=discord.Embed(title="Wszystkie SocialMedia", color=0x0aff95)
    embed.add_field(name="$twitch", value="kanał Wegorz08", inline=False)
    embed.add_field(name="$twitch2", value="kanał Janczalkus", inline=False)
    embed.add_field(name="$autor", value="sociale autora bota", inline=False)
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

client.run("token")
