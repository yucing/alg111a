# 自行尋找問題 Leetcode
# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/solutions/)
```
Given an integer array nums, find the subarray with the largest sum, and return its sum.
```
```
Example 1
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```
```
Example 2
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```
```
Example 3
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```
## 暴力法
* 利用2個 for 迴圈，跑所有的值，並輸出最大值
* 為自己原創
### 程式
```py
class Solution(object):
    def maxSubArray(self, nums):
        # 設第一個值為max
        max = nums[0]
        # 從第一個跑到最後
        for i in range(len(nums)):
            sum = 0
            # 從i跑到最後，找出最大的數
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum > max:
                    max = sum

        return max
```
### 計算過程
* nums = [-2,1,-3,4,-1,2,1,-5,4]
```
[-2, -1, -4, 0, -1, 1, 2, -3, 1]
[1, -2, 2, 1, 3, 4, -1, 3]
[-3, 1, 0, 2, 3, -2, 2]
[4, 3, 5, 6, 1, 5]
[-1, 1, 2, -3, 1]
[2, 3, -2, 2]
[1, -4, 0]
[-5, -1]
[4]
```
### 測試
```
nums = [-2,1,-3,4,-1,2,1,-5,4]
6
nums = [1]
1
nums = [5,4,-1,7,8]
6
```

### LeetCode 測試
* 超時

![](https://github.com/yucing/alg111a/blob/main/picture/11.png)


## 動態規劃
* 為參考其他人程式，並完全理解
### 程式
```py
class Solution(object):
    def maxSubArray(self, nums):
        # 建立一個空陣列
        arr = []
        # 推入第一個數
        arr.append(nums[0])
        # maxSum 設值為第一個數
        maxSum = arr[0]
        for i in range(1, len(nums)):
            # arr[i-1] + nums[i] > num[i] ? arr.append(arr[i-1] + nums[i]) | arr.append(nums[i])
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            # 找出陣列 arr 中最大的值，並推入 maxSum
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum
```
### 推入過程
* nums = [-2,1,-3,4,-1,2,1,-5,4]
```
[-2, 1]
[-2, 1, -2]
[-2, 1, -2, 4]
[-2, 1, -2, 4, 3]
[-2, 1, -2, 4, 3, 5]
[-2, 1, -2, 4, 3, 5, 6]
[-2, 1, -2, 4, 3, 5, 6, 1]
[-2, 1, -2, 4, 3, 5, 6, 1, 5]
```

### 測試
```
nums = [-2,1,-3,4,-1,2,1,-5,4]
6
nums = [1]
1
nums = [5,4,-1,7,8]
6
```

### LeetCode 測試
* Accepted

![](https://github.com/yucing/alg111a/blob/main/picture/12.png)

## 其他方法
* 參考其他人程式，並完全了解
### 程式
```py
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 初始化 max_sum, 並將值設為 nums[0]
        max_sum = nums[0]
        # 初始化 current_sum，並設值為 0
        current_sum = 0
        for i in range(len(nums)):  
            # 如果 current < 0, 表示 current 加上其他數會變小，因此將值初始化
            if current_sum < 0:
                current_sum = 0
            # 計算目前加總
            current_sum += nums[i]
            # 如果目前 current_sum 加總完大於 max_sum，將 max_sum值設為 current_sum
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
```
### 計算過程
* nums = [-2,1,-3,4,-1,2,1,-5,4]
```
[-2, 1, -2, 4, 3, 5, 6, 1, 5]
```
### 測試
```
nums = [-2,1,-3,4,-1,2,1,-5,4]
6
nums = [1]
1
nums = [5,4,-1,7,8]
6
```

### LeetCode 測試
* Accepted

![](https://github.com/yucing/alg111a/blob/main/picture/13.png)
