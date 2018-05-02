
# Algorithm & Data structure| LeetCode_ 数组系列

由于对数据结构和算法掌握的不熟练，目前是小白入门阶段，痛下决心，要好好补一补。从大神大牛的算法学习，逐渐自己加强自身技能，若有理解错误，还望批评指教。---ZJ

[LeetCode](https://leetcode-cn.com/problems/two-sum/description/) | [数组系列](https://leetcode-cn.com/problemset/all/?topicSlugs=array)| [Leetbook](https://hk029.gitbooks.io/leetbook/content/%E6%95%B0%E7%BB%84/001.Two%20Sum[E].html)| [JackCui](https://blog.csdn.net/c406495762/article/details/79247243)|[LeetCode 探索](https://leetcode-cn.com/explore/)

# 1.两数之和 （Easy）

## 题目描述

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。


**示例:**

```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

```

自己的理解：

1. 遍历，双重 for 循环遍历
2. 我的想法很傻
3. 先学习大神们的算法

方法一：（96.65%）

学习原作者：[JackCui](https://blog.csdn.net/c406495762/article/details/79247243)的算法


```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 1. 先判断 nums 是否是 2 个数，<= 1 则返回 False
        if len(nums) <= 1:
            print("数组长度错误")
            return False
        # 2. 创建空字典
        result_dic = {}
        
        # 3. for 循环遍历 nums 的长度
        for i in range(len(nums)):
            print(i)
            # 4. 如果 nums 中 第 i 个元素是 字典中的 key
            # 那么返回 一个list ，list 中包含 result_dic 字典中 num[i] 作为 key 对应的 value 的值，以及 i 值，为最终结果
            if nums[i] in result_dic:
                print("result_dic :",result_dic)
                return [result_dic[nums[i]], i]
            # 5. 如果 nums 中 第 i 个元素不在字典中，
            # 那么 在字典中添加 以 target 减去 nums[i] 元素的值 作为 key ，value 为 索引值 i 
            else:
                 result_dic[target - nums[i]] = i
                   
```


```python
s = Solution()
print("result:",s.twoSum([6,0,0,2, 5, 11, 15,7], 9))
```

    0
    1
    2
    3
    4
    5
    6
    7
    result_dic : {3: 0, 9: 2, 7: 3, 4: 4, -2: 5, -6: 6}
    result: [3, 7]
    


```python
s = Solution()
print("result:",s.twoSum([1,5,0,2, 5, 11, 15,7], 6))
```

    0
    1
    result_dic : {5: 0}
    result: [0, 1]
    

**方法二：**


```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#         hash = {}
#         #循环nums数值，并添加映射
#         for i in range(len(nums)):
#             if target - nums[i] in hash:
#                 return [hash[target - nums[i]], i]
#             hash[nums[i]] = i
#         #无解的情况
#         return [-1, -1]
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        return [-1, -1]    
```

### 解释：

1. 从上面两个例子运算的过程及结果可以看出来，这个算法的巧妙之处在于，将原有的 加法问题，转换为以结果为主导的减法问题
2. result_dic 字典中的 key 是 target 减去 当前 i 值后的数，并记录 使得该算式成立的 i 值
3. 所以若 nums[i] 正存在于 result_dic 中，则又找到了与之前 存的内容正好匹配的 两个值，同时也对应着两个索引
4. 所以返回的是，之前存的 key 对应的 value （也就是其中一个索引值） 以及当前的 i 值

---

# 26. 删除排序数组中的重复项 (Easy)

## 题目描述

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

**示例 1:**

```
给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
```

**示例 2:**

```
给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

```

**说明:**

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

```
**方法一：**


```python
class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        i = 0
        while i < len(nums)-1:
            print(nums)
            if nums[i] == nums[i+1]:                
                del nums[i]
            else:
                i+=1
        return len(nums)  
    
#         new = list(set(nums))
#         new.sort()
#         length = len(new)
#         for i in range(length):
#             nums[i] = new[i]
#         return length    
```


```python
s1 = Solution1()
print("result:", s1.removeDuplicates([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]))
```

    [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 7, 9]
    [0, 1, 2, 3, 4, 7, 9]
    result: 7
    


```python
a = [0,3,4,9,1,1,0,3,4,7,2,2]
print(a)
a.sort() # 使用 list.sort() 方法来排序，此时 list 本身将被修改。
print(a) 
```

    [0, 3, 4, 9, 1, 1, 0, 3, 4, 7, 2, 2]
    [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    

**错误记录：**

1. 注意审题，“给定一个排序数组 ”，已经排好序，则从已经排好的序的角度去考虑，不要去考虑乱序的，哪怕真是乱序的 list ，那么第一步 也应该是先排序 ，之后再处理

**方法二：** 


```python
# 85.45% 60ms
class Solution2(object):
    """ 
    @param A: a list of integers 
    @return an integer 
    """  
    def removeDuplicates(self, nums):  
        #write your code here  
#         k=0  
#         for i in range(1,len(A)):  
#             if A[i] != A[k]:  
#                 k+=1  
#                 A[k] = A[i]  
          
#         del A[k+1:len(A)]  
#         return len(A)  
        # for-loop 遍历 nums 从 1 到 len(nums) 的长度，去除 长度为 0 的情况
        # 如果
        
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k+=1
                nums[k] = nums[i]
                print(nums)
             
        del nums[k+1:len(nums)]
        print(nums)
        return len(nums)
            
```


```python
s2 = Solution2()
print("result:", s2.removeDuplicates([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]))
```

    [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 7, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 7, 9, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 7, 9]
    result: 7
    


```python
# 56ms (不带 删除的代码) 60 ms 带有删除的代码   del nums[pos:len(nums)]
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        this_num = None
        for num in nums:
            if num != this_num:
                nums[pos] = num
                print(nums)
                this_num = num
                pos += 1
        del nums[pos:len(nums)]
        print(nums)
        return pos
```


```python
s2 = Solution()
print("result:", s2.removeDuplicates([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]))
```

    [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 1, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 2, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 2, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 7, 3, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 7, 9, 3, 4, 4, 7, 9]
    [0, 1, 2, 3, 4, 7, 9]
    result: 7
    

**总结：**

1. 法 1 和法 2 对比，明显 法 2 更快
2. 法 1 是两两对比，会将同一个数，跟其他的数多次对比判断
3. 法 2 用的则是，先找出来所有不相同的数，将不同的数赋值到最前面，最终能得到，所有唯一的数都排列在最前面，中间舍弃了一些相同的数，后面相同的数，最后也会被提取或删掉

---

# 121. 买卖股票的最佳时机 (Easy)

## 题目描述

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

**示例 1:**

```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```    
**示例 2:**

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```
**思路：**

1. 先找到最小值，然后再找最小值后面的最大值
2. 第 2 小值，以及第 2 小值后面的最大值 如：`[2, 9, 1, 3]`
3. 也就是所有小值，以及后面最大值 之间的差值，再比较哪个更大
4. 双指针遍历所有情况，选择最大利润。时间复杂度 $O(n^2)$ 

**方法一：**


```python
# 非常蠢的方法，没有通过测试用例
class Solution3(object):
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        result = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                print("i=%d, j=%d"%(i,j))
                result = max(result, prices[j] - prices[i])
                print(result)
        return result           
```


```python
s = Solution3()
print(s.maxProfit([7,6,4,3,1]))
```

    i=0, j=1
    0
    i=0, j=2
    0
    i=0, j=3
    0
    i=0, j=4
    0
    i=1, j=2
    0
    i=1, j=3
    0
    i=1, j=4
    0
    i=2, j=3
    0
    i=2, j=4
    0
    i=3, j=4
    0
    0
    

方法一 在 LeetCode 上没通过 199 / 200 个通过测试用例

最后执行的输入：
 `[10000,9999,9998,9997,9996,9995,9994,9993,9992,9991,9990,9989,9988,9....]`
 
超出时间限制 


**方法二：**

动态规划：选取最小的价格购买，保留最大的利润。只需一次遍历。时间复杂度$O(n)$ 

**思路：**


```python
# 73.33% 40 ms
class Solution(object):
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        # if len(prices) < 2:return 0
        if prices is None or len(prices) == 0:
            return 0
        begin_value = princes[0]
        result = 0
        for p in prices:
            result = max(result, p- begin_value)
            begin_value = min(begin_value, p)
        return result    
        
```


```python
s = Solution3()
print(s.maxProfit([7,6,4,3,1]))
```

    i=0, j=1
    0
    i=0, j=2
    0
    i=0, j=3
    0
    i=0, j=4
    0
    i=1, j=2
    0
    i=1, j=3
    0
    i=1, j=4
    0
    i=2, j=3
    0
    i=2, j=4
    0
    i=3, j=4
    0
    0
    

 **方法三：**


```python
# 32ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        revenue = 0
        
        prev = float('inf')
        
        for price in prices:
            if price < prev:
                prev = price
            else:
                revenue = max(price - prev, revenue)

        return revenue
```

Python 中可以用如下方式表示正负无穷：

`float("inf"), float("-inf")`

**方法四：**


```python
# 28ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0

        minBuy = prices[0]
        max_profit = 0
        for p in prices[1:]:
            if p < minBuy:
                minBuy = p
            if p - minBuy > max_profit:
                max_profit = p - minBuy

        return max_profit
```

---
# 122. 买卖股票的最佳时机 II (Easy)

## 题目描述

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

返回的是最大盈利的数字。

**示例 1:**

```
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
```    
**示例 2:**

```
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
``` 

**示例 3:**

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```


```python
# 36ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        result = 0
        Begin_value = prices[0]
        for p in prices:
            # 越复杂的问题，越要用简单的方式去思考
            # 只要后面的值大于前面的值 就卖出，并重新买入
            if p > Begin_value:
                result += p-Begin_value  #涨股利润累加
                Begin_value = p          #重新买股
            else:
                # 若后面的值，小于前面的值，则重新设置最小值                
                Begin_value = min(Begin_value, p)
        return result
```


```python
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
```

    7
    


```python
# 32ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = 0
        for i in range(n - 1):
            if prices[i + 1] - prices[i] >= 0:
                profit += prices[i + 1] - prices[i]
        return profit
```


```python
# 28ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for index in xrange(1, len(prices)):
            if prices[index] > prices[index - 1]:
                profit += prices[index] - prices[index - 1]
        return profit
```

xrange 用法与 range 完全相同，所不同的是生成的不是一个 list对象，而是一个生成器。
```
>>> xrange(5)
xrange(5)
>>> list(xrange(5))
[0, 1, 2, 3, 4]
>>> xrange(1,5)
xrange(1, 5)
>>> list(xrange(1,5))
[1, 2, 3, 4]
>>> xrange(0,6,2)
xrange(0, 6, 2)
>>> list(xrange(0,6,2))
[0, 2, 4]
```


---

# 189. 旋转数组 (Easy)

[旋转数组](https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/23/)

参考文章:[LeetCode:Rotate Array ](http://bookshadow.com/weblog/2015/02/24/leetcode-rotate-array/)

## 题目描述

将包含 n 个元素的数组向右旋转 k 步。

例如，如果  n = 7 ,  k = 3，给定数组  [1,2,3,4,5,6,7]  ，向右旋转后的结果为 [5,6,7,1,2,3,4]。

**注意:**

尽可能找到更多的解决方案，这里最少有三种不同的方法解决这个问题。

**提示:**

要求空间复杂度为 O(1)

关联的问题: 反转字符串中的单词 II

致谢:
特别感谢 @Freezen 添加此问题并创建所有测试用例。
 
**方法一 ：** 

时间复杂度O（n），空间复杂度O(1) 

思路：将数组元素依次循环向右平移 k 个单位

【目前理解这个方法还是很懵，脑袋清醒了 再回来看】


```python
# 方法一 时间复杂度O（n），空间复杂度O(1) 
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = 0
        distance = 0
        cur = nums[0]
        for x in range(n):
            # 取 % 这个操作 正好可以找到 当前索引位置的数要被转换到的位置            
            idx = (idx + k) % n
            print('idx', idx)
            # 两个数互换             
            nums[idx], cur = cur, nums[idx]
            # cur 存储当前被换出来的数             
            print('cur',cur)
            
            # cur 3 6 2 5 1 4             
            
            distance = (distance + k) % n
            # =0 代表恰好可以整除             
            if distance == 0:
                idx = (idx + 1) % n
                cur = nums[idx]
            print('nums2',nums) 
                    
```


```python
s = Solution()
print(s.rotate([1,2,3,4,5,6,7],3))
```

    idx 3
    cur 4
    nums2 [1, 2, 3, 1, 5, 6, 7]
    idx 6
    cur 7
    nums2 [1, 2, 3, 1, 5, 6, 4]
    idx 2
    cur 3
    nums2 [1, 2, 7, 1, 5, 6, 4]
    idx 5
    cur 6
    nums2 [1, 2, 7, 1, 5, 3, 4]
    idx 1
    cur 2
    nums2 [1, 6, 7, 1, 5, 3, 4]
    idx 4
    cur 5
    nums2 [1, 6, 7, 1, 2, 3, 4]
    idx 0
    cur 1
    nums2 [5, 6, 7, 1, 2, 3, 4]
    None
    

**方法二：** 

时间复杂度 O（n），空间复杂度O(1) 

思路： 以 n - k 为界，分别对数组的左右两边执行一次逆置；然后对整个数组执行逆置。


```python
# 方法二 时间复杂度O（n），空间复杂度O(1) 
class Solution(object):
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)
        print(nums)

    def reverse(self, nums, start, end):
        for x in range(start, int((start + end) / 2)):
            nums[x] ^= nums[start + end - x - 1]
            nums[start + end - x - 1] ^= nums[x]
            nums[x] ^= nums[start + end - x - 1]
```


```python
s = Solution()
print(s.rotate([1,2,3,4,5,6,7],3))
```

    [5, 6, 7, 1, 2, 3, 4]
    None
    

实现两个数交换：

a ^= b
b ^= a
a ^= b


```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums) 
        if k==0:
            return
        if(k<length):
            nums[0:k], nums[k:length] = nums[length-k:length], nums[0:length-k]
        elif(k>length):
            k = k - length
            nums[0:k], nums[k:length] = nums[length-k:length], nums[0:length-k]
        
