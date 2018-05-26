import requests
from bs4 import BeautifulSoup
import time

#get the website page of live score you want
res=requests.get('https://www.cricbuzz.com/cricket-match/live-scores')

#apply beautifulsoup to that page
soup=BeautifulSoup(res.text,'html.parser')

#get the class of all the matches happening
matches=soup.find_all('a',{'class':'text-hvr-underline'})

#matches list
for i in matches[:10]:
    print(str(matches.index(i)+1)+" " +i['title'])

#take input to get which match to show
k=int(input('enter the match number to be shown '))


#get the scores value
scores=soup.find_all('div',{'class':'cb-lv-scrs-col text-black'})
a=scores[k-1].text

print(matches[k-1].text)
print(scores[k-1].text)
        
while True:
    scores=soup.find_all('div',{'class':'cb-lv-scrs-col text-black'})
#get requested match score
    if a!=scores[k-1].text:
        print(matches[k-1].text)
        print(scores[k-1].text)
        a=scores[k-1].text
        print()
    time.sleep(20)
    res=requests.get('https://www.cricbuzz.com/cricket-match/live-scores')

#apply beautifulsoup to that page
    soup=BeautifulSoup(res.text,'html.parser')


