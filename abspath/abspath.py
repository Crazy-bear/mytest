# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 17:44
# @Author  : Alex
# @Site    : 
# @File    : abspath.py
# @Software: PyCharm

# 方法一
# import os
#
#
# # 获取当前目录绝对路径
# dir_path = os.path.dirname(os.path.abspath(__file__))
# print('当前目录绝对路径：', dir_path)
#
#
# # 获取上级目录绝对路径
# dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('上级目录绝对路径：', dir_path)

# 方法二
# from os.path import *
# # 获取当前目录绝对路径
# dir_path = dirname(abspath(__file__))
# print('当前目录绝对路径：', dir_path)
#
# dir_path = dirname(dirname(abspath(__file__)))
# print('上级目录绝对路径：', dir_path)

# 方法三
import os
dir_path = os.path.abspath(os.path.split(__file__)[0])
print('当前目录绝对路径：', dir_path)

# 获取上级目录绝对路径
dir_path = os.path.abspath(os.path.split(os.path.split(__file__)[0])[0])
print('上级目录绝对路径：', dir_path)
