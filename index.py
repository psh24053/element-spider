import json
from getData  import GetData
from writeData import WriteData




latitudeAndlongitudeArr=[]
def init():
    global latitudeAndlongitudeArr

    with open("config.json", 'r', encoding='UTF-8') as f:
        config = json.load(f)
        latitudeAndlongitudeArr = config.get('latitudeAndlongitudeArr')
        return config.get('Cookie')

rowIndex = 0
def startWriteData(Cookie):
    global rowIndex

    WriteData().writeFirst()

    for latitudeAndlongitude  in latitudeAndlongitudeArr:
        print(latitudeAndlongitude)
        pageIndex = 0
        shopList = GetData(Cookie).getShopList(pageIndex,latitudeAndlongitude)
        while shopList is not None and len(shopList)>0:
            WriteData().write_excel(shopList,rowIndex,latitudeAndlongitude)
            pageIndex+=1
            rowIndex+=1
            shopList = GetData(Cookie).getShopList(pageIndex,latitudeAndlongitude)



if __name__ =='__main__':

    startWriteData(init())
