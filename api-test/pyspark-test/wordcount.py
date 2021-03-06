#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: HuHao <huhao1@cmcm.com>
Date: '2018/6/29'
Info:
	没有提示信息，必须开启 spark集群 （当前spark 托管给了 yarn）
        
"""
import pyspark
from pyspark import SparkContext
from pyspark import SparkConf

import os,traceback

if __name__=="__main__":
	try:
		conf=SparkConf().setAppName("miniProject").setMaster("local[*]")
		sc=SparkContext.getOrCreate(conf)
		
		#（a）利用list创建一个RDD;使用sc.parallelize可以把Python list，NumPy array或者Pandas Series,Pandas DataFrame转成Spark RDD。
		rdd = sc.parallelize([1,2,3,4,5])
		rdd
		#Output:ParallelCollectionRDD[0] at parallelize at PythonRDD.scala:480
		
		#（b）getNumPartitions()方法查看list被分成了几部分
		pt = rdd.getNumPartitions()
		print(pt)
	except:
		traceback.print_exc()
	finally:
		os._exit(0)