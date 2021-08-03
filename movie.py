import pandas as pd
from matplotlibimport pyplot as plt
from functoolsimport reduce
 
file_path= './IMDB-Movie-data.csv'
df= pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())
 
# rating,runtime分布情况
# 选择图形：直方图
# 准备数据
# runtime_data = df['Runtime (Minutes)'].values
rate_data= df['Rating'].values
max_rate= rate_data.max()
min_rate= rate_data.min()
 
#设置不等宽组距，hist方法中取到的会是一个左闭右开的区间[1,9,3.5)
num_bin_list= [1.9,3.5]
i= 3.5
while i<=max_rate:
    i+= 0.5
    num_bin_list.append(i)
print(num_bin_list)
 
#设置图形大小
plt.figure(figsize=(13,6),dpi=80)
#画直方图
plt.hist(rate_data,num_bin_list)
 
#xticks让之前的组距能够对上
plt.xticks(num_bin_list)
 
#显示
plt.show()
　　