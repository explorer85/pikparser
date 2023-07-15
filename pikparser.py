from bs4 import BeautifulSoup
import requests

adress = 'https://cdn.pik.ru/sitemap/pik/flats.xml'

xmlDict = {}

r = requests.get(adress)
print("parse response")

xml = r.text

#вывод в файл
with open('outSiteMap.txt', 'w') as f:
    print(xml, file=f)  # Python 3.x


soup = BeautifulSoup(xml, "xml")
sitemapLocs = soup.find_all("loc")

print("The number of sitemaps are {0}".format(len(sitemapLocs)))

flatsArray = []
for loc in sitemapLocs:
     flatId = loc.text.split("/")[-1]
     flatsArray.append(flatId)
     #print(flatId)


fFlats = open("outFlats.txt", "a")  # append mode

for flatId in flatsArray:
    print(flatId)
    requestString = "https://api-selectel.pik-service.ru/v2/flat/mortgage?flatId=" + flatId + "&loanTerm=30&benefitId=114418"
    print(requestString)
    r = requests.get(requestString)
    print("parse response")
    fFlats.write(r.text + "\n")

fFlats.close()

