import urllib2

url="http://hangzhou.anjuke.com/"#安居客首页,爬虫的入口页面
try:
    request =  urllib2.Request(url)
    response = urllib2.urlopen(request)
    print  response.read()
except urllib2.URLError,e:
    print e.reason