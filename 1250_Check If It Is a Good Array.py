'''
2020-9-22 最大公约数
Topic:
https://leetcode-cn.com/problems/check-if-it-is-a-good-array/

Hint:
裴蜀定理 https://zh.wikipedia.org/wiki/%E8%B2%9D%E7%A5%96%E7%AD%89%E5%BC%8F
简单来说，对于a1,a2,a3,... an 的 n 个数， 一定存在 a1 * n1 + a2 * n2 + a3 * n3 + ... + an * nn = d 。 其中 n1,n2,n3...nn 是正整数， d 为 a1,a2,a3,... an 的 n 个数的最大公约数。

'''

class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # def gcd(x: int, y: int) -> int:  也可写出输入变量及输出的type
        def gcd(x, y):  # 本质均为x大y小，即使不是执行一次后也会变成x大y小
            if x%y == 0:
                return y
            else:
                return gcd(y,x%y)

        gg = nums[0]
        for number in nums:
            gg = gcd(gg,number)
        return gg == 1

'''
Improvement: 

1. python 3中，可使用包计算最大公约数
import math
math.gcd()


2.非递归法
while b:
    a,b=b,a%b
print(a)


3.递归法
def gcd(x , y):
    if y == 0:
        print(x)
    else:
        gcd(y, x%y)

gcd(a,b)


4. 一行代码1
print(max([x for x in range(1,a+1) if a%x==0 and b%x==0]))


5. 一行代码2
print([x for x in range(1,a+1) if a % x ==0 and b % x ==0][-1])

'''
