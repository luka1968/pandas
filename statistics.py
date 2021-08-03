# -*- coding: utf-8 -*-
 
"""
@Datetime: 2018/11/19
@Author: Zhang Yafei
"""
"""
对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
思路：重新构造一个全为0的数组，列名为分类，如果某一条数据中分类出现过，就让0变为1
"""
import numpy as np
import pandas as pd
from matplotlibimport pyplot as plt
from matplotlibimport font_manager
 
#中文字体
my_font= font_manager.FontProperties(family='SimHei')
#显示完整的列
pd.set_option('display.max_columns',None)
 
df= pd.read_csv('IMDB-Movie-Data.csv')
#统计分类列表
temp_list= df.Genre.str.split(',').tolist()
genre_list= list(set([ifor jin temp_listfor iin j]))
 
#构造全为0的数组
zero_df= pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
# print(zero_df)
#给每个电影出现分类的位置赋值1
for iin range(df.shape[0]):
    zero_df.loc[i,temp_list[i]]= 1
 
# print(zero_df.head(1))
genre_count= zero_df.sum(axis=0)
print(genre_count)
 
#排序
genre_count= genre_count.sort_values()
_x= genre_count.index
_y= genre_count.values
#画图
plt.figure(figsize=(15,6),dpi=80)
plt.bar(range(len(_x)),_y,width=0.4,color="orange")
plt.xticks(range(len(_x)),_x)
plt.title('电影分类统计图',fontproperties=my_font)
plt.show()