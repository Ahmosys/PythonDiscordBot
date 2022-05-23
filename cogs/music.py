import discord
import asyncio


from discord.ext import commands
from youtube_dl import YoutubeDL
from ext.colours import Colours


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = None
        self.volume = 1.0
        self.queue = {}
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                if "youtube" in item: # If user send link
                    info = ydl.extract_info(item, download=False)
                else: #If user send keyword
                    info = ydl.extract_info(f"ytsearch:{item}", download=False)['entries'][0]
                return {'source': info['formats'][0]['url'], 'title': info['title']}
            except Exception:
                return False # If some errors happen return False
    
    def play_song(self):
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(list(self.queue.values())[0]), volume=self.volume)
        def next(_):
            if len(self.queue) > 1:
                self.queue.pop(list(self.queue.keys())[0])
                self.play_song()
            else:
                asyncio.run_coroutine_threadsafe(self.vc.disconnect(), self.bot.loop)
                self.queue = {}
        self.vc.play(source, after=next)
    
    @commands.command(description = "Permet de jouer une musique dans un salon vocal.")
    async def play(self, ctx, *args):
        ctx_voice = ctx.message.author.voice
        query = " ".join(args)
        if ctx_voice is None:
            await ctx.send("Vous devez être connecter à un salon vocal pour effectuer cette commande!")
            return
        elif not query:
            await ctx.send("Veuillez renseigner un lien ou un mot clé!")
            return
        elif self.vc is None or not self.vc.is_connected():
            self.vc = await ctx_voice.channel.connect()
        elif self.vc.channel != ctx_voice.channel:
            print("Pas même channel que ctx")
            await self.vc.move_to(ctx_voice.channel)
        ytb_dl = self.search_yt(query)
        if ytb_dl == False:
            await ctx.send("Lien ou mot clé invalide!")
        elif self.vc.is_playing():
            await ctx.send("Le bot est déjà entrain de jouer du son, j'ajoute le son à la queue!")
            self.queue[list(ytb_dl.values())[1]] = list(ytb_dl.values())[0] # Add to queue dict
        else:
            self.queue[list(ytb_dl.values())[1]] = list(ytb_dl.values())[0]
            await ctx.send(f"Je lance la musique : {list(self.queue.keys())[0]}")
            self.play_song()
    
    @commands.command(description = "Permet de déconnecter le bot du salon vocal.")
    async def dc(self, ctx):
        ctx_voice = ctx.message.author.voice
        if ctx_voice is None:
            await ctx.send("Vous devez être connecter à un salon vocal pour effectuer cette commande!")
        elif self.vc is None or not self.vc.is_connected():
            await ctx.send("Vous ne pouvez pas déconnecter le bot car celui-ci n'est pas connecté à un salon vocal!")
        elif self.vc.channel != ctx_voice.channel:
            await ctx.send("Vous ne pouvez pas déconnecter le bot car vous n'êtes pas dans le même salon vocal que lui!")
        else:
            self.queue = {}
            await self.vc.disconnect()
            
    @commands.command(description = "Permet de mettre en pause la musique en cours d'écoute.")
    async def pause(self, ctx):
        if self.vc is None or not self.vc.is_connected():
            await ctx.send("Vous ne pouvez pas mettre en pause le bot car celui-ci n'est pas connecté à un salon vocal!")
        elif self.vc.is_paused():
            await ctx.send("Le son est déjà en pause!")
        elif not self.vc.is_playing():
            await ctx.send("Actuellement, aucun son n'est en cours de lecture!")
        else:
            self.vc.pause()
            
    @commands.command(description = "Permet de lire la musique précédemment mis en pause.")
    async def resume(self, ctx):
        if self.vc is None or not self.vc.is_connected():
            await ctx.send("Vous ne pouvez pas mettre reprendre la lecture car le bot car le bot n'est pas connecté à un salon vocal!")
        elif not self.vc.is_paused():
            await ctx.send("Actuellement, aucun son est en pause!")
        else:
            self.vc.resume()
    
    @commands.command(description = "Permet de passer la musique.")
    async def skip(self, ctx):
        if self.vc is None or not self.vc.is_connected():
            await ctx.send("Vous ne pouvez pas skip le son car le bot n'est pas connecté à un salon vocal!")
        elif not self.vc.is_playing():
            await ctx.send("Actuellement, aucun son n'est en cours de lecture!")
        else:
            self.vc.stop()
            await ctx.send("Je passe au prochain son de la queue!")
    
    @commands.command(description = "Permet de définir le volume du son sortant.")
    async def setvol(self, ctx, *, volume : float  = None):
        if volume is None:
            await ctx.send("Veuillez spécifier un volume!")
        elif volume > 100 or volume < 1:
            await ctx.send("Veuillez spécifier une valeur entre 1 et 100!")
        else:
            self.volume = volume / 100
            await ctx.send(f"Le son a bien été défini sur {volume}%")
    
    @commands.command(description = "Permet d'afficher les sons en liste d'attente")
    async def queue(self, ctx):
        em = discord.Embed(title = "File d'attente | Music", color = Colours.green(), timestamp = ctx.message.created_at)
        em.set_footer(text = ctx.author)
        if (len(self.queue) <= 1):
            await ctx.send("Aucun son dans la file d'attente !")
        else:
            for i, (titre) in enumerate(self.queue.keys()):
                em.add_field(name = f"Position - {i}", value = f"```{titre}```", inline = False)
            await ctx.send(embed = em)

def setup(bot):
	bot.add_cog(music(bot))