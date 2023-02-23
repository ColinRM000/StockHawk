import discord, discord.utils, json, asyncio, os, time, datetime
from discord.utils import get
from discord.ext import commands, tasks
from requests_html import HTMLSession
from discord.ext.commands import ConversionError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select, ButtonStyle
from PIL import Image
###############################################
#               COLOR LIST                    #
orange = 0xe67e22                             #
yellow = 0xf1c40f                             #
red = 0xe74c3c                                #
dark_red = 0x992d22                           #
blue = 0x3498db                               #
###############################################

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)


intents = discord.Intents.default()
client = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents) 
intents.members = True 
client.remove_command('help')

for filename in os.listdir('./cogs'): # COG OPENER
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print(f"{client.user.name} is online.")
    print("[!] CONSOLE LOG:")
    client.loop.create_task(status_task())
    if not image_updates.is_running():
        image_updates.start()

@client.event
async def on_guild_join(guild):
    CHH = client.get_channel(975639048175648778)
    alert = discord.Embed(title=f"🌐 SH Update:", description=f"StockHawk has joined the server {guild}!", colour= blue)
    alert.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    await CHH.send(embed=alert)

@tasks.loop(hours=1) 
async def image_updates():
    print("Updating Gainers, Losers, and Actives...")
    # Gainers.png
    s = Service(r"chromedriver")
    s.start() 
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://money.cnn.com/data/hotstocks/')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'cnnBody_Left.wsodContent')
    driver.set_window_size(650, 1131)  
    driver.save_screenshot("gains.png")
    driver.quit()
    in_file = 'gains.png'
    out_file = 'gains.png'
    img = Image.open(in_file)
    width = 650
    height = 1131
    width, height = img.size
                    #left #top  #right   #bottom
    cropped = img.crop((0, 530, width-0, height-325)) 
    cropped.save(out_file)
    CHH = client.get_channel(975652068759076884)
    alert = discord.Embed(title=f"🌐 SH Image Update:", description=f"Gainers.png has been updated.", colour= blue)
    alert.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    alert.set_footer(text=f"{datetime.datetime.now()}")
    await CHH.send(embed=alert)
    print("Gainers.png has been updated.")
    # Losers.png
    print("Updating Losers.png")
    s = Service(r"chromedriver")
    s.start() 
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://money.cnn.com/data/hotstocks/')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'cnnBody_Left.wsodContent')
    driver.set_window_size(650, 1131)  
    driver.save_screenshot("losers.png")
    driver.quit()
    in_file = 'losers.png'
    out_file = 'losers.png'
    img = Image.open(in_file)
    width = 650
    height = 1131
    width, height = img.size
                     #left #top  #right   #bottom
    cropped = img.crop((0, 865, width-0, height-0)) 
    cropped.save(out_file)
    alert = discord.Embed(title=f"🌐 SH Image Update:", description=f"Losers.png has been updated.", colour= blue)
    alert.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    alert.set_footer(text=f"{datetime.datetime.now()}")
    await CHH.send(embed=alert)
    print("Losers.png has been updated.")
    # Actives.png
    print("Updating Actives.png")
    s = Service(r"chromedriver")
    s.start() 
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-gpu')
    options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://money.cnn.com/data/hotstocks/')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'cnnBody_Left.wsodContent')
    driver.set_window_size(650, 1131)  
    driver.save_screenshot("actives.png")
    driver.quit()
    in_file = 'actives.png'
    out_file = 'actives.png'
    img = Image.open(in_file)
    width = 650
    height = 1131
    width, height = img.size
                    #left #top  #right   #bottom
    cropped = img.crop((0, 205, width-0, height-650)) 
    cropped.save(out_file)
    alert = discord.Embed(title=f"🌐 SH Image Update:", description=f"Actives.png has been updated.", colour= blue)
    alert.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    alert.set_footer(text=f"{datetime.datetime.now()}")
    await CHH.send(embed=alert)
    print("Actives.png has been updated.")
    print("IMAGE UPDATES COMPLETE.")

