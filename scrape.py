import requests 
from bs4 import BeautifulSoup 
import pprint
# REQUESTING DATA

res = requests.get('https://news.ycombinator.com/news')
res2 =  requests.get('https://news.ycombinator.com/news?p=2') # adding another page

# BEAUTIFULSOUP BASICS
soup = BeautifulSoup(res.text, 'html.parser') # this is a soup object
soup2 = BeautifulSoup(res2.text, 'html.parser') # adding another page

# BEAUTIFULSOUP SELECTORS
links = soup.select('.titleline')
votes = soup.select('.score')
subtext = soup.select('.subtext')

links2 = soup2.select('.titleline')
votes2 = soup2.select('.score')
subtext2 = soup2.select('.subtext')
# combining
mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse = True)

# HACKER NEWS PROJECT
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        a_tag = item.find('a') 
        title = a_tag.getText()
        href = a_tag.get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            #print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
