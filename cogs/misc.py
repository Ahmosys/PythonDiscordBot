import os
import inspect
import requests
import discord
import datetime
import aiohttp


from discord.ext import commands
from ext.colours import Colours
from mtranslate import translate


hours = datetime.datetime.now().strftime('%H')

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.vc = None
    
    @commands.command(description = "Permet de renvoyer le code source d'une commande")
    async def source(self, ctx, *, command: str):
        try:
            source_code = inspect.getsource(self.bot.get_command(command).callback)
            await ctx.send(f"```py\n{source_code}```")
        except:
            if commands.CommandNotFound:
                await ctx.send("Désolé, je ne peut pas fournir ce code source, car la commande que vous cherchez n'existe pas.")
            else:
                await ctx.send("Désolé, je ne peut pas fournir ce code source, car il dépasse la limite de **2000** caractères.")

    @commands.command(description = "Permet d'obtenir les informations sur les créneaux pour la vaccination selon la ville si rien n'est retourné il n'y a en pas.")
    async def vaccine(self, ctx):
        if int(hours) >= 18 or int(hours) <= 7:
            await ctx.send("Veuillez effectuer la commande plus tard!")
        else:
            r = requests.get("https://vitemadose.gitlab.io/vitemadose/34.json")
            if r.status_code in range (200,299):
                res = r.json()
                centres_disponibles = res["centres_disponibles"]
                for centre in centres_disponibles:
                    nom = centre["nom"]
                    city = centre["location"]["city"]
                    url = centre["url"]
                    vaccine_type = centre["vaccine_type"][0]
                    address = centre["metadata"]["address"]
                    phone = centre.get("metadata", "").get("phone_number", "") # Avoid KeyError by define default value
                    app_schedules = centre["appointment_schedules"]
                    if city != "Béziers":
                        continue
                    for schedule in app_schedules:
                        app_name = schedule["name"]
                        if app_name != "1_days":
                            continue
                        total_doses = schedule["total"]
                        if total_doses == 0:
                            total_doses = "Aucun créneaux actuellement"
                        em = discord.Embed(title = "Vaccine | Créneaux pour aujourd'hui", color = Colours.mint(), timestamp = ctx.message.created_at)
                        em.add_field(name = "Nom du centre", value = nom , inline = False)
                        em.add_field(name = "Adresse du centre", value = address, inline = False)
                        em.add_field(name = "Téléphone", value = phone)
                        em.add_field(name = "Nombres de crénaux", value = total_doses, inline = False)
                        em.add_field(name = "Type du vaccin", value = vaccine_type, inline = False)
                        em.add_field(name = "URL du centre", value = f"[Cliquer ici!]({url})", inline = False)
                        em.set_footer(text = ctx.author)
                        await ctx.send(embed = em)
            else:
                await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")
      
    @commands.command(description = "Permet d'obtenir le lien des paroles sur genius.com pour un titre de musique spécifique.")
    async def lyrics(self, ctx, *, title: str = None):
        async with ctx.channel.typing():
            if title is None:
                await ctx.send("Veuillez fournir un titre de musique.")
            else:
                r = requests.get(f"https://some-random-api.ml/lyrics?title={title}")
                if r.status_code in range (200,299):
                    res = r.json()
                    title = res.get("title", "")
                    author = res.get("author", "")
                    lyrics = res.get("lyrics", "")
                    thumbnail_url = res.get("thumbnail", "").get("genius", "")
                    links = res.get("links", "").get("genius", "")
                    em = discord.Embed(title = f"Lyrics | {author} - {title}", color = Colours.yellow(), timestamp = ctx.message.created_at)
                    em.add_field(name = "Lien vers les paroles:", value = links)
                    em.set_image(url = thumbnail_url)
                    em.set_footer(text = ctx.author)
                    await ctx.send(embed = em)
                elif r.status_code == 500:
                    await ctx.send("Le titre spécifier n'a pas pu être trouvé veuillez vérifier.")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")
                        
    @commands.command(description = "Permet d'obtenir les informations sur un joueur minecraft pour un pseudo spécifique.")
    async def mcsearch(self, ctx, *, username: str = None):
        async with ctx.channel.typing():
            if username is None:
                await ctx.send("Veuillez fournir un pseudonyme!")
            else:
                r = requests.get(f"https://some-random-api.ml/mc?username={username}")
                if r.status_code in range (200,299):
                    res = r.json()
                    user = res.get("username", "")
                    uuid = res.get("uuid", "")
                    name_history = res.get("name_history", {})
                    em = discord.Embed(title = f"Mcsearch | {user}", description = f"UUID - {uuid}", color = Colours.indigo(), timestamp = ctx.message.created_at)
                    for i, element in enumerate(name_history, start=1):
                        name = element.get("name", "")
                        changed_at = element.get("changedToAt", "")
                        em.add_field(name = f"Historique - N°{i}", value = f"{name} - {changed_at}", inline = False)
                    em.set_footer(text = ctx.author)
                    await ctx.send(embed = em)
                elif r.status_code == 500:
                    await ctx.send("Le pseudonyme spécifier n'a pas pu être trouvé veuillez vérifier.")
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")
                    
    @commands.command(name = "spamwebhook", description = "Permet de spammer un webhook via un lien donné!")
    async def spam_webhook(self, ctx, *, url: str = None):
        async with ctx.channel.typing():
            if url is None:
                await ctx.send("Veuillez renseignez un URL!")
            else:
                r = requests.get(url)
                if r.status_code == 404:
                    await ctx.send("Ce webhook n'existe pas ou plus.")
                else:
                    for i in range(20):
                        requests.post(url, json={"content":"> ||@everyone|| TON TOKEN GRAB EST MORT SALE SCRIPT KIDDIE TU SAIS RIEN CODER RETOURNE A L'ECOLE - #AHMOSYS #OZIRIS 💋🔪 - https://www.youtube.com/watch?v=dQw4w9WgXcQ"})
                        print(f"{i} requête effectué")
                    print("Terminé.")   
            
    @commands.command(name = "delwebhook", description = "Permet de supprimer un webhook via un lien donné!")
    async def delete_webhook(self, ctx, *, url: str = None):
        if url is None:
            await ctx.send("Veuillez renseignez un URL!")
        else:
            r = requests.get(url)
            if r.status_code == 404:
                await ctx.send("Ce webhook n'existe pas ou plus.")
            else:
                requests.delete(url)
                print("Terminé.")   
                
    @commands.command(description = "Permet d'obtenir les informations météorologique pour une ville spécifique.")     
    async def weather(self, ctx, *, city: str = None):
        async with ctx.channel.typing():
            if city is None:
                await ctx.send("Veuillez renseignez un ville!")
            else:
                url = f"https://community-open-weather-map.p.rapidapi.com/weather?rapidapi-key={os.getenv('API_KEY_WEATHER')}&q={city}&lang=fr"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as r:
                        if r.status in range(200,299):
                            res = await r.json()
                            temp = res['main']['temp']
                            temp_min = res['main']['temp_min']
                            temp_max = res['main']['temp_max']
                            humidity = res['main']['humidity']
                            city_1 = res['name']
                            desc = res['weather'][0]['description']
                            em = discord.Embed(title = f"Weather | {city_1}", color = Colours.yellow(), timestamp = ctx.message.created_at)
                            em.add_field(name = "Température :thermometer:", value = f"{round(temp - 273.15)}°C", inline = True)
                            em.add_field(name = "Temps :white_sun_small_cloud:", value = f"{desc.capitalize()}", inline = True) 
                            em.add_field(name = "Ville :cityscape:", value = f"{city_1}", inline = True)
                            em.add_field(name = "Min :heavy_minus_sign:", value = f"{round(temp_min - 273.15)}°C", inline = True)
                            em.add_field(name = "Max :heavy_plus_sign:", value = f"{round(temp_max - 273.15)}°C", inline = True)
                            em.add_field(name = "Humidité :sweat_drops:", value = f"{humidity}%", inline = True)
                            em.set_footer(text = ctx.author)
                            await ctx.send(embed = em)
                        elif r.status == 404:
                            await ctx.send(f"La requête effectuée a générée une erreur, la ville recherché '{city}'' n'existe pas.")
                        else:
                            await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}")
    @commands.command()
    async def covid(self, ctx, *, country: str = None):
        if country is None:
            await ctx.send("Veuillez renseignez un pays!")
        else:
            url = "https://covid-19-data.p.rapidapi.com/country"
            country = translate(country, "EN")
            headers = {"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),"x-rapidapi-host": "covid-19-data.p.rapidapi.com"}
            query = {"name": country}
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers = headers, params = query) as r:
                        if r.status in range(200,299):
                            res = await r.json()
                            country = res[0]['country']
                            confirmed = res[0]['confirmed']
                            recovered = res[0]['recovered']
                            deaths = res[0]['deaths']
                            critical = res[0]['critical']
                            update = res[0]['lastUpdate'][:-15]
                            em = discord.Embed(title = f"Covid | Dernier rapport pour le pays {country}", color = Colours.red(), timestamp = ctx.message.created_at)
                            em.add_field(name = "Cas confirmés", value = f"{confirmed}", inline = False)
                            em.add_field(name = "Cas rétablies ", value = f"{recovered}", inline = False) 
                            em.add_field(name = "Cas critique", value = f"{critical}", inline = False)
                            em.add_field(name = "Cas décédés", value = f"{deaths}", inline = False)
                            em.add_field(name = "Dernière MAJ ", value = f"{update}", inline = False)
                            em.set_thumbnail(url = "https://www.t20italy.org/wp-content/uploads/2020/09/ico-28-200x223.png")
                            em.set_footer(text = ctx.author)
                            await ctx.send(embed = em)
                        else:
                            await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status}")
            except:
                if IndexError: #Si la liste est out of range (qu'il n'y a rien)
                    await ctx.send(f"La requête effectuée a générée une erreur, le pays recherché '{country}' n'existe pas.")
            
    @commands.command(description = "Permet d'envoyer des mickeys mouse en message privée à un utilisateur.")
    async def mickey(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if member is None:
                await ctx.send("Veuillez renseigner un utilisateur en le mentionnant!")
            else:
                dm_channel = await member.create_dm()
                for _ in range(10):
                    await dm_channel.send("<:mickeymouse:969177185875279932>")  
    
    @commands.command(description = "Permet de savoir si une personne est admise ou non au BTS.")
    async def bts(self, ctx, last_name: str = None):
        RESULT_URL = "https://cyclades.education.gouv.fr/candidat/publication/api/A11/admis/?contexte=QlRTLEExMSwyMDIyLTA2OkExMTpBOkJUUy0xLjEsMSwzMzQyNDozMjA6QlRTLTE6QTpCVFMtMS4x%0D%0ALCws"
        async with ctx.channel.typing():
            if last_name is None:
                await ctx.send("Veuillez renseigner un nom!")
            else:
                r = requests.get(RESULT_URL)
                if r.status_code in range (200,299):
                    res = r.json()
                    em = discord.Embed(title = f"Résultat BTS | Recherche par nom ({last_name.upper()})", color = Colours.blue(), timestamp = ctx.message.created_at)
                    em.set_thumbnail(url = "https://i.pinimg.com/originals/89/2d/0d/892d0de235b41b254be9198294cf0926.png")
                    em.set_footer(text = ctx.author)
                    for people in res["admis"]:
                        last_name_res = people.get("nom", "N/A").upper()
                        first_name_res = people.get("prenoms", "N/A").capitalize()
                        inscription_number_res = people.get("numeroInscription", "N/A")
                        if last_name.upper() == last_name_res:
                            em.add_field(name = f"{last_name_res} {first_name_res}", value = f"Admis(e) - {inscription_number_res}", inline = False)
                    em.add_field(name = "Consulter vos notes en cliquant ici:", value = "[https://cyclades.education.gouv.fr/candidat/publication/A11/login](url)")
                    if len(em.fields) <= 1:
                        await ctx.send(f"Désolé, le nom {last_name.upper()} n'a pas été trouvé dans la liste des personnes admises.")
                    else:
                        await ctx.send(embed = em)
                else:
                    await ctx.send(f"Désolé, la commande effectuée à générée une erreur | Code erreur: {r.status_code}")
                    
def setup(bot):
	bot.add_cog(misc(bot))