import time
import requests
import random
from IPS import get_proxy
import json
from parse import parseCookie




UserAgent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
headers = {
    'referer': 'https://h5.ele.me/msite/food/',
    'cookie':'',
    'user-agent':UserAgent,
    'accept': 'application/json, text/plain, */*'
}
commentHeaders = {
    'referer': 'https://h5.ele.me/msite/food/',
    'cookie': '',
    'user-agent': UserAgent,
    'accept': 'application/json, text/plain, */*',
    'referer':'https://h5.ele.me/shop/',
    'x-shard':'https://h5.ele.me/shop/',
    'x-uab':'123#aV0Dbd7Qw3tumHbxlDl48ldEzQXHO1io8aHFS7NtNz/HzaHKDdQPLzeaLkadHza6hjjk8GDdOnmLuPaFo+eA2U1QL84UsQ+MIvzuFzR+KdbZIUXMNYIifOAoT46XPJv7WOwLT5To7wHcangIjNlhCWeg3xcpLaOagoBUdUZPZRK0j5y+ui0BoNkzjgiJiRatCwoNNrzkLO+Xfb8lrRSr+Bv+mHdDCw9kX1Yk84+4pscAJ6yrlivUqMhpzsbAR8rv6QhDLGrCif8dhbPGPHydZpmva1b/BuIT0f60K4Et1xVKVX7d/nBQLYfQH2WqfSCyHHsmGfGJmQvJaJQDpwo5uyRroRthcLcwc1VGFdaTMdmUPsaoFVEfP58MdOYPD2gDrhQiEEpi9gbN/dpBzQth4hZry25srFUDKv1paOCqZzK9f353GamvdHiUWtugindOWB5mRc1w+2F7Bt5Cge2hc+4enzXcold6OyqMSOYr5GMojm3OlYCKJwCnTh9DWcg48OMejoWLioR14svfhHh1amly+qIog/FFGPnBb09l1+uXYtQOr49uRpza9euUBmOc/a2NyiYWrlR/YGsDnCYO4H+QRKEKZN5cNKQy3yIFQ69qbolMkstuXCeRJ5gieXDF2CIU8jC3gitoWsOziIXVZl5IVgz0GrR0bUUej3xX2XgKh8MtYmtGQGlP4y72do0y1/cpWRH/5uv+hpJhq2upRFm50OBVKMa4Azg05JlUpzvrdkN00yq8QaA0Cuwi1Z1dCdYoNF7KKEdBPMCyMkv7tYc+YuMNowfLPHT+8v2N2qUELMf8TDeLWZR4yfga5hnudC6WJ5len48/npcMbdyI5bdM6kx9/t3uURVXgBHr6oVJg3JQ9jPsD0Cyi41nQ+nWBBPBuEYN',
    'referer':'https://h5.ele.me/shop/',
        'x-font-version': '949d1b141c5746fea6d983574da7188f',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode' :'cors',
    'sec-fetch-site' : 'same-origin',
    'x - ua': 'RenderWay / H5AppName / wap'
}
# 商家信息URL
shopURL = 'https://h5.ele.me/restapi/shopping/v3/restaurants?latitude={1}&longitude={2}&keyword=&offset={0}&limit=8&extras[]=activities&extras[]=tags&terminal=h5&rank_id=undefined&brand_ids[]=&restaurant_category_ids[]=770&restaurant_category_ids[]=514&restaurant_category_ids[]=1026&restaurant_category_ids[]=1282&restaurant_category_ids[]=263&restaurant_category_ids[]=266&restaurant_category_ids[]=778&restaurant_category_ids[]=522&restaurant_category_ids[]=1034&restaurant_category_ids[]=1290&restaurant_category_ids[]=267&restaurant_category_ids[]=268&restaurant_category_ids[]=269&restaurant_category_ids[]=786&restaurant_category_ids[]=530&restaurant_category_ids[]=1042&restaurant_category_ids[]=1298&restaurant_category_ids[]=794&restaurant_category_ids[]=538&restaurant_category_ids[]=1050&restaurant_category_ids[]=1306&restaurant_category_ids[]=802&restaurant_category_ids[]=546&restaurant_category_ids[]=1058&restaurant_category_ids[]=1314&restaurant_category_ids[]=810&restaurant_category_ids[]=554&restaurant_category_ids[]=1066&restaurant_category_ids[]=1322&restaurant_category_ids[]=818&restaurant_category_ids[]=562&restaurant_category_ids[]=1074&restaurant_category_ids[]=1330&restaurant_category_ids[]=826&restaurant_category_ids[]=570&restaurant_category_ids[]=1082&restaurant_category_ids[]=1338&restaurant_category_ids[]=834&restaurant_category_ids[]=578&restaurant_category_ids[]=1090&restaurant_category_ids[]=1346&restaurant_category_ids[]=842&restaurant_category_ids[]=586&restaurant_category_ids[]=1098&restaurant_category_ids[]=1354&restaurant_category_ids[]=850&restaurant_category_ids[]=594&restaurant_category_ids[]=1106&restaurant_category_ids[]=1362&restaurant_category_ids[]=858&restaurant_category_ids[]=602&restaurant_category_ids[]=346&restaurant_category_ids[]=1114&restaurant_category_ids[]=354&restaurant_category_ids[]=866&restaurant_category_ids[]=610&restaurant_category_ids[]=1122&restaurant_category_ids[]=362&restaurant_category_ids[]=874&restaurant_category_ids[]=618&restaurant_category_ids[]=1130&restaurant_category_ids[]=370&restaurant_category_ids[]=882&restaurant_category_ids[]=626&restaurant_category_ids[]=1138&restaurant_category_ids[]=378&restaurant_category_ids[]=890&restaurant_category_ids[]=634&restaurant_category_ids[]=1146&restaurant_category_ids[]=386&restaurant_category_ids[]=898&restaurant_category_ids[]=642&restaurant_category_ids[]=1154&restaurant_category_ids[]=394&restaurant_category_ids[]=906&restaurant_category_ids[]=650&restaurant_category_ids[]=1162&restaurant_category_ids[]=402&restaurant_category_ids[]=914&restaurant_category_ids[]=658&restaurant_category_ids[]=1170&restaurant_category_ids[]=410&restaurant_category_ids[]=922&restaurant_category_ids[]=666&restaurant_category_ids[]=1178&restaurant_category_ids[]=418&restaurant_category_ids[]=930&restaurant_category_ids[]=674&restaurant_category_ids[]=1186&restaurant_category_ids[]=426&restaurant_category_ids[]=938&restaurant_category_ids[]=682&restaurant_category_ids[]=1194&restaurant_category_ids[]=434&restaurant_category_ids[]=946&restaurant_category_ids[]=690&restaurant_category_ids[]=1202&restaurant_category_ids[]=442&restaurant_category_ids[]=954&restaurant_category_ids[]=698&restaurant_category_ids[]=1210&restaurant_category_ids[]=450&restaurant_category_ids[]=706&restaurant_category_ids[]=962&restaurant_category_ids[]=1218&restaurant_category_ids[]=458&restaurant_category_ids[]=970&restaurant_category_ids[]=714&restaurant_category_ids[]=1226&restaurant_category_ids[]=209&restaurant_category_ids[]=466&restaurant_category_ids[]=978&restaurant_category_ids[]=722&restaurant_category_ids[]=1234&restaurant_category_ids[]=212&restaurant_category_ids[]=214&restaurant_category_ids[]=474&restaurant_category_ids[]=218&restaurant_category_ids[]=986&restaurant_category_ids[]=730&restaurant_category_ids[]=221&restaurant_category_ids[]=222&restaurant_category_ids[]=223&restaurant_category_ids[]=224&restaurant_category_ids[]=225&restaurant_category_ids[]=482&restaurant_category_ids[]=226&restaurant_category_ids[]=994&restaurant_category_ids[]=738&restaurant_category_ids[]=1250&restaurant_category_ids[]=227&restaurant_category_ids[]=228&restaurant_category_ids[]=232&restaurant_category_ids[]=490&restaurant_category_ids[]=746&restaurant_category_ids[]=234&restaurant_category_ids[]=1002&restaurant_category_ids[]=1258&restaurant_category_ids[]=236&restaurant_category_ids[]=240&restaurant_category_ids[]=241&restaurant_category_ids[]=498&restaurant_category_ids[]=754&restaurant_category_ids[]=1010&restaurant_category_ids[]=242&restaurant_category_ids[]=1266&restaurant_category_ids[]=249&restaurant_category_ids[]=762&restaurant_category_ids[]=506&restaurant_category_ids[]=1018&restaurant_category_ids[]=250&restaurant_category_ids[]=1274'
# 评论信息URL
commentURL = 'https://h5.ele.me/pizza/ugc/restaurants/{0}/batch_comments?has_content=true&offset=0&limit=20'
# 商家详细信息（地址在里边）
infoURL = 'https://h5.ele.me/restapi/booking/v1/cart_client'
infoPayload = {"sub_channel":"","business_type":0,"geohash":"yb4h12gwsz88","user_id":0,"add_on_type":0,"restaurant_id":"E5261343707481227761","come_from":"mobile","additional_actions":[71],"entities":[[]],"entities_with_ingredient":[[]],"operating_sku_ids":[],"tying_sku_entities":[[]],"packages":[[]],"from":None}




