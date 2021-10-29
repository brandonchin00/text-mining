import bs4
import sys
import requests
#import the necessary modules

'''this will search for the appropriate wikipedia article and request to download the file'''
wiki_page = 'Democratic_Party_(United_States)' 
response = requests.get(f'https://en.wikipedia.org/wiki/{wiki_page}')

response.raise_for_status() #this will return error if the article is not found

wiki = bs4.BeautifulSoup(response.text,"html.parser") #Beautiful Soup is a module from Python's library where you can easily pull HTML files
#the parser module allows python code

'''converts it to txt.file'''
with open(wiki_page+".txt", "w", encoding="utf-8") as f: 
    for i in wiki.select('p'):
        # write each paragraph to the file
        f.write(i.getText())




