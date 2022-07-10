import discord
from discord.ext import commands,tasks
from arxivlib import Arxiv
from datetime import datetime, time, timedelta
from keep_alive import keep_alive



TOKEN = %DISCORD BOT TOKEN% 

sortings = ['random','date','relevance']

bot = commands.Bot(command_prefix="$", activity=discord.Game(name="$Arxiv Hunting"))

@bot.event
async def on_ready():
    print('Ready to find article!')
    arxiv_time.start()

@bot.command()
async def complete_search(ctx,sorting,number,author,title,abstract,start=0):
  arx = Arxiv(number,start)
  if not any(sorting==x for x in sortings):
    await ctx.channel.send('Wrong sorting. The options are: random, date, relevance')
  else:
    
    if sorting == sortings[0]:
      results = arx.complete_random_search(author,title,abstract)
    elif sorting == sortings[1]:
      results = arx.complete_date_search(author,title,abstract)
    elif sorting == sortings[2]:
      results = arx.complete_relevance_search(author,title,abstract)

    await ctx.channel.send(('\n'.join(map(str, results))))

@bot.command()
async def author_title_search(ctx,sorting,number,author,title,start=0):
  arx = Arxiv(number,start)
  if not any(sorting==x for x in sortings):
    await ctx.channel.send('Wrong sorting. The options are: random, date, relevance')
  else:
    
    if sorting == sortings[0]:
      results = arx.author_title_random_search(author,title)
    elif sorting == sortings[1]:
      results = arx.author_title_date_search(author,title)
    elif sorting == sortings[2]:
      results = arx.author_title_relevance_search(author,title)
      
    await ctx.channel.send(('\n'.join(map(str, results))))
  
@bot.command()
async def author_abstract_search(ctx,sorting,number,author,abstract,start=0):
  arx = Arxiv(number,start)
  if not any(sorting==x for x in sortings):
    await ctx.channel.send('Wrong sorting. The options are: random, date, relevance')
  else:
    
    if sorting == sortings[0]:
      results = arx.author_abstract_random_search(author,abstract)
    elif sorting == sortings[1]:
      results = arx.author_abstract_date_search(author,abstract)
    elif sorting == sortings[2]:
      results = arx.author_abstract_relevance_search(author,abstract) 

    await ctx.channel.send(('\n'.join(map(str, results))))

@bot.command()
async def title_abstract_search(ctx,sorting,number,title,abstract,start=0):
  arx = Arxiv(number,start)
  if not any(sorting==x for x in sortings):
    await ctx.channel.send('Wrong sorting. The options are: random, date, relevance')
  else:
    
    if sorting == sortings[0]:
      results = arx.title_abstract_random_search(title,abstract)
    elif sorting == sortings[1]:
      results = arx.title_abstract_date_search(title,abstract)
    elif sorting == sortings[2]:
      results = arx.title_abstract_relevance_search(title,abstract) 

    await ctx.channel.send(('\n'.join(map(str, results))))

@bot.command()
async def author_search(ctx,sorting,number,author,start=0):
  arx = Arxiv(number,start)
  if not any(sorting==x for x in sortings):
    await ctx.channel.send('Wrong sorting. The options are: random, date, relevance')
  else:
    
    if sorting == sortings[0]:
      results = arx.author_random_search(author)
    elif sorting == sortings[1]:
      results = arx.author_date_search(author)
    elif sorting == sortings[2]:
      results = arx.author_relevance_search(author) 

    await ctx.channel.send(('\n'.join(map(str, results))))

@bot.command()
async def title_search(ctx,sorting,number,title,start=0):
  arx = Arxiv(number,start)
  if not any(sorting==x for x in sortings):
    await ctx.channel.send('Wrong sorting. The options are: random, date, relevance')
  else:
    
    if sorting == sortings[0]:
      results = arx.title_random_search(title)
    elif sorting == sortings[1]:
      results = arx.title_date_search(title)
    elif sorting == sortings[2]:
      results = arx.title_relevance_search(title) 

    await ctx.channel.send(('\n'.join(map(str, results))))

@bot.command()
async def abstract_search(ctx,sorting,number,abstract,start=0):
  arx = Arxiv(number,start)
  if not any(sorting==x for x in sortings):
    await ctx.channel.send('Wrong sorting. The options are: random, date, relevance')
  else:
    
    if sorting == sortings[0]:
      results = arx.abstract_random_search(abstract)
    elif sorting == sortings[1]:
      results = arx.abstract_date_search(abstract)
    elif sorting == sortings[2]:
      results = arx.abstract_relevance_search(abstract) 

    await ctx.channel.send(('\n'.join(map(str, results))))

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     if message.content.startswith('$hello'):
#         channel = bot.get_channel(953693155889385537)
#         await channel.send('hello')

@tasks.loop(hours=24)
async def arxiv_time():
  channel = bot.get_channel(953693155889385537)
  arx = Arxiv(3,0)
  results = arx.abstract_date_search('qubits')
  await channel.send(('\n'.join(map(str, results))))


keep_alive()


bot.run(TOKEN)






          
