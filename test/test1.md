# 限制條件
5ₓ₁ +7ₓ₂ +9ₓ₃ +2ₓ₄ +1ₓ₅ ≤ 250
18ₓ₁ +4ₓ₂ -9ₓ₃ +10ₓ₄ +12ₓ₅ ≤ 285
4ₓ₁ +7ₓ₂ +3ₓ₃ +8ₓ₄ +5ₓ₅ ≤ 211
5ₓ₁ +13ₓ₂ +16ₓ₃ +3ₓ₄ -7ₓ₅ ≤ 315

# 求值得最大值為
7ₓ₁ +8ₓ₂ +2ₓ₃ +6ₓ₄ +9ₓ₅

# 爬山
* 答案 [8, 8, 8, 8, 7] 247
```py
import random
max_num = 5
h = 1

coefs = [[5, 7, 9, 2, 1],
        [18, 4, -9, 10, 12],
        [4, 7, 3, 8, 5],
        [5, 13, 15, 3, -7]]

maxs = [250,  285, 211, 315]

num = [7, 8, 2, 6, 9]

current_answer = [0, 0, 0, 0, 0]
current_temp1 = [0, 0, 0, 0, 0]
current_temp2 = [0, 0, 0, 0, 0]

answer = [0, 0, 0, 0, 0]

# 主程式
def Climbing():
    failCount = 0
    while failCount < 100:
        dh = random.randint(0,h)
        for i in range(max_num):
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
```