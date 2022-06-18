import mechanize

vbrowser = mechanize.Browser()
vbrowser.open("https://www.geeksforgeeks.org/")
url = mechanize.urlopen("https://www.geeksforgeeks.org/")
print(url.code)
print(url.read())