```


```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 直接将 需要旋转的 k 个放到前面，前面的放到后面
        #  如：nums[4:] 从索引 4 开始一直到最后一个
        # nums[:4] 从 0 开始一直到 索引4 不包含 索引4  的值
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
```

# 217.存在重复(Easy)

## 题目描述

给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。


```python
# 不解释了
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
```

# 136. 只出现一次的数字(Easy)

## 题目描述

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

**说明：**

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

**示例 1:**
```
输入: [2,2,1]
输出: 1
```
**示例 2:**
```
输入: [4,1,2,1,2]
输出: 4
```
思路： 
1. 我的想法很蠢，不说了

参考：

[Leetcode解题思路总结(Medium)](https://blog.csdn.net/luoshengkim/article/details/50668684)

[LeetCode: Single Number解题思路](http://www.powerxing.com/leetcode-single-number/)

`a^a=0, a^0=a`，根据交换律`a^b=b^a`，比如`3^4^3=4`，根据异或操作的这种性质，我们可以将所有元素依次做异或操作，相同元素异或为 0，最终剩下的元素就为 Single Number。

因为`A XOR A = 0`，且`XOR`运算是可交换的，于是，对于实例`{2,1,4,5,2,4,1}`就会有这样的结果：

`(2^1^4^5^2^4^1) => ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5`

就把只出现了一次的元素(其余元素均出现两次)给找出来了！


```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        for item in nums:
            temp ^= item
            print(temp)

        return temp
                

