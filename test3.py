import tempfile
import os
import urllib.request

test = tempfile.mkdtemp()
urllib.request.urlretrieve('https://www.debian.org/releases/bullseye/example-preseed.txt', test+'/preseed.cfg')
print(test)
