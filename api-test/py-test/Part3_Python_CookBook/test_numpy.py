#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: HuHao <huhao1@cmcm.com>
Date: '2018/7/21'
Info:
        
"""

import os,traceback
import numpy as np


def test_plain():
	x = [1,2,3,4]
	y = [4,5,6,7]
	print(x*2) # [1, 2, 3, 4, 1, 2, 3, 4] 并不是想要的翻倍效果
	# print(x+10) # list 与 int 不能进行concatenate 合并
	
	
def f(x):
	return 3*x**2 - 2*x + 7

	
def test_numpy():
	'''
	对 numpy 数组匹配操作，比通过循环简单调用math 函数快很多
	:return:
	'''
	ax = np.array([1,2,3,4])
	ay = np.array([5,6,7,8])
	print(ax*2) # [2 4 6 8] 值翻倍
	print(ax+10) # [11 12 13 14] 值全部 +10
	print(ax+ay) # [ 6  8 10 12] 按索引相加
	print(ax*ay) # 对应索引位置相乘
	print(ax/(ay*1.0)) # [ 5.          3.          2.33333333  2.        ]
	
	print(f(ax)) # [ 8 15 28 47] 对每一个元素调用函数
	print(np.sqrt(ax)) # 调用内置函数 [ 1.          1.41421356  1.73205081  2.        ]


def test_zero():
	'''
	底层实现中，NumPy 数组使用了 C 或者 Fortran 语言的机制分配内存。也就是说， 它们是一个非常大的连续的并由同类型数据组成的内存区域。
	所以，你可以构造一个比 普通 Python 列表大的多的数组。
	:return:
	'''
	grid = np.zeros(shape=(10000,10000),dtype=float)
	print(grid)
	'''
	[[ 0.  0.  0. ...,  0.  0.  0.]
	 [ 0.  0.  0. ...,  0.  0.  0.]
	 [ 0.  0.  0. ...,  0.  0.  0.]
	 ...,
	 [ 0.  0.  0. ...,  0.  0.  0.]
	 [ 0.  0.  0. ...,  0.  0.  0.]
	 [ 0.  0.  0. ...,  0.  0.  0.]]
	'''
	
	grid += 10
	print(grid)
	'''
	[[ 10.  10.  10. ...,  10.  10.  10.]
	 [ 10.  10.  10. ...,  10.  10.  10.]
	 [ 10.  10.  10. ...,  10.  10.  10.]
	 ...,
	 [ 10.  10.  10. ...,  10.  10.  10.]
	 [ 10.  10.  10. ...,  10.  10.  10.]
	 [ 10.  10.  10. ...,  10.  10.  10.]]
	'''
	print(np.sin(grid))
	pass

def test_arr():
	a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
	print(a)
	'''
	[[ 1  2  3  4] 第0列
	 [ 5  6  7  8] 第1列
	 [ 9 10 11 12]]第2列
	'''
	print(a[1])  # 第1列 [5 6 7 8]
	print(a[:,1]) # 第1行 [ 2  6 10]
	print(a[1:3,1:3]) # [1,3) 列 [1,3) 行
	'''
	[[ 6  7]
    [10 11]]
	'''
	
	a[1:3,1:3] +=10
	print(a)
	'''
	[[ 1  2  3  4]
	 [ 5 16 17  8]
	 [ 9 20 21 12]]
	'''
	
	print(a+[100,101,102,103]) # 列加
	'''
	[[101 103 105 107]
	 [105 117 119 111]
	 [109 121 123 115]]
	'''
	
	print(np.where(a<10,a,10)) # a 中元素小于10 就取该元素，否则就取10
	'''
	[[ 1  2  3  4]
	 [ 5 10 10  8]
	 [ 9 10 10 10]]
	'''
	
	pass

def test_matrix():
	m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
	print(m)
	'''
	[[ 1 -2  3]
	 [ 0  4  5]
	 [ 7  8 -9]]
	'''
	print(m.T) # 转置
	'''
	[[ 1  0  7]
	 [-2  4  8]
	 [ 3  5 -9]]
	'''
	print(m.I) #  逆矩阵
	'''
	[[ 0.33043478 -0.02608696  0.09565217]
	 [-0.15217391  0.13043478  0.02173913]
	 [ 0.12173913  0.09565217 -0.0173913 ]]
	'''
	print(m*(m.I)) # 矩阵*逆矩阵 = 单维矩阵 2*1/2 = 1
	'''
	[[  1.00000000e+00   0.00000000e+00   0.00000000e+00]
	 [ -1.38777878e-17   1.00000000e+00   0.00000000e+00]
	 [ -2.22044605e-16   0.00000000e+00   1.00000000e+00]]
	'''
	
	v = np.matrix([[2],[3],[4]])
	print(v) # 1列3行矩阵
	'''
	[[2]
    [3]
    [4]]
	'''
	
	print(m*v)
	'''
	(3,3) * (1,3) = (1,3)
	[[ 1 -2  3]      [[2]    |[ 1 -2  3]*[2 3 4]|   |8 |
	 [ 0  4  5]   *   [3]  = |[ 0  4  5]*[2 3 4]| = |32|
	 [ 7  8 -9]]     [4]]    |[ 7  8 -9]*[2 3 4]|   |2 |
	[[ 8]
    [32]
    [ 2]]
	'''
	
def test_linalg():
	m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
	v = np.matrix([[2],[3],[4]])
	
	print(np.linalg.det(m)) # -230.0 求矩阵行列式
	print(np.linalg.eigvals(m)) # 求矩阵特征值 [-13.11474312   2.75956154   6.35518158]
	print(np.linalg.eig(m)) # 求矩阵的特征值和特征矩阵
	'''
	(array([-13.11474312,   2.75956154,   6.35518158]),
	 matrix([[ 0.2368169 , -0.83437342,  0.09866106],
        [ 0.27244696,  0.53498201, -0.90024871],
        [-0.93257193, -0.13272245, -0.42404983]]))
	'''
	
	x = np.linalg.solve(m,v) # 求 mx = v 特征向量
	print(x)
	'''
	[[ 0.96521739]
	 [ 0.17391304]
	 [ 0.46086957]]
	'''
	
	print(m*x)
	'''
	[[ 2.]
    [ 3.]
    [ 4.]]
	'''


if __name__=="__main__":
	try:
		# test_plain()
		# test_numpy()
		# test_zero()
		# test_arr()
		# test_matrix()
		test_linalg()
		pass
	except:
		traceback.print_exc()
	finally:
		os._exit(0)




