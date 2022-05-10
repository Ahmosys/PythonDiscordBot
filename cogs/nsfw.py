import random
import requests
import discord


from discord.ext import commands
from ext.colours import Colours
from json import JSONDecodeError


class nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def check_channel(self, ctx):
        return ctx.channel.is_nsfw()

    @commands.command(description="Permet d'afficher 1 image pornographiques réelles / gifs de realbooru.com pour une clé de recherche spécifique.")
    async def realb(self, ctx, *, keyword: str = None):
        async with ctx.channel.typing():
            if not check_channel(ctx):
                    await ctx.send("Le salon n'est pas marqué comme étant **NSFW**, s'il vous plaît exécuter la commande dans un salon approprié.")
            elif keyword is None:
                await ctx.send("Veuillez renseigner un mot-clé!")
            else:
                r = requests.get(f"https://realbooru.com/index.php?page=dapi&s=post&q=index&limit=1000&json=1&tags={keyword}")
                if r.status_code in range (200,299):
                    try:
                        res = r.json()
                        i = random.randint(0,len(res))
                        directory = res[i]["directory"]
                        image = res[i]["image"]
                        url_image = f"https://realbooru.com/images/{directory}/{image}"
                        await ctx.send(f"Voilà pour toi, n'hésite pas à me redemandé!\n{url_image}") 
                    except JSONDecodeError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                    except IndexError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")
    
    @commands.command(description="Permet d'afficher 1 image pornographiques réelles / gifs de rule34.xxx pour une clé de recherche spécifique.")
    async def r34(self, ctx, *, keyword: str = None):
        async with ctx.channel.typing():
            if not check_channel(ctx):
                    await ctx.send("Le salon n'est pas marqué comme étant **NSFW**, s'il vous plaît exécuter la commande dans un salon approprié.")
            elif keyword is None:
                await ctx.send("Veuillez renseigner un mot-clé!")
            else:
                r = requests.get(f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=1000&json=1&tags={keyword}")
                if r.status_code in range (200,299):
                    try:
                        res = r.json()
                        i = random.randint(0,len(res))
                        url_image = res[i]["file_url"]
                        await ctx.send(f"Voilà pour toi, n'hésite pas à me redemandé!\n{url_image}") 
                    except JSONDecodeError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                    except IndexError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")

    @commands.command(description="Permet d'afficher 1 image pornographiques réelles / gifs de gelbooru.com pour une clé de recherche spécifique.")
    async def gelb(self, ctx, *, keyword: str = None):
        async with ctx.channel.typing():
            if not check_channel(ctx):
                    await ctx.send("Le salon n'est pas marqué comme étant **NSFW**, s'il vous plaît exécuter la commande dans un salon approprié.")
            elif keyword is None:
                await ctx.send("Veuillez renseigner un mot-clé!")
            else:
                r = requests.get(f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&limit=1000&json=1&tags={keyword}")
                if r.status_code in range (200,299):
                    try:
                        res = r.json()
                        i = random.randint(0,len(res))
                        url_image = res[i]["file_url"]
                        await ctx.send(f"Voilà pour toi, n'hésite pas à me redemandé!\n{url_image}") 
                    except JSONDecodeError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                    except IndexError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")

    ## 403 status code for the moment. TODO
    @commands.command(description="Permet d'afficher 1 image pornographiques réelles / gifs de gelbooru.com pour une clé de recherche spécifique.")
    async def furry(self, ctx, *, keyword: str = None):
        async with ctx.channel.typing():
            if not check_channel(ctx):
                    await ctx.send("Le salon n'est pas marqué comme étant **NSFW**, s'il vous plaît exécuter la commande dans un salon approprié.")
            elif keyword is None:
                await ctx.send("Veuillez renseigner un mot-clé!")
            else:
                r = requests.get(f"https://furry.booru.org/index.php?page=dapi&s=post&q=index&limit=1000&json=1&tags={keyword}")
                if r.status_code in range (200,299):
                    try:
                        res = r.json()
                        i = random.randint(0,len(res))
                        directory = res[i]["directory"]
                        image = res[i]["image"]
                        url_image = f"https://furry.booru.org/images/{directory}/{image}" 
                        await ctx.send(f"Voilà pour toi, n'hésite pas à me redemandé!\n{url_image}")
                    except JSONDecodeError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                    except IndexError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")

    @commands.command(description="Permet d'afficher 1 image pornographiques réelles / gifs de safebooru.org pour une clé de recherche spécifique.")
    async def safeb(self, ctx, *, keyword: str = None):
        async with ctx.channel.typing():
            if not check_channel(ctx):
                    await ctx.send("Le salon n'est pas marqué comme étant **NSFW**, s'il vous plaît exécuter la commande dans un salon approprié.")
            elif keyword is None:
                await ctx.send("Veuillez renseigner un mot-clé!")
            else:
                r = requests.get(f"https://safebooru.org/index.php?page=dapi&s=post&q=index&limit=1000&json=1&tags={keyword}")
                if r.status_code in range (200,299):
                    try:
                        res = r.json()
                        i = random.randint(0,len(res))
                        directory = res[i]["directory"]
                        image = res[i]["image"]
                        url_image = f"https://safebooru.org/images/{directory}/{image}" 
                        await ctx.send(f"Voilà pour toi, n'hésite pas à me redemandé!\n{url_image}")
                    except JSONDecodeError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                    except IndexError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")

    @commands.command(name = "snudesuser", description = "Permet d'envoyer 1 image pornographique à un utilisateur en DM.")
    #@commands.has_permissions(administrator = True)
    async def send_nudes(self, ctx, member: discord.Member = None, categorie: str = "ass"):
        async with ctx.channel.typing():
            categories  = ["ass", "pussy", "boobs", "blowjob", "creampy", "doggystyle", "missionary"]
            if not check_channel(ctx):
                await ctx.send("Le salon n'est pas marqué comme étant **NSFW**, s'il vous plaît exécuter la commande dans un salon approprié.")
            elif member is None:
                await ctx.send("Veuillez renseigner un utilisateur en le mentionnant!")
            elif member == self.bot.user:
                await ctx.send("Impossible d'envoyé le message au bot!")
            elif categorie not in categories:
                categories = " | ".join(categories)
                await ctx.send(f"Catégorie demandée '{categorie}' invalide.\nVeuillez choisir une catégorie parmis celle ci-dessous:\n{categories}")
            else:
                try:
                    channel = await member.create_dm()
                    r = requests.get(f"https://api.ramsesxyz.fr/" + categorie)
                    res = r.json()
                    em = discord.Embed(title="Tient chacal, régale toi bien!  <:handjob:846563073404829707>", timestamp = ctx.message.created_at, color = Colours.pink())
                    em.set_image(url = res.get("urlImage"))
                    em.set_footer(text = ctx.author)
                    await channel.send(embed = em)
                    await ctx.send(f"Je t'ai envoyé un dm {member.mention} va voir! c'est une dinguerie  <:titsmodji:846557137672732743>")
                except:
                    await ctx.send(f"Le member {member.name} **n'autorise pas** les messages privés venant des membres du serveur.")

    @commands.command(description = "Permet d'afficher 1 image/gifs pornographiques de nekobot.xyz pour une catégorie de recherche spécifique.")
    async def neko(self, ctx, categorie: str = None):
        async with ctx.channel.typing():
            categories  = ["ass", "hmidriff", "pgif", "4k", "hentai", "holo", "hneko", "neko", "hkitsune", "kemonomimi", "anal", "hanal", "gonewild", 
                            "kanna", "ass", "pussy", "thigh", "hthigh", "gah", "coffee", "food", "paizuri", "tentacle", "boobs", "hboobs", "yaoi"]
            if not check_channel(ctx):
                await ctx.send("Le salon n'est pas marqué comme étant **NSFW**, s'il vous plaît exécuter la commande dans un salon approprié.")
            elif categorie is None:
                await ctx.send("Veuillez renseigner une catégorie!")
            elif categorie not in categories:
                categories = " | ".join(categories)
                await ctx.send(f"Catégorie demandée '{categorie}' invalide.\nVeuillez choisir une catégorie parmis celle ci-dessous:\n{categories}")
            else:
                r = requests.get(f"https://nekobot.xyz/api/image?type={categorie}")
                if r.status_code in range (200,299):
                    res = r.json()
                    em = discord.Embed(title="Tient chacal, régale toi bien!  <:handjob:846563073404829707>", timestamp = ctx.message.created_at, color = Colours.pink())
                    em.set_image(url = res.get("message"))
                    em.set_footer(text = ctx.author)
                    await ctx.send(embed = em)
                elif r.status_code == 400:
                    categories = " | ".join(categories)
                    await ctx.send(f"Catégorie demandée '{categorie}' invalide.\nVeuillez choisir une catégorie parmis celle ci-dessous:\n{categories}")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")

    @commands.command(description = "Permet d'afficher 1 image/gifs pornographiques de akaneko-api pour une catégorie de recherche spécifique.")
    async def akaneko(self, ctx, categorie: str = None):
        async with ctx.channel.typing():
            categories  = ["neko", "sfwfoxes", "wallpapers", "mobilewallpapers", "bdsm", "doujin", "femdom", "hentai", "maid", "orgy", "panties", "nsfwwallpaper", "nsfwmobileWallpapers",
                            "netorare", "gif", "blowjob", "feet", "uglybastard", "uniform", "gangbang", "foxgirl", "cumslut", "glasses", "thighs", "tentacles", "loli", "masturbation",
                            "school", "yuri", "ryouiki"]
            if not check_channel(ctx):
                await ctx.send("Le salon n'est pas marqué comme étant **NSFW**, s'il vous plaît exécuter la commande dans un salon approprié.")
            elif categorie is None:
                await ctx.send("Veuillez renseigner une catégorie!")
            elif categorie not in categories:
                categories = " | ".join(categories)
                await ctx.send(f"Catégorie demandée '{categorie}' invalide.\nVeuillez choisir une catégorie parmis celle ci-dessous:\n{categories}")
            else:
                r = requests.get(f"https://akaneko-api.herokuapp.com/api/{categorie}")
                if r.status_code in range (200,299):
                    res = r.json()
                    em = discord.Embed(title="Tient chacal, régale toi bien!  <:handjob:846563073404829707>", timestamp = ctx.message.created_at, color = Colours.pink())
                    em.set_image(url = res.get("url"))
                    em.set_footer(text = ctx.author)
                    await ctx.send(embed = em)
                elif r.status_code == 400:
                    categories = " | ".join(categories)
                    await ctx.send(f"Catégorie demandée '{categorie}' invalide.\nVeuillez choisir une catégorie parmis celle ci-dessous:\n{categories}")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")
                    
    @commands.command(description = "Permet d'afficher 1 gifs pornographiques de redgifs.com pour une clé de recherche spécifique.")
    async def redgifs(self, ctx, keyword: str = None):
        async with ctx.channel.typing():
            if not check_channel(ctx):
                await ctx.send("Le salon n'est pas marqué comme étant **NSFW**, s'il vous plaît exécuter la commande dans un salon approprié.")
            elif keyword is None:
                await ctx.send("Veuillez renseigner un mot-clé!")
            else:
                r = requests.get(f"https://api.redgifs.com/v1/gfycats/search?search_text={keyword}&count=250&order=trending")
                if r.status_code in range (200,299):
                    try:
                        res = r.json()
                        url_gifs = res["gfycats"]
                        i = random.randint(0,len(url_gifs))
                        url_gif = url_gifs[i]["max5mbGif"]
                        url_mp4 = url_gifs[i]["mp4Url"]
                        em = discord.Embed(title="Tient chacal, régale toi bien!  <:handjob:846563073404829707>", description = url_mp4, timestamp = ctx.message.created_at, color = Colours.pink())
                        em.set_image(url = url_gif)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                        await ctx.send(url_mp4)
                    except IndexError:
                        await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")
            

def setup(bot):
	bot.add_cog(nsfw(bot))