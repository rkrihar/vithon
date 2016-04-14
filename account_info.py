import mechanize
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import cookielib
from datetime import date
import time
cj = cookielib.LWPCookieJar()
cookies = mechanize.CookieJar()
br = Browser()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_robots(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)

d1 = date(2016,3,6)
#d2 = 

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
r = br.open('http://115.248.50.60/registration/Main.jsp?wispId=1&nasId=00:15:17:b4:b1:dc')
br.select_form('chooseAuthForm')
br.form['loginUserId'] = raw_input("username: ")
br.form['loginPassword'] = raw_input("password: ")
br.submit()
page = br.open(br.geturl())
#html = page.read()
home = br.open('http://115.248.50.60/registration/main.do?content_key=%2FCustomerSessionHistory.jsp')

cooky =  home.info().headers[3][12:114]

header = [
('Host', 'http://115.248.50.60/registration/customerSessionHistory.do'),
('Content-Length', '162'),
('Cache-Control', 'max-age=0'),
('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
('Origin', 'http://115.248.50.60'),
('Upgrade-Insecure-Requests', '1'),
('Connection', 'keep-alive'),
('User-Agent', 'User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'),
('Content-Type', 'application/x-www-form-urlencoded'),
('Referer', 'http://115.248.50.60/registration/main.do?content_key=%2FCustomerSessionHistory.jsp'),
('Accept-Encoding', 'gzip, deflate'),
('Accept-Language', 'en-US,en;q=0.8'),
('Cookie', cooky)
]


url = 'http://115.248.50.60/registration/customerSessionHistory.do'
shead = 'location=allLocations&parameter=custom&customStartMonth=03&customStartDay=05&customStartYear=2016&customEndMonth=00&customEndDay=01&customEndYear=2017&button=View'
opener = mechanize.build_opener(mechanize.HTTPCookieProcessor(cookies))
opener.addheaders = header
sent_page = opener.open(url,shead)
#print sent_page.read()
soup = BeautifulSoup(sent_page.read())
td = soup.findAll('td',{'class': 'subTextRight'})
print td[len(td)-1].b.string


time.sleep(3)
