import json
import pprint

with open('results.json' , 'r') as file:
    data = json.load(file)
    # data = json.loads("afsd")  #Differece b/w loads and load is load takes input as file and loads as string

printer = pprint.PrettyPrinter()
# printer.pprint(data)

language = data.get('2015ugcs089')
# printer.pprint(language)
printer.pprint(language.get("name"))

# ⚡CP:(C⭐C++⭐Algo⭐DS)⚡WebDev:(HTML⭐CSS⭐JS⭐Bootstrap⭐ReactJs⭐Redux⭐GraphQL)
# ⚡AppDev⚡Databases:(Firebase All Sections⭐ SQL⭐MongoDB)⚡Web Scraping(Scrapy&Selenium)

# 💡📍

# ⚡CP:(C⭐C++⭐Algo⭐DS)⚡WebDev:(HTML⭐CSS⭐JS⭐Bootstrap⭐ReactJs⭐Redux⭐GraphQL)
# ⚡AppDev⚡Databases:(Firebase All Sections⭐SQL⭐MongoDB)⚡Web Scraping(Scrapy&Selenium)

# ⚡CP:(C⭐C++⭐Algo⭐DS)⚡WebDev:(HTML⭐CSS⭐JS⭐Bootstrap⭐ReactJs⭐Redux⭐GraphQL)
# ⚡AppDev⚡Databases: (Firebase All Sections⭐SQL ⭐MongoDB)⚡Web Scraping (Scrapy&Selenium)

⚡CP:(C|C++|Algo|DS)⚡WebDev:(HTML|CSS|JS|Bootstrap|ReactJs|Redux|GraphQL)
⚡AppDev⚡Databases: (Firebase All Sections|SQL |MongoDB)⚡Web Scraping (Scrapy&Selenium)