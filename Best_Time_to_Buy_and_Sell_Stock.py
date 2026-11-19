# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6

#1. Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)
        return res

#2. Two Pointers
#bu soru aslinda bize solda kendisinden daha kucuk bir eleman olmayan, sagda ise kendisinden daha buyuk eleman olmayan iki elemanin farkini bulmamiz
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 ,1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l=r #eger soldaki eleman kontrol edilen sagdaki yeni sayidan kucuk olamiyorsa o zaman yeni en kucugumuz o sayi olacagindan hemen en soldaki konumunu terk edip yeni en soldaki konumun o sagdaki sayi olmasi lazimdir
            r+=1
        return maxP

#3. Dynamic Programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
