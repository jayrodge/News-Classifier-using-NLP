from lxml import html
import requests

buisness_news=[]
BASE_URL='https://www.moneycontrol.com/news/business-3.html/page-'#Link of the news website
for i in range(1,61): #Number of Pages to Crawl
    url=BASE_URL+str(i)+'/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    for j in range(1,25):
        k=[21,24]
        if(j in k):
            continue
        path=str('//*[@id="newslist-'+str(j)+'"]/p/text()') #Include XPath
        buisness_news.append(tree.xpath(path)[0])

print(len(buisness_news))

with open('data/csv/money_control_l.csv', 'w') as wf:
		for l in buisness_news:
			wf.write(l+'\n')