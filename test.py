from functools import reduce

a = range(1,5)
print(list(map(lambda x:x*x, a))) # 映射
print(list(filter(lambda x:x%2==1, a))) # 過濾
print(reduce(lambda x,y:x+y, a)) # 加總