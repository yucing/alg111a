# A = 65
# ord() -> 取得ascii
# chr() -> ascii轉成字元
'''list_a = [97,98]
for i in list_a:
    print(chr(i))'''
count = 1
C = []

def main(n,k):
    for i in range(n):
        charTemp = chr(i+65)
        C.append(charTemp)
    print("從 {} 取 {} 個".format(C,k))
    co = (int(countLoop(n,k)))
    answer(co, k, n, 0)
    print("共 {} 總".format(co))

def countLoop(n,k):
    global count
    if(k == 0):
        return count
    count = count * n / k
    n -= 1
    k -= 1
    return countLoop(n,k)

def answer(co, k, n, Loop):
    if Loop * k >= co :
        return
    temp = []
    temp.append(C[Loop])
    La(temp, k, n, Loop, 1)
    Loop += 1
    return answer(co, k, n, Loop)

def La(temp, k, n, Loop, ktt):
    if ktt > k:
        return
    for j in range(Loop + 1, n):
        ktt += 1
        temp.append(C[j])
        if ktt < k:
            La(temp, k, n, Loop + 1, ktt)
        if len(temp) == k:
            print(temp)
        temp.pop()

main(4,2)