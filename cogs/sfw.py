import os
import aiohttp
import discord


from discord.ext import commands
from ext.colours import Colours


class sfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(description = "Permet d'afficher 1 image de unsplash.com pour une catégorie de recherche spécifique.")
    async def unsplash(self, ctx, *, keyword: str = None):
        async with ctx.channel.typing():
            if keyword is None:
                await ctx.send("Veuillez renseigner un mot-clé!")
            else:
                keyword = keyword.replace(" ", "")
                url = f"https://api.unsplash.com/photos/random/?query={keyword}&orientation=landscape&client_id={os.getenv('API_KEY_UNSPLASH')}"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as r:
                        if r.status in range(200,299):
                            res = await r.json()
                            url = res["urls"]["regular"]
                            em = discord.Embed(title = f"Unsplash | {keyword.title()} ", color = Colours.green(), timestamp = ctx.message.created_at)
                            em.set_image(url = url)
                            em.set_footer(text = ctx.author)
                            await ctx.send(embed = em)
                        elif r.status == 404:
                            await ctx.send(f"La requête effectuée a générée une erreur, le mot recherché '{keyword}' n'existe pas.")
                        else:
                            await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}")
                            
    @commands.command(description="Permet de modifier un avatar en y ajoutant le filtre gay.")
    async def gay(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='png', size=1024)}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        em = discord.Embed(title = "Gay filter", color = Colours.indigo(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                         
    @commands.command(description="Permet de modifier un avatar en y ajoutant le filtre jpeg.")
    async def jpeg(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=jpeg&url={member.avatar_url_as(format='png', size=1024)}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Jpeg filter", color = Colours.indigo(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                                
    @commands.command(description="Permet de modifier un avatar en y ajoutant le filtre deepfry.")
    async def deepfry(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=deepfry&image={member.avatar_url_as(format='png', size=1024)}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Deepfry filter", color = Colours.indigo(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                
    @commands.command(description="Permet de modifier un avatar en y ajoutant le filtre blurpify.")
    async def blurpify(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=blurpify&image={member.avatar_url_as(format='png', size=1024)}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Blurpify filter", color = Colours.indigo(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                       
    @commands.command(description="Permet de modifier un avatar en y ajoutant le filtre magik.")
    async def magik(self, ctx, member: discord.Member = None, *, intensity: int = 5):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            if intensity > 10:
                await ctx.send(f"Désolé, l'intensité doit être comprise en **0** et **10**.") 
            else:
                url = f"https://nekobot.xyz/api/imagegen?type=magik&image={member.avatar_url_as(format='png', size=1024)}&intensity={intensity}"
                url = str(url).replace(".webp", ".jpg")
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as r:
                        if r.status in range(200,299):
                            res = await r.json()
                            url = res["message"]
                            em = discord.Embed(title = "Magik filter", color = Colours.indigo(), timestamp = ctx.message.created_at)
                            em.set_image(url = url)
                            em.set_footer(text = ctx.author)
                            await ctx.send(embed = em)
                        else:
                            await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                    
    @commands.command(description="Permet de modifier un avatar en y ajoutant le filtre jail.")
    async def jail(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://some-random-api.ml/canvas/jail/?avatar={member.avatar_url_as(format='png', size=1024)}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        em = discord.Embed(title = "Aller hop, au goulag fdp.", color = Colours.indigo(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                         
    @commands.command(description="Permet de modifier un avatar en y ajoutant le filtre glass.")
    async def glass(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://some-random-api.ml/canvas/glass/?avatar={member.avatar_url_as(format='png', size=1024)}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        em = discord.Embed(title = "Glass filter", color = Colours.indigo(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                      
    @commands.command(description="Permet de modifier un avatar en y ajoutant le filtre wasted.")
    async def wasted(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://some-random-api.ml/canvas/wasted/?avatar={member.avatar_url_as(format='png', size=1024)}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        em = discord.Embed(title = "Wasted filter", color = Colours.indigo(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
    
    @commands.command(description = "Permet de modifier un avatar en y ajoutant le filtre choisi.")
    async def filter(self, ctx, member: discord.Member = None, *, filter: str = None):
        async with ctx.channel.typing():
            possible_filter = ["greyscale", "invert", "brightness", "threshold", "sepia", "red", "green", "blue", "blurple", "pixelate", "blur"]
            if member is None:
                await ctx.send("Veuillez renseigner un membre!")
            elif filter is None:
                await ctx.send("Veuillez renseigner un filtre!")
            else:
                url = f"https://some-random-api.ml/canvas/{filter}/?avatar={member.avatar_url_as(format='png', size=1024)}"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as r:
                        if r.status in range(200,299):
                            em = discord.Embed(title = f"{filter.capitalize()} filter", color = Colours.indigo(), timestamp = ctx.message.created_at)
                            em.set_image(url = url)
                            em.set_footer(text = ctx.author)
                            await ctx.send(embed = em)
                        elif r.status == 404:
                            possible_filter = " | ".join(possible_filter)
                            await ctx.send(f"La requête effectuée a générée une erreur, le filtre utilisé '{filter}' n'existe pas.\nVeuillez choisir un filtre parmis celle ceux ci-dessous:\n{possible_filter}")
                        else:
                            await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}")
                                          
    @commands.command(description="Permet d'appliquer le meme wolverine sur un avatar donné.")
    async def wolverine(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://vacefron.nl/api/wolverine?user={member.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        em = discord.Embed(title = "Wolverine meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                           
    @commands.command(description="Permet d'appliquer le meme wolverine sur un texte donné.")
    async def pancarte(self, ctx, *, text: str):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=fact&text={text}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Pancarte meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                        
    @commands.command(description="Permet d'appliquer le meme baguette sur un avatar donné.")
    async def baguette(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=baguette&url={member.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Baguette meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                        
    @commands.command(description="Permet d'appliquer le meme menace sur un avatar donné.")
    async def menace(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=threats&url={member.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Menace meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                                  
    @commands.command(description="Permet d'appliquer le meme clyde sur un texte donné.")
    async def clyde(self, ctx, *, text: str):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Clyde meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                       
    @commands.command(description="Permet d'appliquer le meme awoify sur un avatar donné.")
    async def awoify(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=awooify&url={member.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Awoify meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                        
    @commands.command(description="Permet d'appliquer le meme ship sur deux avatar donné.")
    async def ship(self, ctx, member1: discord.Member = None, member2: discord.Member = None):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={member1.avatar_url}&user2={member2.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Ship meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}")
                         
    @commands.command(description="Permet d'appliquer le meme captcha sur un avatar donné.")
    async def captcha(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=captcha&url={member.avatar_url}&username={member.name}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Captcha meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                        
    @commands.command(name="www", description="Permet d'appliquer le meme who would win sur deux avatar donné.")
    async def who_would_win(self, ctx, member1: discord.Member = None, member2: discord.Member = None):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={member1.avatar_url}&user2={member2.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Who would win meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}")
                        
    @commands.command(name="chmymind", description="Permet d'appliquer le meme change my mind sur un texte donné.")
    async def change_my_mind(self, ctx, *, text: str):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Change my mind meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                                             
    @commands.command(description="Permet d'appliquer le meme lolice sur un avatar donné.")
    async def lolice(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=lolice&url={member.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Lolice meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                        
    @commands.command(description="Permet d'appliquer le meme kannagen sur un texte donné.")
    async def kannagen(self, ctx, *, text: str):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Kannagen meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                         
    @commands.command(name="trumptweet", description="Permet d'appliquer le meme trump tweet sur un texte donné.")
    async def trump_tweet(self, ctx, *, text: str):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Trump tweet meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                          
    @commands.command(description="Permet d'appliquer le meme tweet sur un avatar et un texte donné.")
    async def tweet(self, ctx, twitter_username: str, *, text: str):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={twitter_username}&text={text}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Trump tweet meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                       
    @commands.command(name="phcomment", description="Permet d'appliquer le meme phcomment sur un avatar et un texte donné.")
    async def ph_comment(self, ctx, member: discord.Member, *, text: str):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=phcomment&image={member.avatar_url}&text={text}&username={member.name}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Ph comment meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                      
    @commands.command(description="Permet d'appliquer le meme stickbug sur un avatar donné.")
    async def stickbug(self, ctx, member : discord.Member):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=stickbug&url={member.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Stickbug meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_footer(text = ctx.author)
                        await ctx.send(text = url)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                         
    @commands.command(description="Permet d'appliquer le meme iphonex sur un avatar donné.")
    async def iphonex(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=iphonex&url={member.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "iPhone X meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 
                         
    @commands.command(description="Permet d'appliquer le meme trap sur deux avatar donné.")
    async def trap(self, ctx, member1: discord.Member = None, member2: discord.Member = None):
        async with ctx.channel.typing():
            url = f"https://nekobot.xyz/api/imagegen?type=trap&name={member2.name}&author={member1.name}&image={member2.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Trap meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}")
                        
    @commands.command(description="Permet d'appliquer le meme trash sur un avatar donné.")
    async def trash(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if not member:
                member = ctx.message.author
            url = f"https://nekobot.xyz/api/imagegen?type=trash&url={member.avatar_url}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    if r.status in range(200,299):
                        res = await r.json()
                        url = res["message"]
                        em = discord.Embed(title = "Trash meme", color = Colours.pink(), timestamp = ctx.message.created_at)
                        em.set_image(url = url)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
                    else:
                        await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}") 


def setup(bot):
	bot.add_cog(sfw(bot))