```


```python
s = Solution()
print(s.singleNumber([4,1,2,1,2]))
```

    4
    5
    7
    6
    4
    4
    

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
     int count=0;
     for(int i=0;i<nums.size();i++){
         count^=nums[i];
      }
     return count;
}    
};

```

`^`按位异或运算符：当对应的二进位相异(不同)时，结果为 1 （不同为 1，相同为 0）	

(a ^ b) 输出结果 49 ，二进制解释： 0011 0001


```python
a = 60 # 0011 1100

b = 13 # 0000 1101 

a ^ b  # 0011 0001
```




    49



---

# 350. 两个数组的交集 II (Easy)

## 题目描述

给定两个数组，写一个方法来计算它们的交集。

**例如:**

给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

**注意：**

   输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
   (只跟次数有关，跟顺序无关)

   我们可以不考虑输出结果的顺序。
   
   例： nums1 = [3,3,3,3,3,3,1,1], nums2 = [1,3,3,3,2,1] 答案：` [3,3,3,1,1]` `[1,3,3,3,1]` 两个都对，跟顺序无关


**跟进:**

1. 如果给定的数组已经排好序呢？你将如何优化你的算法？
2. 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
3. 如果 nums2 的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？




```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 用来存储出现的 数字，以及与之对应的次数         
        nums_map = {}
        for i in nums2:
            if i in nums_map:
                nums_map[i] += 1
            else:
                nums_map[i] = 1
        # 存储 要返回的list 结果，与顺序无关
        print('nums_map',nums_map)
        res = []
        for i in nums1:
            if i in nums_map and nums_map[i] > 0:
                res += [i]
                print(res)
                # 前面的 字典中，有其中一个 nums 中元素出现的次数的统计，
                # 当遍历第二个的时候，每向 list 中添加一个 字典中统计的次数就减少一个
                nums_map[i] -= 1
                print('nums_map_final:',nums_map)
        return res
        
```


