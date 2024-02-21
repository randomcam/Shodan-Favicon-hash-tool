from shodan import Shodan
from faviconhashmaker import faviconhash
from api import key
api=Shodan(key)
#favicon='-1256722636' #Tesco
#favicon= faviconhash('https://cwa.roocdn.com/_next/static/favicon-32x32.9ac59871.png')
#favicon=faviconhash('https://www.dpd.co.uk/asset_files/icon/favicon.ico')
#favicon= faviconhash('https://www.parcelforce.com/profiles/pfwprofile/themes/parcelforce2/favicon.ico')

favicon= faviconhash("https://www.gov.uk/assets/static/favicon-9ed7849c462c53aa2cdf1690eb257e801ecbf5696d1d0928868c5b032b4adb36.ico")


print(favicon)
# Search
for banner in api.search_cursor('http.favicon.hash:'+str(favicon)):
    #print(banner.keys())
    
    print(str(banner['ip_str'])+':'+str(banner['port']))
    
#results=api.search('http.favicon.hash:-1256722636', limit=1)
#print(results)

