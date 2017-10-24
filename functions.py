from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request
import random

def random_quote():
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
    conn=urlopen(Request('https://www.inc.com/dave-kerpen/365-quotes-to-inspire-you-in-2014.html',data=None, headers={'User-Agent': user_agent}))
    html_content = conn.read()
    soup=BeautifulSoup(html_content,'html.parser')
    quotes=soup.find_all('li')[114:]
    number=random.randint(0,len(quotes))
    return(str(quotes[number])[4:-5])


