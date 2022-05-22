import discord
import asyncio

from discord.ext import commands, tasks
from discord.errors import NotFound


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.member_voice = 0
        self.saved_roles = {}
        
    
    @tasks.loop(seconds=1)
    async def check_voice(self):
        member = self.bot.get_guild(676916551009697832).get_member(self.member_voice)
        if member.voice is not None:
            await member.move_to(None)
    
    @commands.command(description="Permet de démarrer la tâche vérifiant qu'un membre parle.", name="startvoice")
    async def start_task_voice(self, ctx, member : discord.Member = None):
        async with ctx.channel.typing():
            if member is None:
                await ctx.send("Veuillez mentionné un membre!")
            elif member.id == 283954969416302592:
                await ctx.author.move_to(None)
                await ctx.send("Tu ne peux pas déconnecter ce membre.")
            else:
                self.member_voice = member.id
                self.check_voice.start()
    
    @commands.command(description="Permet d’arrêter la tâche vérifiant qu'un membre parle.", name="stopvoice")
    async def stop_task_voice(self, ctx):
        async with ctx.channel.typing():
            if self.member_voice == ctx.author.id:
                await ctx.send("Tu ne peux pas arrêter toi-même cette commande, car tu es la cible.")
            else:
                self.check_voice.stop()
    
    @commands.command(description = "Permet d'effacer un nombre de messages donné dans un salon textuel.")
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, number: int = 100):
        async with ctx.channel.typing():
            if (number > 100 or number == 0):
                await ctx.send("Je ne peut pas effectuer cette commande, vous devez renseigner un nombre entre **1** et **100**.")
            else:
                deleted = await ctx.channel.purge(limit = number)
                await ctx.channel.send(f"**{len(deleted)}** messages supprimés, tout clean {ctx.author.mention}", delete_after=5)
    
    @commands.command(name = "clearexceptpin", description = "Permet d'effacer un nombre de messages donné dans un salon textuel sans toucher aux messages épinglés.")
    @commands.has_permissions(manage_messages = True)
    async def clear_except_pin(self, ctx, number: int = 100):
        async with ctx.channel.typing():
            if (number > 100 or number == 0):
                await ctx.send("Je ne peut pas effectuer cette commande, vous devez renseigner un nombre entre **1** et **100**.")
            else:
                deleted = await ctx.channel.purge(limit = number, check = lambda msg: not msg.pinned)
                await ctx.channel.send(f"**{len(deleted)}** messages supprimés, tout clean {ctx.author.mention}", delete_after=5)
    
    @commands.command(name = "clonechannel", description = "Permet de cloner un salon textuel donné.")
    @commands.has_permissions(manage_channels = True)
    async def clone_channel(self, ctx, text_channel: discord.TextChannel = None):
            if not text_channel:
                text_channel = ctx.channel
            message = await ctx.send(f"Le clonage du salon '{text_channel.name}' va être éffectué vous perdrez vos **épinglés** ainsi que les **messages**."
                                                        + "\nVeuillez valider en réagissant avec ✅ sinon annulé en réagissant avec ❌.")
            await message.add_reaction("✅")
            await message.add_reaction("❌")
            def check_reaction(reaction, user):
                return ctx.message.author == user and message.id == reaction.message.id and str(reaction.emoji) in {"✅", "❌"}
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout = 10, check = check_reaction)
                if reaction.emoji == "✅":
                    await message.delete()
                    current_channel = text_channel
                    new_channel = await current_channel.clone(name = current_channel.name, reason = "Clonage salon")
                    await current_channel.delete()
                    await new_channel.send(f"J'ai bien cloné le salon textuel '{new_channel.name}' {ctx.author.mention}.", delete_after=5)
                else:
                        await message.delete()
                        await ctx.send(f"J'ai bien annulé le clonage du salon {ctx.author.mention}.")
            except asyncio.TimeoutError:
                await message.delete()
                await ctx.send(f"Temps écoulé, j'ai annulé le clonage du salon {ctx.author.mention}.")
    @clone_channel.error
    async def clone_channel_error(self, ctx, error):
        if isinstance (error, commands.ChannelNotFound):
            await ctx.send("Désolé, le channel mentionné n'a pas été trouvé, veuillez vérifier et réitérer.")

    @commands.command(name = "enablensfw", description = "Permet d'activer le marquage NSFW sur un salon textuel donné.")
    @commands.has_permissions(manage_channels = True)
    async def enable_nsfw(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send("Ce channel est déjà marqué comme étant NSFW.\nSi vous voulez enlever ce marquage taper **!disablensfw**.")
        else:
            await ctx.channel.edit(nsfw = True)
            await ctx.send(f"J'ai bien changé ce channel '{ctx.channel.name}' en **NSFW**.", delete_after = 5)

    @commands.command(name="disablensfw", description = "Permet de désactiver le marquage NSFW sur un salon textuel donné.")
    @commands.has_permissions(manage_channels = True)
    async def disable_nsfw(self, ctx):
        if not ctx.channel.is_nsfw():
            await ctx.send("Ce channel est déjà marqué comme étant NON NSFW.")
        else:
            await ctx.channel.edit(nsfw = False)
            await ctx.send(f"J'ai bien changé ce channel '{ctx.channel.name}' en **NON NSFW**.", delete_after = 5)

    @commands.command(description = "Permet de sauvegarder les rôles assignés à un membre.")
    @commands.has_permissions(manage_roles = True)
    async def savestate(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Veuillez mentionné le membre dont vous voulez sauvegarder les rôles.")
        self.saved_roles[member.id] = member.roles[1:]
        await ctx.send(f"Les rôles de {member.name} ont bien été sauvegardés.")

    @commands.command(description = "Permet d'attribuer les rôles savegardés auparavant à un membre.")
    @commands.has_permissions(manage_roles = True)
    async def loadstate(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Veuillez mentionné le membre dont vous voulez restitué restituer les rôles.")
        await member.add_roles(*self.saved_roles[member.id])
        await ctx.send(f"Les rôles de {member.name} ont bien été restitués.")
    
    @commands.command(name="unpinall", description = "Permet de désépingler les épinglés d'un salon textuel.") 
    @commands.has_permissions(manage_channels = True)     
    async def unpin_all(self, ctx):
        pins = await ctx.channel.pins()
        if len(pins) > 0:
            for i in pins:
                await i.unpin()
            await ctx.send("J'ai bien supprimé tout les épinglés.")
        else:
            await ctx.send("Désolé, ce salon textuel ne comporte pas de messages épinglés.")

    @commands.command(name="createinv", description = "Permet de crée une invitation de serveur.")
    @commands.has_permissions(create_instant_invite = True)
    async def create_guild_invite(self, ctx, time_in_seconds: int = 3600 , uses: int = 10, *, reason: str = "Invitation crée via bot."):
        if (uses > 100 or uses == 0):
            await ctx.send("Je ne peut pas effectuer cette commande, vous devez renseigner un nombre d'utilisation entre **1** et **100**.")
        invite_link = await discord.abc.GuildChannel.create_invite(ctx.message.channel, max_uses = uses, max_age = time_in_seconds, reason = reason)
        await ctx.send(f"Voici votre lien d'invitation: {invite_link}")

    @commands.command(name="delinv", description = "Permet de supprimer une invitation de serveur donné.")
    @commands.has_permissions(create_instant_invite = True)
    async def delete_guild_invite(self, ctx, invite_url: str = None):
        if invite_url is None:
            await ctx.send("Veuillez fournir l'url ou l'id d'invitation!")
        try:
            invite = await self.bot.fetch_invite(invite_url)
            invite_id = invite.id
            await invite.delete()
            await ctx.send(f"L'invitation '{invite_id}' à bien été supprimée.")
        except NotFound:
            await ctx.send(f"Le lien ou l'id d'invitation fournis '{invite_url}' n'est pas valide.")

    @commands.command(name = "slowmode", description = "Permet d'activer/désactiver le mode lent d'un salon textuel en fournissant un temps en secondes.")
    @commands.has_permissions(manage_channels = True)
    async def slow_mode_delay(self, ctx, delay_in_seconds : int = 60):
        if delay_in_seconds > 21600:
            await ctx.send("Le délai maximal est de 6h soit 21600 secondes veuillez fournir un délai entre 0 et 21600 secondes.")
        elif delay_in_seconds == 0:
            if ctx.channel.slowmode_delay == 0:
                await ctx.send("Le mode lent de ce salon textuel est déjà désactivé!")
            else:
                await ctx.channel.edit(slowmode_delay = delay_in_seconds)
                await ctx.send("J'ai bien désactive le mode lent pour ce salon textuel.", delete_after = 5)
        else:
            await ctx.channel.edit(slowmode_delay = delay_in_seconds)
            await ctx.send(f"J'ai bien changé ce channel '{ctx.channel.name}' en mode lent avec un délai de {delay_in_seconds} secondes.", delete_after = 5)

    @commands.command(description = "Permet d'expulser un membre du serveur.")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member = None, *, reason: str = "Aucune raison"):
        if member is None:
            await ctx.send("Veuillez mentionner le membre devant être expluser!")
        await member.kick(reason = reason)
        await ctx.send(f"Le membre {member.name} à été expulsé(e) par {ctx.author.mention} pour la raison: {reason}")
        
    @commands.command(description = "Permet de déconnecter un membre du serveur.")
    async def disconnect(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if member is None:
                await ctx.send("Veuillez mentionner le membre devant être déconnecter!")
            elif member.voice is None:
                await ctx.send("Le membre doit être connecté à un salon vocal pour pouvoir le déconnecter!")
            elif member.id == 283954969416302592:
                await ctx.send("Tu ne peux pas déconnecter ce membre.")
            else:      
                await member.move_to(None)
                dm_channel = await member.create_dm()
                for _ in range (5):
                    await dm_channel.send("Nique ta mère HOHO ! <:mickeymouse:969177185875279932>")

    @commands.command(description = "Permet de bannir un membre du serveur.")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *, reason: str = "Aucune raison"):
        if member is None:
            await ctx.send("Veuillez mentionner le membre devant être banni!") 
        await member.ban(reason = reason)
        await ctx.send(f"Le membre {member.name} à été banni par {ctx.author.mention} pour la raison: {reason}")
    
    @commands.command(description = "Permet de débannir un membre du serveur.")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member = None):
        if member is None:
            await ctx.send("Veuillez mentionner le membre devant être débanni!")
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user} à bien été débanni!")

    @commands.command(name = "guildowner", description = "Permet d'obtenir le profil discord du propriétaire du serveur.")
    async def guild_owner(self, ctx):
        await ctx.send(f"Le propriétaire du serveur {ctx.guild.name} est: {ctx.guild.owner.mention} dites-lui merci ! :heart:")
        
    
def setup(bot):
	bot.add_cog(moderation(bot))