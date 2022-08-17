import tempfile
import os

os.rmdir(test := tempfile.mkdtemp())
print(test)


