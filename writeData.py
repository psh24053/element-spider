import xlwt
from xlwt import  easyxf
from getData  import GetData
from parse import  parseCommentLabels

# 定义xlsx样式
defaultStyle = easyxf('font: name Arial;')


f = xlwt.Workbook()
sheet1 = f.add_sheet('spider',cell_overwrite_ok=True)

# 获取信息
row0 = {
    "商家":"name",
    "位置":"",
    "id": 'id',
    "月售":"recent_order_num",
    "人均消费":"averagePriceTip",
    "评价数":"recordCount",
    "compare_rating":"compare_rating",
    "口味分":"food_score",
    "order_rating_amount":"order_rating_amount",
    "overall_score":"overall_score",
    "包装分":"package_score",
    "rider_score":"rider_score",
    "service_score":"service_score",
    "shop_score":"shop_score",
    "taste_score":"taste_score",
    "全部":"",
    "好评":"",
    "差评":"",
    "有图":"",
    "最新":"",
    "差评频次":"",
    "味道好":"",
    "价格实惠":"",
    "贵":"",
    "推荐":"",
    "满意":"",
    "分量足":"",
    "服务好":"",
    "服务差":"",
    "包装精美":"",
    "送货快":"",
    "物美价廉":"",
    "菜品差":"",
    "主食不错":"",
    "菜品不错":"",
    "干净卫生":"",
    "食材新鲜":"",
    "够辣":""
}

class WriteData:
    # 写首行
    def writeFirst(self):
        first_col = sheet1.col(0)  # xlwt中是行和列都是从0开始计算的
        first_col.width = 256 * 40
        second_col = sheet1.col(1)  # xlwt中是行和列都是从0开始计算的
        second_col.width = 256 * 80
        # 写商家表第一行
        for i in range(0, len(list(row0.keys()))):
            sheet1.write(0, i, list(row0.keys())[i], defaultStyle)

    def write_excel(self,shopList, rowIndex,latitudeAndlongitude):

        for i in range(0, len(shopList)):
            currentRow = i + 1 + rowIndex * 8
            print('正在写第{1}页第{0}个商家数据'.format(currentRow, rowIndex + 1))

            # ##################################################################
            # 获取评论标签，获取一次即可，每次是一样的
            commentList = GetData().getComments(shopList[i].get('restaurant').get('id'),latitudeAndlongitude)
            if commentList.get('tags') is not None:
                commentLabels = parseCommentLabels(commentList.get('tags'))
                for columnIndex in range(0, len(list(row0.values()))):
                    if commentLabels.get(list(row0.keys())[columnIndex]) is not None:
                        # print('commentlabel{1}'.format(commentLabels.get(list(row0.values())[columnIndex])))
                        sheet1.write(currentRow, columnIndex, commentLabels.get(list(row0.keys())[columnIndex]),
                                     defaultStyle)
            # ##################################################################
            # 获取评分
            if commentList.get('rating') is not None:
                commentRatingLabels = commentList.get('rating')
                for columnIndex in range(0, len(list(row0.values()))):
                    if commentRatingLabels.get(list(row0.keys())[columnIndex]) is not None:
                        # print('commentlabel{1}'.format(commentLabels.get(list(row0.values())[columnIndex])))
                        sheet1.write(currentRow, columnIndex, commentRatingLabels.get(list(row0.keys())[columnIndex]),
                                     defaultStyle)
            # ##################################################################
            # 获取商家信息
            for columnIndex in range(0, len(list(row0.values()))):
                if shopList[i].get('restaurant').get(list(row0.values())[columnIndex]) is not None:
                    sheet1.write(currentRow, columnIndex,
                                 str(shopList[i].get('restaurant').get(list(row0.values())[columnIndex])),
                                 defaultStyle)
            # ##################################################################
            # 地址信息需要单独获取
            shopAddress = GetData().getInfo(shopList[i].get('restaurant').get('id'))
            sheet1.write(currentRow, 1, shopAddress,
                         defaultStyle)

            f.save('test.xls')
