# 2022/9/28 演算法 第四週

# 動態規劃 編輯距離
## [維基百科](https://zh.m.wikipedia.org/zh-tw/%E7%B7%A8%E8%BC%AF%E8%B7%9D%E9%9B%A2)
### 來文斯坦距離
* 可刪除、加入、取代
### LCS 最長公共子序列
* 只可刪除、加入
### Jaro
* 只可字符轉置
### 漢明距離
* 只可取代
## 舉例
* kitten -> sitting
### 來文斯坦 : 3
```md
1. kitten -> sitten
2. sitten -> sittin
3. sittin -> sitting
```
### LCS : 5
```md
1. kitten -> itten
2. itten -> sitten
3. sitten -> sittn
4. sittn -> sittin
5. sittin -> sitting
```
## 範例
* editDistance.py

# 分割擊破法 \ 分治法 Divide and conquer
## [iT邦幫忙](https://ithelp.ithome.com.tw/articles/10281926?sc=iThelpR)
## 常見例子
* 二分搜尋法
* 合併排序
## 範例
* binSearch.py
* binArraySearch.py