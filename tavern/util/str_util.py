# -*- coding: utf-8 -*-
import os,sys
import random

# 随机生成8位字符
def randomString(num = 8, checked = ""):
	seed = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
	salt = []
	for i in range(num):
		salt.append(random.choice(seed))
	random_string = checked + ''.join(salt)
	return random_string

# 给定一个数据，返回随机元素
def randomItem(arr):
	random_item = random.choice(arr)
	return random_item

# 给定整数的最大值和最小值，返回随机数字
def randomNum(Min,Max):
	random_num = random.randint(Min,Max)
	return random_num

def randomSetsOfNum(Min,Max,is_inside = True):
	if Min == Max:
		if is_inside:
			return [randomNum(Min)]
		return 
	return [Min-1,Max+1]

def randomSetsOfString(Min,Max,is_inside = True):
	if is_inside:
		sets = [randomString(Min), randomString(randomNum(Min+1, Max-1)), randomString(Max)]
	else:
		if Min == 0:
			sets = [randomString(Max+1)]
		else:
			sets = [randomString(Min-1),randomString(Max+1)]
	return sets