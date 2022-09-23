# 2022/9/21 演算法 第三週
# random
## random seed
### 固定不變
```py
random.seed(數值)
# seed 保持不變
# random.random() -> 取得的序列都一樣
```
### 改變
```py
seed = time.time()%SEED_MAX
# seed 用時間去取
# 每次取得的 seed 會不同
```

# python math
## math.sin(x)
* 值會介在 0~1 間
## math.floor(x)
    Ex: 如果 x = 3.1
        傳回值為 3