# Rotating Status
async def status_task():
    while True:
        s = HTMLSession()
        # Twitter
        top1 = "https://www.marketwatch.com/investing/stock/twtr"
        r = s.get(top1, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname1 = (r.html.find('span.company__ticker', first=True).text) 
        topprice1 = (r.html.find('bg-quote.value', first=True).text)
        topchange1 = (r.html.find('span.change--percent--q', first=True).text)
        # Ford Motor
        top2 = "https://www.marketwatch.com/investing/stock/F"
        r = s.get(top2, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname2 = (r.html.find('span.company__ticker', first=True).text) 
        topprice2 = (r.html.find('bg-quote.value', first=True).text)
        topchange2 = (r.html.find('span.change--percent--q', first=True).text)
        # Bank of America
        top3 = "https://www.marketwatch.com/investing/stock/BAC"
        r = s.get(top3, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname3 = (r.html.find('span.company__ticker', first=True).text) 
        topprice3 = (r.html.find('bg-quote.value', first=True).text)
        topchange3 = (r.html.find('span.change--percent--q', first=True).text)
        # Carnival Corp
        top4 = "https://www.marketwatch.com/investing/stock/CCL"
        r = s.get(top4, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname4 = (r.html.find('span.company__ticker', first=True).text) 
        topprice4 = (r.html.find('bg-quote.value', first=True).text)
        topchange4 = (r.html.find('span.change--percent--q', first=True).text)
        # Occidental Petroleum
        top5 = "https://www.marketwatch.com/investing/stock/OXY"
        r = s.get(top5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname5 = (r.html.find('span.company__ticker', first=True).text) 
        topprice5 = (r.html.find('bg-quote.value', first=True).text)
        topchange5 = (r.html.find('span.change--percent--q', first=True).text)
        # AT&T
        top6 = "https://www.marketwatch.com/investing/stock/T"
        r = s.get(top6, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname6 = (r.html.find('span.company__ticker', first=True).text) 
        topprice6 = (r.html.find('bg-quote.value', first=True).text)
        topchange6 = (r.html.find('span.change--percent--q', first=True).text)
        # General Motors
        top7 = "https://www.marketwatch.com/investing/stock/GM"
        r = s.get(top7, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname7 = (r.html.find('span.company__ticker', first=True).text) 
        topprice7 = (r.html.find('bg-quote.value', first=True).text)
        topchange7 = (r.html.find('span.change--percent--q', first=True).text)
        # Marathon Oil Corp
        top8 = "https://www.marketwatch.com/investing/stock/MRO"
        r = s.get(top8, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname8= (r.html.find('span.company__ticker', first=True).text) 
        topprice8 = (r.html.find('bg-quote.value', first=True).text)
        topchange8 = (r.html.find('span.change--percent--q', first=True).text)
        # Exxon Mobil Corp
        top9 = "https://www.marketwatch.com/investing/stock/XOM"
        r = s.get(top9, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname9= (r.html.find('span.company__ticker', first=True).text) 
        topprice9 = (r.html.find('bg-quote.value', first=True).text)
        topchange9 = (r.html.find('span.change--percent--q', first=True).text)
        # Norwegian Cruise Line
        top10 = "https://www.marketwatch.com/investing/stock/NCLH"
        r = s.get(top10, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
        topname10= (r.html.find('span.company__ticker', first=True).text) 
        topprice10 = (r.html.find('bg-quote.value', first=True).text)
        topchange10 = (r.html.find('span.change--percent--q', first=True).text)  

        await client.change_presence(activity=discord.Game(name="👁️‍🗨️ Scanning NASDAQ!"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname1}: ${topprice1} | {topchange1}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname2}: ${topprice2} | {topchange2}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname3}: ${topprice3} | {topchange3}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname4}: ${topprice4} | {topchange4}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname5}: ${topprice5} | {topchange5}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname6}: ${topprice6} | {topchange6}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname7}: ${topprice7} | {topchange7}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname8}: ${topprice8} | {topchange8}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname9}: ${topprice9} | {topchange9}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"📈{topname10}: ${topprice10} | {topchange10}"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"🌐SH is serving {len(client.guilds)} servers!"), status=discord.Status.online)
        await asyncio.sleep(10)

@client.command()
async def news(ctx, title, body):
    if ctx.author.id != 251241177750306816:
            return
    embed = discord.Embed(title="📢 Business Insider", colour= 0x0022a8)
    embed.add_field(name=f"💬 {title}", value="\u200b", inline=False)
    embed.set_thumbnail(url=f"https://i.imgur.com/ocmsa6m.png")
    for guild in client.guilds:
        for channel in guild.channels:
            if(channel.name == '📢┃stock-news'):
                await channel.send(
                    embed=embed,
                    components = [
                        Button(style=ButtonStyle.URL, label="Open Article", url=f"{body}")
                    ],
                )

@client.command()
@commands.has_permissions(administrator=True)
async def alertsetup(ctx):
    guild = ctx.guild
    await guild.create_text_channel("📢┃stock-news")
    embed = discord.Embed(title="🌟Setup Complete🌟", colour= 0x0022a8)
    embed.add_field(name="Channel created:", value=f"📢┃stock-news", inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    await ctx.send(embed=embed, delete_after=5.0)

@client.command()
async def help(ctx):        
    embed = discord.Embed(title="🗺️ Help Menu", colour= 0x0022a8)
    embed.add_field(name="?alertsetup", value="[Admin]- Creates a channel that Stock Hawk sends articles to.", inline=False)
    embed.add_field(name="?search", value="Provides a quote for a stock. | Usage: ?search TWTR", inline=False)
    embed.add_field(name="?gainers", value=f"Provides a chart of the top gaining stocks.", inline=False)
    embed.add_field(name="?losers", value=f"Provides a chart of the top losing stocks.", inline=False)
    embed.add_field(name="?actives", value=f"Provides a chart of the most active stocks.", inline=False)
    embed.add_field(name="\u200b", value=f"\u200b", inline=False)
    embed.add_field(name="🌟 Premium Commands:", value=f"\u200b", inline=False)
    embed.add_field(name="?insider", value=f"Provides a list of insider activity on a select stock. Shows you what big names are buying or selling the stock. | Usage: ?insider TWTR", inline=False)
    embed.set_thumbnail(url=f"https://i.imgur.com/ocmsa6m.png")
    embed.set_footer(text=f"Support: https://crm-bots.com/")
    await ctx.send(embed=embed)
    CHH = client.get_channel(975639196100329492)
    alert = discord.Embed(title=f"🌐 SH Update:", description=f"{ctx.author.name} used the command help!", colour= blue)
    alert.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    alert.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    alert.set_footer(text=f"🔎 Server Name: {ctx.message.guild.name} | Server ID: {ctx.message.guild.id}")
    await CHH.send(embed=alert)

@client.command()
async def search(ctx, query):
    s = HTMLSession()
    url = f"https://www.marketwatch.com/investing/stock/{query}"
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
    price = (r.html.find('bg-quote.value', first=True).text)
    change = (r.html.find('span.change--percent--q', first=True).text)
    open = (r.html.find('li.kv__item span.primary', first=True).text)
    update = (r.html.find('span.timestamp__time bg-quote', first=True).text)
    header = (r.html.find('h1.company__name', first=True).text)
    abbrv = (r.html.find('span.company__ticker', first=True).text)
    embed = discord.Embed(title=f"📈 {abbrv} Quote", colour= 0x0022a8)
    embed.add_field(name="Company:", value=f"{header}", inline=False)
    embed.add_field(name="Current Price:", value=f"${price}", inline=False)
    embed.add_field(name="Change:", value=f"{change}", inline=False)
    embed.add_field(name="Opening Price:", value=f"{open}", inline=False)
    embed.set_thumbnail(url=f"https://i.imgur.com/ocmsa6m.png")
    embed.set_footer(text=f"Last Updated: {update}")
    await ctx.send(embed=embed)
    CHH = client.get_channel(975639196100329492)
    alert = discord.Embed(title=f"🌐 SH Update:", description=f"{ctx.author.name} used the command search!", colour= blue)
    alert.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    alert.add_field(name="Searched for:", value=f"{query}", inline=False)
    alert.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    alert.set_footer(text=f"🔎 Server Name: {ctx.message.guild.name} | Server ID: {ctx.message.guild.id}")
    await CHH.send(embed=alert)

@search.error
async def some_command_name_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(title=f"📡 Error:", colour= blue)
        embed.add_field(name="Ticker Invalid:", value=f"Please enter a valid ticker and try again.", inline=False)
        await ctx.send(embed=embed, delete_after=10.0)

@client.command()
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit, check=lambda msg: not msg.pinned)



@client.command()
async def gainers(ctx):
    file2 = discord.File('loading.gif')
    embed2 = discord.Embed(title=f"⚙️ Scraping Top Gainers Chart...", colour= 0x0022a8)
    embed2.set_image(url='attachment://loading.gif')
    await ctx.send(embed=embed2, file=file2, delete_after=2.0)
    await asyncio.sleep(2)
    s = HTMLSession()
    url = f"https://www.marketwatch.com/investing/stock/XOM"
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
    update = (r.html.find('span.timestamp__time bg-quote', first=True).text)
    file = discord.File('gains.png')
    embed = discord.Embed(title=f"📈 Top Gainers", colour= 0x0022a8)
    embed.set_image(url='attachment://gains.png')
    embed.set_footer(text=f"Last Updated: {update}")
    await ctx.send(embed=embed, file=file)
    CHH = client.get_channel(975639196100329492)
    alert = discord.Embed(title=f"🌐 SH Update:", description=f"{ctx.author.name} used the command gains!", colour= blue)
    alert.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    alert.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    alert.set_footer(text=f"🔎 Server Name: {ctx.message.guild.name} | Server ID: {ctx.message.guild.id}")
    await CHH.send(embed=alert)

@client.command()
async def losers(ctx):
    file2 = discord.File('loading.gif')
    embed2 = discord.Embed(title=f"⚙️ Scraping Top Losers Chart...", colour= 0x0022a8)
    embed2.set_image(url='attachment://loading.gif')
    await ctx.send(embed=embed2, file=file2, delete_after=2.0)
    await asyncio.sleep(2)
    s = HTMLSession()
    url = f"https://www.marketwatch.com/investing/stock/XOM"
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
    update = (r.html.find('span.timestamp__time bg-quote', first=True).text)
    file = discord.File('losers.png')
    embed = discord.Embed(title=f"📉 Top Losers", colour= 0x0022a8)
    embed.set_image(url='attachment://losers.png')
    embed.set_footer(text=f"Last Updated: {update}")
    await ctx.send(embed=embed, file=file)
    CHH = client.get_channel(975639196100329492)
    alert = discord.Embed(title=f"🌐 SH Update:", description=f"{ctx.author.name} used the command losers!", colour= blue)
    alert.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    alert.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    alert.set_footer(text=f"🔎 Server Name: {ctx.message.guild.name} | Server ID: {ctx.message.guild.id}")
    await CHH.send(embed=alert)

@client.command()
async def actives(ctx):
    file2 = discord.File('loading.gif')
    embed2 = discord.Embed(title=f"⚙️ Scraping Top Actives Chart...", colour= 0x0022a8)
    embed2.set_image(url='attachment://loading.gif')
    await ctx.send(embed=embed2, file=file2, delete_after=2.0)
    await asyncio.sleep(2)
    s = HTMLSession()
    url = f"https://www.marketwatch.com/investing/stock/XOM"
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'})
    update = (r.html.find('span.timestamp__time bg-quote', first=True).text)
    file = discord.File('actives.png')
    embed = discord.Embed(title=f"💎 Most Actives", colour= 0x0022a8)
    embed.set_image(url='attachment://actives.png')
    embed.set_footer(text=f"Last Updated: {update}")
    await ctx.send(embed=embed, file=file)
    CHH = client.get_channel(975639196100329492)
    alert = discord.Embed(title=f"🌐 SH Update:", description=f"{ctx.author.name} used the command actives!", colour= blue)
    alert.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    alert.set_thumbnail(url="https://i.imgur.com/ocmsa6m.png")
    alert.set_footer(text=f"🔎 Server Name: {ctx.message.guild.name} | Server ID: {ctx.message.guild.id}")
    await CHH.send(embed=alert)                                                                               
 
 
client.run(config['bot']['token'])