```python
s = Solution()
print('result:',s.intersect([1,3,3,3,3,3,3,3,3,3,3,3,2,1],[3,3,3,1,1]))
```

    nums_map {3: 3, 1: 2}
    [1]
    nums_map_final: {3: 3, 1: 1}
    [1, 3]
    nums_map_final: {3: 2, 1: 1}
    [1, 3, 3]
    nums_map_final: {3: 1, 1: 1}
    [1, 3, 3, 3]
    nums_map_final: {3: 0, 1: 1}
    [1, 3, 3, 3, 1]
    nums_map_final: {3: 0, 1: 0}
    result: [1, 3, 3, 3, 1]
    


```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = {}
        for x in nums1:
            if m.has_key(x):
                m[x] += 1
            else:
                m[x] = 1
        
        res = []
        for x in nums2:
            if m.has_key(x) and m[x] > 0:    
                res.append(x)
                m[x] -= 1
        return res
```

# 66. 加一 (Easy)

## 题目描述

给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

**示例 1:**

```
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
```
**示例 2:**

```
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
```
理解 & 思路：

[LeetCode 66. Plus One（加1）](https://www.cnblogs.com/jimmycheng/p/7223474.html)
[LeetCode 66](https://blog.csdn.net/zr1076311296/article/details/51705280)

这道题目给了我们一个 digits 的 array， 这个 array 等于一个数字，让我们加 1。

来分析一下，如果是不需要进位的 < 9 ， 那么直接加 1 就返回。

如果是需要进位的，=9， 那么我们需要把目前的 digit 改为0，接着继续检查前一位，因为你不确定前一位加 1 是不是需要进位。

一旦当我们找到不需要进位的那个 digit， 加 1 返回就可以了。

如果碰到一种极端的情况，类似于 999 的话，那么我们 遍历完之后 是 000， 还需要一个1 ，所以要重新建立一个array， size + 1，把 1 加在 [0] 的位置。

一个非负数的内容从高位到低位(十进制位)依次放到数组的每一位，例如：123，存放到数组中就是[1,2,3]，现在将这个数加 1 ，返回加1后的结果，如[1,2,3]应该返回[1,2,4].



```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        # 倒序，从 数组的最后一位开始， 4， 3,2 1,0         
        for i in range(len(digits))[::-1]:  
            # 先对数字进行 加 1 操作
            digits[i] += carry  
            if digits[i] > 9:  
                # digits[i] 原本 =9 , 加 1 后 大于 9 为 10 ，则需进一位。
                # 则  digits[i] -10 变为 0
                digits[i] -= 10  
                carry = 1  
            else:  
                carry = 0  
        # 这个针对于 都是 9999 这种情况 需要整个长度上 加 1 插入 索引 0 位  1                  
        if carry > 0:  
            print('digits:',digits)
            digits.insert(0, 1)  
        return digits  
    
```


```python
s = Solution()
print(s.plusOne([9,9,9,9,9,9]))
```

    digits: [0, 0, 0, 0, 0, 0]
    [1, 0, 0, 0, 0, 0, 0]
    


```python
for i in range(0,5)[::-1]:
    print(i)
    
a = [9,9,9,9]    

a.insert(0,1)
print(a)
```

    4
    3
    2
    1
    0
    [1, 9, 9, 9, 9]
    


```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        cur =1
        a=len(digits)
        for i in range(a):  
            # 用来实现倒数 a-1-i  4， 3,2,1             
            if digits[a-1-i]+cur>9:
                digits[a-1-i]=0
                cur=1
            else:
                digits[a-1-i]+=cur 
                cur=0
        if cur==1:
            digits.insert(0,1)
              
        return digits
        
```


```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 先把 list 转化成字符串，再转成 int 类型 进行 加 1 操作，
        # 之后再循环遍历转成 list
        tmp = ''
        for i in digits:
            tmp += str(i)
        tmp = int(tmp) + 1
        digits = [int(i) for i in list(str(tmp))]
        #  return [int(i) for i in str(tmp)]
        return digits
```

# 283. 移动零 (Easy)

## 题目描述

给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。

例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。

**注意事项:**

1. 必须在原数组上操作，不要为一个新数组分配额外空间。
2. 尽量减少操作总数。

**思路：**

1. 一开始的想法是，判断是 0 后，保持最前面的不动，把后面的前移，最后末尾再加 0 
2. 然后测试用例，后面几个没有通过
3. 看到别人的想法是 两两互换



```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        s = e = 0
        while e < len(nums):
            if nums[e]:
                nums[s] = nums[e]
                print('nums1:',nums)
                s += 1
            e += 1
            
        while s < len(nums):
            nums[s] = 0
            s += 1
            print('s:',s)
            print('nums2:',nums)     
```


```python
s = Solution()
print(s.moveZeroes([1,0,2,3,0,0,4,0,9]))
```

    nums1: [1, 0, 2, 3, 0, 0, 4, 0, 9]
    nums1: [1, 2, 2, 3, 0, 0, 4, 0, 9]
    nums1: [1, 2, 3, 3, 0, 0, 4, 0, 9]
    nums1: [1, 2, 3, 4, 0, 0, 4, 0, 9]
    nums1: [1, 2, 3, 4, 9, 0, 4, 0, 9]
    s: 6
    nums2: [1, 2, 3, 4, 9, 0, 4, 0, 9]
    s: 7
    nums2: [1, 2, 3, 4, 9, 0, 0, 0, 9]
    s: 8
    nums2: [1, 2, 3, 4, 9, 0, 0, 0, 9]
    s: 9
    nums2: [1, 2, 3, 4, 9, 0, 0, 0, 0]
    None
    


```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # point 记住的元素为 0 的索引位置 
        point = 0
        for i in range(len(nums)):
            # 当前位置元素不为 0 的情况下，跟之前记录的索引为 0 的值交换
            if nums[i]:
                nums[point] , nums[i] = nums[i], nums[point]
                point += 1
            print(nums)
            print("point:",point)
            print('i:',i,'\n'+('-'*30))
```


```python
s = Solution()
print(s.moveZeroes([0,1,0,2,3,0,0,4,0,9]))
```

    [0, 1, 0, 2, 3, 0, 0, 4, 0, 9]
    point: 0
    i: 0 
    ------------------------------
    nums[i] 1
    [1, 0, 0, 2, 3, 0, 0, 4, 0, 9]
    point: 1
    i: 1 
    ------------------------------
    [1, 0, 0, 2, 3, 0, 0, 4, 0, 9]
    point: 1
    i: 2 
    ------------------------------
    nums[i] 2
    [1, 2, 0, 0, 3, 0, 0, 4, 0, 9]
    point: 2
    i: 3 
    ------------------------------
    nums[i] 3
    [1, 2, 3, 0, 0, 0, 0, 4, 0, 9]
    point: 3
    i: 4 
    ------------------------------
    [1, 2, 3, 0, 0, 0, 0, 4, 0, 9]
    point: 3
    i: 5 
    ------------------------------
    [1, 2, 3, 0, 0, 0, 0, 4, 0, 9]
    point: 3
    i: 6 
    ------------------------------
    nums[i] 4
    [1, 2, 3, 4, 0, 0, 0, 0, 0, 9]
    point: 4
    i: 7 
    ------------------------------
    [1, 2, 3, 4, 0, 0, 0, 0, 0, 9]
    point: 4
    i: 8 
    ------------------------------
    nums[i] 9
    [1, 2, 3, 4, 9, 0, 0, 0, 0, 0]
    point: 5
    i: 9 
    ------------------------------
    None
    


```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num=0
        for i in range(len(nums)):
            if nums[i]==0:
                num+=1
            else:
                nums[i-num]=nums[i]
            print('nums:',nums)    
        aa=len(nums)
        for j in range(num):
            nums[aa-1-j]=0
            print('nums1:',nums)    
```


```python
s = Solution()
print(s.moveZeroes([1,0,2,3,0,0,4,0,9]))
```

    nums: [1, 0, 2, 3, 0, 0, 4, 0, 9]
    nums: [1, 0, 2, 3, 0, 0, 4, 0, 9]
    nums: [1, 2, 2, 3, 0, 0, 4, 0, 9]
    nums: [1, 2, 3, 3, 0, 0, 4, 0, 9]
    nums: [1, 2, 3, 3, 0, 0, 4, 0, 9]
    nums: [1, 2, 3, 3, 0, 0, 4, 0, 9]
    nums: [1, 2, 3, 4, 0, 0, 4, 0, 9]
    nums: [1, 2, 3, 4, 0, 0, 4, 0, 9]
    nums: [1, 2, 3, 4, 9, 0, 4, 0, 9]
    nums1: [1, 2, 3, 4, 9, 0, 4, 0, 0]
    nums1: [1, 2, 3, 4, 9, 0, 4, 0, 0]
    nums1: [1, 2, 3, 4, 9, 0, 0, 0, 0]
    nums1: [1, 2, 3, 4, 9, 0, 0, 0, 0]
    None
    

# 36. 有效的数独 (Medium)

## 题目描述

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

1. 数字 1-9 在每一行只能出现一次。
2. 数字 1-9 在每一列只能出现一次。
3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

数独部分空格内已填入了数字，空白格用 '.' 表示。

**示例 1:**

输入:
```
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

```
输出: true

**示例 2:**

输入:

```
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
```
输出: false

解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

**说明:**

- 一个有效的数独（部分已被填充）不一定是可解的。
- 只需要根据以上规则，验证已经填入的数字是否有效即可。
- 给定数独序列只包含数字 1-9 和字符 '.' 。
- 给定数独永远是 9x9 形式的。


https://blog.csdn.net/coder_orz/article/details/51596499

https://blog.csdn.net/yzp1011/article/details/79702496

https://blog.csdn.net/coder_orz/article/details/51596499

https://blog.csdn.net/runningtortoises/article/details/45830627

https://www.cnblogs.com/zhuifengjingling/p/5277555.html

思考：

1. 我目前的想法还是很蠢，不说了
2. 来自大神的思考，记录所有出现过的行、列、块的数字及相应位置，最后判断是否有重复。用 set 操作精简代码



```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
#       i: 所有的行索引（0-8），row 数组，每一行的数组  
        for i, row in enumerate(board):
#             print('i:',i, 'row:',row)
#           j: 所有的列索引（0-8），c ：每一个字符
            for j, c in enumerate(row):
                if c != '.':
#                     print('j:',j, 'c:',c)
#                     print('(i, c):',(i, c))
#                     print('(i/3, j/3, c):',i/3, j/3, c)
                    # (c, j) 表示 每一行中，每个字符数字，与之对应的位置 如  (c, j): ('5', 0) 就是 数字 5 在行中的位置 是 0 
                    # 这样就能判断 每一列是否有重复的数字
                    # (i, c) 表示，每一列中，列索引对应的字符数字，如： (0, '5') (0, '3')(0, '7') 代表 竖着看，按列来看，0 的 位置上 有 5  3  7 
                    # 则能判断 每一行是都有重复的数字 如重复出现 （0,5）（0,5）
                    # (i/3, j/3, c) ,三宫格 中(只考虑 三宫格内的 三行三列就可以) 对应的坐标位置及 字符数字
                    seen += [(c, j),(i, c),(i/3, j/3, c)] 
                    
#                     print('seen:\n',seen,'\n')       
        return len(seen) == len(set(seen))
```


```python
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

board1 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
s = Solution()
# print(s.isValidSudoku(board))
print(s.isValidSudoku(board1))
```

    False
    


```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.is_row_valid(board)) and (self.is_col_valid(board)) and (self.is_square_valid(board))
    
    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True
    
    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
    
    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
#               将 board 分成了 9 块 
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True
    
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
```


```python
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
# 相当于转置
print(*board)

for col in zip(*board):    
    print(col)
```

    ['5', '3', '.', '.', '7', '.', '.', '.', '.'] ['6', '.', '.', '1', '9', '5', '.', '.', '.'] ['.', '9', '8', '.', '.', '.', '.', '6', '.'] ['8', '.', '.', '.', '6', '.', '.', '.', '3'] ['4', '.', '.', '8', '.', '3', '.', '.', '1'] ['7', '.', '.', '.', '2', '.', '.', '.', '6'] ['.', '6', '.', '.', '.', '.', '2', '8', '.'] ['.', '.', '.', '4', '1', '9', '.', '.', '5'] ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ('5', '6', '.', '8', '4', '7', '.', '.', '.')
    ('3', '.', '9', '.', '.', '.', '6', '.', '.')
    ('.', '.', '8', '.', '.', '.', '.', '.', '.')
    ('.', '1', '.', '.', '8', '.', '.', '4', '.')
    ('7', '9', '.', '6', '.', '2', '.', '1', '8')
    ('.', '5', '.', '.', '3', '.', '.', '9', '.')
    ('.', '.', '.', '.', '.', '.', '2', '.', '.')
    ('.', '.', '6', '.', '.', '.', '8', '.', '7')
    ('.', '.', '.', '3', '1', '6', '.', '5', '9')
    

# 48. 旋转图像 （Medium）

给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

**说明：**

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

**示例 1:**

```
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```
**示例 2:**

```
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```
思路：

原矩阵的 i，j 会变到 j，(n-1)-i 这个位置上

（如果直接去换，此处有坑：遍历下一个的时候，可能已经变成最新的元素了，则又把它变走了）

所以先转置上三角，再每一行翻转


```python
class Solution1(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # i 行索引， j 列索引 先进行行列互换         
        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j],matrix[j][i]
                
        print('matrix:',matrix)  
        # 每一行翻转
        for i in range(n):
            matrix[i].reverse()

                
```


```python
class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        matrix[:] = map(list,zip(*matrix)) 

```

补：

对于 `map()` 它的原型是：`map(function,sequence)`，就是对序列`sequence`中每个元素都执行函数`function`操作。

对于`zip()`，原型是`zip(*list)`，`list`是一个列表，`zip(*list)`返回的是一个元组.

python 矩阵转置- 使用`zip()`函数和`map( )`函数

-  `map(list,zip(*matrix))`


```python
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

s1 = Solution1()
s1.rotate(matrix)
print('s1:',matrix)

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s2 = Solution2()
s2.rotate(matrix)
print('s2:',matrix)
```

    matrix [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    s1: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    s2: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    


```python
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

matrix.reverse()
print(matrix)
```

    [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    
