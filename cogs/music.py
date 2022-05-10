import discord


from discord.ext import commands
from youtube_dl import YoutubeDL


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = None
        self.volume = 1.0
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                if "youtube" in item: # If user send link
                    info = ydl.extract_info(item, download=False)
                else: #If user send keyword
                    info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
                return {'source': info['formats'][0]['url'], 'title': info['title']}
            except:
                return False # If some errors happen return False
    
    @commands.command(description = "Permet de jouer une musique dans un salon vocal.")
    async def play(self, ctx, *args):
        ctx_voice = ctx.message.author.voice
        query = " ".join(args)
        
        if ctx_voice is None:
            await ctx.send("Vous devez être connecter à un salon vocal pour éffectuer cette commande!")
            return
        elif query == "":
            await ctx.send("Veuillez renseigner un lien ou un mot clé!")
            return
        elif self.vc is None or not self.vc.is_connected():
            print("Pas connecté")
            self.vc = await ctx_voice.channel.connect()
        elif self.vc.is_playing():
            await ctx.send("Le bot est déjà entrain de jouer un son!")
            return
        elif self.vc.channel != ctx_voice.channel:
            print("Pas même channel que ctx")
            await self.vc.move_to(ctx_voice.channel)
        ytb_dl = self.search_yt(query)
        if ytb_dl == False:
            await ctx.send("Lien ou mot clé invalide!")
        else:
            self.vc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(ytb_dl['source']), volume=self.volume), after=None)
            await ctx.send(f"Je lance la musique : {ytb_dl['title']}")
    
    @commands.command(description = "Permet de déconnecter le bot du salon vocal.")
    async def dc(self, ctx):
        ctx_voice = ctx.message.author.voice
        if ctx_voice is None:
            await ctx.send("Vous devez être connecter à un salon vocal pour éffectuer cette commande!")
        elif self.vc is None or not self.vc.is_connected():
            await ctx.send("Vous ne pouvez pas déconnecter le bot car celui-ci n'est pas connecté à un salon vocal!")
        elif self.vc.channel != ctx_voice.channel:
            await ctx.send("Vous ne pouvez pas déconnecter le bot car vous n'êtes pas dans le même salon vocal que lui!")
        else:
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
    
    @commands.command(description = "Permet de définir le volume du son sortant.")
    async def setvol(self, ctx, *, volume : float  = None):
        if volume is None:
            await ctx.send("Veuillez spécifier un volume!")
        elif volume > 100 or volume < 1:
            await ctx.send("Veuillez spécifier une valeur entre 1 et 100!")
        else:
            self.volume = volume / 100
            await ctx.send(f"Le son a bien été défini sur {volume}%")
    
    
def setup(bot):
	bot.add_cog(music(bot))