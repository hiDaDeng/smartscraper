from smartscraper import SmartScraper


# 网址规律
template = 'https://book.douban.com/tag/小说?start={param}&type=T'


# 待训练的网页链接
train_url = template.format(param=0)
#定义 想要的字段
wanted_dict = {"title":["活着"],
               "pub": ["余华 / 作家出版社 / 2012-8-1 / 20.00元"]}
# 训练/在url对应的页面中寻找wanted_dict规律
scraper = SmartScraper()
scraper.build(train_url, wanted_dict=wanted_dict)



# 批量采集&存储
for pn in range(1, 11):
    url = template.format(param=(pn-1)*20)
    scraper.get_result_similar(url)
    scraper.save(file_path='data.csv')


