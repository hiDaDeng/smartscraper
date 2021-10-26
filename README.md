# SmartScraper: 简单、自动、快捷的Python网络爬虫

**Note**: The origin developer of SmartScraper  is **Alireza Mika**， I only change a little code of AutoScraper.



![img](https://user-images.githubusercontent.com/17881612/91968083-5ee92080-ed29-11ea-82ec-d99ec85367a5.png)

SmartScraper使页面数据抓取变得容易，不再需要学习诸如pyquery、beautifulsoup等定位包，我们只需要提供的url和数据给ta学习网页定位规律即可。


## 一、安装

```bash
pip install smartscraper
```

<br><br>

## 二、快速上手

### 2.1 获取相似结果

例如 我们想从 **豆瓣读书-小说** 页面获得20本书的书名和出版信息

- P1  https://book.douban.com/tag/小说?start=0&type=T
- P2  https://book.douban.com/tag/小说?start=20&type=T

![](img/douban.png)

我们使用P1链接训练**书名、出版信息**这两个字段

```python
from smartscraper import SmartScraper

# 待训练的网页链接
url = 'https://book.douban.com/tag/小说?start=0&type=T'

#定义 想要的字段
wanted_dict = {"title":["活着"],
               "pub": ["余华 / 作家出版社 / 2012-8-1 / 20.00元"]
              }

# 训练/在url对应的页面中寻找wanted_dict规律
scraper = SmartScraper()
results = scraper.build(url, wanted_dict=wanted_dict)
print(results)
```

运行代码，采集到的results如下

```python
{'title': ['活着', 
           '房思琪的初恋乐园', 
           '白夜行', 
           '索拉里斯星', 
           '鄙视',
           ...], 
 'pub': ['余华 / 作家出版社 / 2012-8-1 / 20.00元', 
         '林奕含 / 北京联合出版公司 / 2018-2 / 45.00元', 
         '[日] 东野圭吾 / 刘姿君 / 南海出版公司 / 2013-1-1 / CNY 39.50', 
         '[波] 斯坦尼斯瓦夫·莱姆 / 靖振忠 / 译林出版社 / 2021-8 / 49.00元', 
         '[意] 阿尔贝托·莫拉维亚 / 沈萼梅、刘锡荣 / 江苏凤凰文艺出版社 / 2021-7 / 62.00',
          ...]
}

```

使用刚刚训练的scraper尝试从 **P2链接** 获取书名和出版信息

```python
scraper.get_result_similar('https://book.douban.com/tag/小说?start=20&type=T')
```

<br>



### 2.2 保存数据

每次运行方法``get_result_similar``后可结合save一起使用，数据将以**追加**形式存入 **csv**中。

```python
scraper.save(file_path='data.csv')
```



### 2.3 保存模型

训练的smartscraper模型可以保存，后续直接调用

```python
scraper.save('douban_Book.pkl')
```

模型导入代码

```python
scraper.load('douban_Book.pkl')
```

<br><br>

## 三、完整代码

假设我们要采集豆瓣小说前10页的所有数据，代码如下

```python
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


```



<br><br>

## 四、其他

### 4.1 项目补充说明

- SmartScraper仅为了简化使用，对AutoScraper进行了小修改（几行代码）

- 原创项目地址  https://github.com/alirezamika/autoscraper

<br><br>

###  4.2 相关课程

如果您是经管人文社科专业背景，编程小白，面临海量文本数据采集和处理分析艰巨任务，个人建议学习[《python网络爬虫与文本数据分析》](https://ke.qq.com/course/482241?tuin=163164df)视频课。作为文科生，一样也是从两眼一抹黑开始，这门课程是用五年时间凝缩出来的。自认为讲的很通俗易懂o(*￣︶￣*)o，

- python入门
- 网络爬虫
- 数据读取
- 文本分析入门
- 机器学习与文本分析
- 文本分析在经管研究中的应用

感兴趣的童鞋不妨 戳一下[《python网络爬虫与文本数据分析》](https://ke.qq.com/course/482241?tuin=163164df)进来看看~
[![](img/课程.png)](https://ke.qq.com/course/482241?tuin=163164df)



### 4.3 自媒体

- [B站:大邓和他的python](https://space.bilibili.com/122592901/channel/detail?cid=66008)

- **公众号：大邓和他的python**

  





