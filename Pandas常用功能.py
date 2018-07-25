
# coding: utf-8

# # Pandas常用功能
# 除了Pandas的常用外，还包含一些tushare的用法，是一个整合了多种功能的文档

# In[18]:


import numpy as np
import tushare as ts
import pandas as pd
import matplotlib as plt


# 1. 数据结构

# In[36]:


#pandas主要有三种数据结构，Series、DataFrame、Panel，他们都建立在NumPy之上
#较高维的数据结构可以看做是较低维数据结构的容器
#Series一维结构
a = pd.Series([1,3,5,np.nan,'你好',8])
print(a)
print('--'*16)
dates = pd.date_range('20180724', periods=7)
print(dates)
#DataFrame二维结构
print('--'*16)
df = pd.DataFrame(np.floor(np.random.normal(10,1,[7,4])), index=dates, columns=list('ABCD'))
print(df)


# In[78]:


#系列的创建
#利用array进行创建
a = pd.Series(np.arange(1,10,0.8))
print(a)
#利用array，并加入索引
a = pd.Series(np.arange(1,10,0.8), index=range(3,39,3))
print(a)
#利用字典进行创建
a = pd.Series({'a':1, 'b':2}, index=['a','b','b','c'])
print(a)
print('系列中c对应的元素值为：{}'.format(a['c']))
a = pd.Series()
print(a)
#从标量创建一个系列
a = pd.Series(5, index=[1,2,3,4])
print(a)

#从具体位置访问系列中数据，只有通过列表创建的系列才能通过位置访问
a = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(a[2])
print(a[1:3])


# In[152]:


#数据帧DataFrame
#创建数据帧，index，columns等属性
b = pd.DataFrame([['张三',18],['李四',24],['周五',22]], index=['第一名','第二名','第三名'], columns=['姓名','年龄'], dtype=float)
print(b)
print('-+-'*10)
#通过字典创建数据帧
dict = {'姓名': ['张三','李四','周五'], '年龄': [17,26,31]}
b = pd.DataFrame(dict, index=['第一','第二','第三'])
print(b)
print('-+-'*10)
#多组字典创建数据帧，这就是典型的Json串类型
dict = [{'姓名':'张三'},{'姓名':'李四','年龄':18},{'姓名':'周五','年龄':22}]
b = pd.DataFrame(dict, index=['第一','第二','第三'])
print(b)
print('-+-'*10)
#通过系列进行创建
ser = {'one': pd.Series(['11','21','31'], index=['x','y','z']), 'two': pd.Series(['12','22','32'], index=['x','y','z1'])}
b = pd.DataFrame(ser, index=['x','y','z'])
print(b)
print('-+-'*10)

#添加一列数据
b['three'] = pd.Series(['13','23','33'], index=['x','y1','z'])
print(b)
print('-+-'*10)

#删除一列数据 del 或者 pop
# del b['three']
# print(b)
# b.pop('one')       # pop有返回值，返回的是删除的那列
# print(b)
# print('-+-'*10)

#选择一行数据
print(b.loc['x'])
#按整数位选择一行数据
print(b.iloc[2])
#行切片
print(b[1:3])
#增加一行
add = pd.DataFrame([{'one':'41', 'two':'42', 'three':'43'}], index = ['v'])
b = b.append(add, sort=True)            #注意append是有返回的
print(b)
#删除一行，注意，不能按整数位删除，而是根据index值进行删除
b = b.drop('z')            #注意drop是有返回的
print(b)


# In[ ]:


#面板Panel，属于3D容器

