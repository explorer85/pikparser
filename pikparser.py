from bs4 import BeautifulSoup
import requests
import json

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



#uni = "\u041f\u043e\u043b\u043d\u0430\u044f \u043e\u043f\u043b\u0430\u0442\u0430"
#print(uni)
#uttf8text = uni.encode('utf-8')
#uttf8text = uttf8text.decode('utf-8')
#print(uttf8text)


fFlats = open("outFlats.txt", "a")  # append mode

for flatId in flatsArray:
    print(flatId)
    requestString = "https://api-selectel.pik-service.ru/v2/flat/mortgage?flatId=" + flatId + "&loanTerm=30&benefitId=114418"
    #print(requestString)
    r = requests.get(requestString)
    unicode = r.text

    unicodeDict = json.loads(unicode)


    if unicodeDict.get('benefits'):
             benifitsObj = unicodeDict['benefits']
             #print(benifitsObj)
             if benifitsObj.get('cash'):                 
                      print(benifitsObj['cash'])
    fFlats.write(unicode + "\n")

    

    
    

fFlats.close()



