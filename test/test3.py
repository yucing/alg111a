import random
max_num = 5
h = 1

coefs = [[5, 7, 9, 2, 1],
        [18, 4, -9, 10, 12],
        [4, 7, 3, 8, 5],
        [5, 13, 15, 3, -7]]

maxs = [250,  285, 211, 315]

num = [7, 8, 2, 9, 6]

current_answer = [0, 0, 0, 0, 0]
current_temp1 = [0, 0, 0, 0, 0]
current_temp2 = [0, 0, 0, 0, 0]

answer = [0, 0, 0, 0, 0]

# 主程式
def Climbing():
    failCount = 0
    while failCount < 1000:
        for i in range(max_num):
            dh = random.randint(0,h)
            current_temp1[i] += dh
            current_temp2[i] -= dh
            a = Count(current_temp1)
            b = Count(current_temp2)
            if a >= b:
                for j in range(max_num):
                    current_answer[j] = current_temp1[j]
            else:
                for j in range(max_num):
                    current_answer[j] = current_temp2[j]

            if limit(current_answer) == False:
                failCount += 1
            elif limit(current_answer) == True:
                Move()
                failCount = 0
    print(answer, Count(answer))
            
# 移動
def Move():
    for i in range(max_num):
        answer[i] = current_answer[i]
        current_temp1[i] = current_answer[i]
        current_temp2[i] = current_answer[i]

# 計算大小
def Count(a):
    temp = 0
    for i in range(max_num):
        temp = temp + a[i]*num[i]
    return temp

# 限制
def limit(t):
    temp = 0
    for i in coefs:
        a = limitCount(i, t)
        if a > maxs[temp]:
            return False
        temp += 1
    return True

# 限制大小
def limitCount(a, b):
    temp = 0
    for i in range(max_num):
        temp = temp + a[i]*b[i]
    return temp

Climbing()