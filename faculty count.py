from BeautifulSoup import BeautifulSoup
import mechanize
import time
from datetime import datetime
from mechanize import Browser
br=Browser()
br.set_handle_robots(False)
ad ='https://academics.vit.ac.in/student/'
header = [

('Host',' academics.vit.ac.in'),
('Connection',' keep-alive'),
('Accept','*/*'),
('User-Agent',' Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'),
('Referer',' https://academics.vit.ac.in/student/fac_profile.asp'),
('Accept-Encoding',' gzip, deflate, sdch'),
('Accept-Language',' en-US,en;q=0.8'),
('Cookie',' logstudregno=13BIT0151; _ga=GA1.3.995155495.1433518551; ASPSESSIONIDSUTQADSB=GDHIPDIDPNEJGDKAPMIHEDEK')
]
br.addheaders = header
i = 1
max = 999
while i <= max:
    localtime = time.asctime( time.localtime(time.time()) )
    t = localtime.split(' ')
    utc = datetime.utcnow();
    s = str(utc);
    url='https://academics.vit.ac.in/student/getfacdet.asp?fac=Z&x='+t[0]+',%20'+s[8:10]+'%20'+t[1]+'%20'+t[4]+'%20'+s[11:19]+'%20GMT'
    r = br.open(url)
    html = r.read()
    soup = BeautifulSoup(html)
    if i==1 :
        max = len(soup('tr'))-1
        print max
    '''link = soup('tr')[i].a
    r = br.open(ad+link['href'])
    html = r.read()
    soup = BeautifulSoup(html)
    img = soup('img')[0]['src']
    name = soup('td',{'width':'660'})[0].string
    br.retrieve(ad+img,'G:/python/faculty/'+name+'.jpg')'''
    i = i+1
    break
f = open('count.txt','a')
f.write('Z: '+str(max)+'\n')
f.close()
