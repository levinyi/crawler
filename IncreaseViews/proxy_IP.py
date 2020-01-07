import urllib
from bs4 import BeautifulSoup
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'

header = {}
header['User-Agent'] = User_Agent
url = 'https://www.xicidaili.com/wt/1'
req = urllib.request.Request(url, headers=header)
res = urllib.request.urlopen(req).read()
soup = BeautifulSoup(res)
ips = soup.findAll('tr')
f = open("proxy", "w")

for x in range(1, len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    ip_temp = tds[1].contents[0]+","+tds[2].contents[0]+"\n"
    print(tds[1].contents[0]+"\t"+tds[2].contents[0])
    f.write(ip_temp)
f.close()
