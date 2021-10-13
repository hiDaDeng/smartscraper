from smartscraper import SmartScraper

url = 'https://book.douban.com/tag/小说?start=0&type=T'

# 一般一个例子就会学会规律，如果为了精准学习，可以多加几个例子
#wanted_list = ["活着", "房思琪的初恋乐园", "白夜行"]

#这里只用了一个就学会了
wanted_dict = {"title":["活着"],
               "pub": ["余华 / 作家出版社 / 2012-8-1 / 20.00元"]
               }

#wanted_dict = {"title":"活着"}
#训练书名模板titleTemplate
scraper = SmartScraper()
results = scraper.build(url, wanted_dict=wanted_dict)
print(results)


results2 = scraper.get_result_similar('https://book.douban.com/tag/小说?start=20&type=T')

print(results2)