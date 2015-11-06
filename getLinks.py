import urllib.request
import csv
import re

test1 = urllib.request.urlopen("http://www.google.com")
test = test1.read().decode('utf-8')
test1.close()
sane = 0
needlestack = []
value = []
import re
urls = re.findall(r'href=[\'"]?([^\'" >]+)', test)
name = re.findall(r'href=[\'<]?([^\'> >]+)', test)
print (', '.join(urls))

while sane == 0:
  curpos = test.find("href")
  if curpos >= 0:
    testlen = len(test)
    test = test[curpos:testlen]
    curpos = test.find('"')
    testlen = len(test)
    test = test[curpos+1:testlen]
    curpos = test.find('"')
    needle = test[0:curpos]
    
    if needle.startswith("http" or "www"):
        needlestack.append(needle)
  else:
    sane = 1
with open('test.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=' ',
        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for item in needlestack:
        a.writerow(item)
        print (item)

