# -*- coding: utf-8 -*-
 
"""
@Datetime: 2018/11/19
@Author: Zhang Yafei
"""
"""
现在我们有一组关于全球星巴克店铺的统计数据，如果我想知道美国的星巴克数量和中国的哪个多，或者我想知道中国每个省份星巴克的数量的情况，那么应该怎么办？
思路：遍历一遍，每次加1 ？？？
"""
import pandas as pd
 
pd.set_option('display.max_columns',None)
 
df= pd.read_csv('starbucks_store_worldwide.csv')
# print(df.head(1))
# print(df.info())
grouped= df.groupby(by='Country')
# print(grouped)
 
# DataFrameGroupBy
# 可以进行遍历
# for i,j in grouped:
#     print(i)
#     print('-'*100)
#     print(j)
#     print('*'*100)
country_count= grouped['Brand'].count()
# print(country_count['US'])
# print(country_count['CN'])
 
#统计中国每个省份店铺的数量
china_data= df[df.Country== 'CN']
china_grouped= china_data.groupby(by='State/Province').count()['Brand']
# print(china_grouped)
#数据按照多个条件进行分组
brand_grouped= df['Brand'].groupby(by=[df['Country'],df['State/Province']]).count()
# print(brand_grouped)
# print(type(brand_grouped))
#数据按照多个条件进行分组,返回dataframe
brand_grouped1= df[['Brand']].groupby(by=[df['Country'],df['State/Province']]).count()
brand_grouped2= df.groupby(by=[df['Country'],df['State/Province']])[['Brand']].count()
brand_grouped3= df.groupby(by=[df['Country'],df['State/Province']]).count()[['Brand']]
# print(brand_grouped1)
# print(brand_grouped2)
# print(brand_grouped3)
#索引的方法和属性
print(brand_grouped1)
print(brand_grouped1.index)