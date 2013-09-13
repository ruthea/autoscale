import os
import urllib


url = 'http://helloflask25.cfapps.io'
nf = urllib.urlopen(url)
start = time.time()
page = nf.read()
end = time.time()
nf.close()

