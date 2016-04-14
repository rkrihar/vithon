from mechanize import Browser, build_opener
import BeautifulSoup,mechanize
import cookielib
cookies = mechanize.CookieJar()
br = Browser()
br.set_handle_robots('False')
#opener = mechanize.build_opener(mechanize.HTTPCookieProcessor(cookies))
#opener.addheaders=header
n=151
while n<152:
    m = str(n).zfill(4)
    regno = '13BIT'+m
    br.retrieve('https://academics.vit.ac.in/student/view_photo_2.asp?rgno='+regno,'G:/python/'+regno+'.jpeg')
    print 'done'+str(n)
    n+=1
