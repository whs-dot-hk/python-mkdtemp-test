import urllib.request
import os

local_filename, headers = urllib.request.urlretrieve('http://python.org/')
print(local_filename)
html = open(local_filename)
print(html)
html.close()
os.unlink(local_filename)
