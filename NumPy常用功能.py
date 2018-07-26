
# coding: utf-8

# # NumPy常用功能汇总

# In[2]:


import numpy as np


# 1.创建矩阵的方法

# In[7]:


# 1.不适用NumPy的默认创建方法——类型为list
a = [[1,2,3],[1,2,3]]
# print(type(a1))
# 2.使用numpy生成一个3*4的矩阵，默认值为0
a = np.zeros([2,3])
# 3.利用range和arange创建矩阵，range只能是整数，arrange可以为小数
a = np.array(range(1,10,1))
a = np.arange(1,10,1.5)
# 4.利用[]和()都创建矩阵
a = np.array([[1,2],[3,4]])
a = np.array([(1,2),(3,4)])
# 5.利用random创建矩阵
a = np.random.random([3,4])
# 6.生成正态分布的矩阵
a = np.floor(np.random.randn(6,6))                         #标准正态分布
a = np.floor(np.random.normal(10,1,[6,6]))                 #普通正态分布
# print(a)


# 2.常用的功能

# In[136]:


#矩阵的秩
print('矩阵的秩为：{}'.format(a.ndim))
#矩阵的维度
print('矩阵的维度为：{}'.format(a.shape))
#矩阵的大小
print('矩阵的大小为：{}'.format(a.size))
#矩阵的数据类型
print('矩阵的数据类型为：{}'.format(a.dtype))
#矩阵的元素字节大小
print('矩阵的元素字节大小为：{}'.format(a.itemsize))
#矩阵的数据
print('矩阵的数据为：{}'.format(a.data))

#矩阵转换维度，reshape会返回一个矩阵，而resize则修改自身
#reshape和shape操作
print('--------修改b矩阵为12*3--------')
b = a.reshape([9,4])
b.shape = [9,4]
b.shape = (12,3)
print(b)
#resize操作
print('--------修改b矩阵为9*4--------')
b.resize([9,4])
print(b)
print('矩阵的类型为：{}'.format(type(b)))

#矩阵乘法，*表示按元素相乘，dot表示矩阵相乘
print(a*a)
c = a.reshape([4,9])
print(np.dot(c,b))

#元素向下取整
a = np.floor(a)

#矩阵索引、切片和迭代
print(a[1:3,3:5])

#遍历矩阵
for n in a:
    print('矩阵行遍历:{}'.format(n))
for n in a.flat:
    print('矩阵元素遍历:{}'.format(n))

#数组堆叠，按行合并vstack=column_stack，按列合并hstack=row_stack
m = a[1:4,1:4]
n = a[2:5,2:5]
print(np.vstack((m,n)))

#增加新维度newaxis，从一维变2D，变3D
p = a[:,:,np.newaxis]
print(p)
print(p.shape)
#矩阵分隔vsplit，hsplit

#矩阵比较，is和等号=
q = p.copy()
print(p is q)  #false
print(p == q)  #全为true的矩阵

#函数深浅拷贝，函数调用不会拷贝数组
q = p.copy()   #深拷贝
print(p is q)
q = p          #对象拷贝
print(p is q)

