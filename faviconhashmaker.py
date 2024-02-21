import mmh3
import requests
import codecs
def faviconhash(link):
    
    
    response = requests.get(link)
    
    favicon = codecs.encode(response.content,"base64")
    
    hash = mmh3.hash(favicon)
    #print(hash)
    return hash
#faviconhash("https://www.gov.uk/assets/static/favicon-9ed7849c462c53aa2cdf1690eb257e801ecbf5696d1d0928868c5b032b4adb36.ico")
#https://cwa.roocdn.com/_next/static/favicon-32x32.9ac59871.png
#faviconhash("https://assets.aldi-digital.co.uk/assets/33cf39ae13c36cffad797011246c2b34/dist/images/LOGO.png")
#faviconhash("https://www.tesco.com/favicon.ico")
