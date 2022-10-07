# A = 65
# ord() -> 取得ascii
# chr() -> ascii轉成字元
'''list_a = [97,98]
for i in list_a:
    print(chr(i))'''
C = []

def main(n,k):
    for i in range(n):
        charTemp = chr(i+65)
        C.append(charTemp)
    print("從 {} 取 {} 個".format(C,k))
    co = (int(countLoop(n,k,1)))
    temp = []
    answer(n, k , temp)
    print("共 {} 總".format(co))

def countLoop(n,k,count):
    if(k == 0):
        return count
    count = count * n / k
    n -= 1
    k -= 1
    return countLoop(n,k,count)

def answer(n, k, temp):
    for i in range(n+1-k):
        temp.append(C[i])
        answer2(n, k ,temp, i+1)
        temp = []

def answer2(n, k, temp, i):
    if len(temp) < k:
        temp.append(C[i])
        return answer2(n, k, temp, i+1)
    if len(temp) == k:
        print(temp)

main(4,2)