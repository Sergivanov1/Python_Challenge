import urllib.request
import re
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

text = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]

result = ("".join(re.findall('[A-Za-z]', text)))

print(result) # equality is result