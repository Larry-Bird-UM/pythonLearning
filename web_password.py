import urllib,urllib2,httplib,cookielib
url ='http://mail.163.com/'
values={'username':'chinacncom',
        'password':'Gospurs2016'}
data=urllib.urlencode(values)
req = urllib2.Request(url,data)
response=urllib2.urlopen(req)
the_page = response.read()
print the_page

