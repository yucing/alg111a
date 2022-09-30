import random
max_num = 5

coefs = [[5, 7, 9, 2, 1],
        [18, 4, -9, 10, 12],
        [4, 7, 3, 8, 5],
        [5, 13, 15, 3, -7]]

maxs = [250,  285, 211, 315]

num = [7, 8, 2, 6, 9]

current_answer = [0, 0, 0, 0, 0]

answer = [0, 0, 0, 0, 0]

# 主程式
def Climbing(answer, h=1):
    failcount = 0
    while failcount < 10000:
        max = Count(answer)
        if MoveTF(max,h) == True:
            Move()
            failcount = 0
        else:
            failcount += 1

    print(answer,max)


# 計算此時的 max 大小
def Count(a):
    temp = 0
    for i in range(max_num):
        temp += a[i]*num[i]
    return temp

# 判斷是否移動
def MoveTF(a, h):
    for i in range(max_num):
        dh = random.randint(-h,h)
        current_answer[i] = current_answer[i]+dh
        if current_answer[i] < 0:
            current_answer[i] = 0
    if limit() == False:
        return False
    if(a <= Count(current_answer)):
        return True
    else:
        return False
# 移動
def Move():
    for i in range(max_num):
        answer[i]=current_answer[i]
    #print(answer)

# 判斷是否有超過限制
def limit():
    temp = 0
    for i in coefs:
        limit_num = LimitCount(i)
        if (limit_num >= maxs[temp]):
            return False
        temp += 1
    return True

# 計算
def LimitCount(a):
    temp = 0
    for i in range(max_num):
        temp = temp + current_answer[i]*a[i]
    return temp

def last():
    for i in range(4):
        for j in range(max_num):
            temp = coefs[i][j]*answer[j]
            if temp >= maxs[i]:
                return False
    return True

Climbing(answer)