class GetData:

    def __init__(self,Cookie):
        self.Cookie = Cookie

    def getShopList(self,pageIndex,latitudeAndlongitude):
        headers['cookie'] = self.Cookie

        time.sleep(2+random.random())
        res = requests.get(shopURL.format(pageIndex*8,latitudeAndlongitude.get('latitudes'),latitudeAndlongitude.get('longitude')), headers=headers, proxies=get_proxy())

        print('第{0}页商家'.format(pageIndex + 1))
        return res.json().get('items')

    def getComments(self,id,latitudeAndlongitude):

        commentHeaders['x-shard'] = 'shopid={0};loc={1},{2}'.format(id,latitudeAndlongitude.get('longitude'),latitudeAndlongitude.get('latitude'))
        commentHeaders['cookie'] = self.Cookie

        time.sleep(2+random.random())
        res = requests.get(commentURL.format(id), headers=commentHeaders, proxies=get_proxy())
        return res.json()

    def getInfo(self,id):
        infoPayload['restaurant_id'] = id
        infoPayload['user_id'] = parseCookie(self.Cookie).get('user_id')

        time.sleep(2+random.random())
        res = requests.post(infoURL, data=json.dumps(infoPayload), headers=headers, proxies=get_proxy())
        return res.json().get('cart').get('restaurant').get('address')
