class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) == 1:
            return -1

        n = len(prices)
        # print(n)
        max_profit = 0

        for i in range(n):
            current_profit = max(list(map(lambda x: prices[i] - x, prices[i + 1:])))
            if current_profit > max_profit:
                max_profit = current_profit
            # if max
            # for j in range(i + 1, n):
            #     current_profit = prices[j] - prices[i]
            #     if current_profit > max_profit:
            #         max_profit = current_profit
        print(max_profit)
        return max_profit

sol = Solution()
sol.maxProfit([7,1,5,3,6,4])
prices = [7,1,5,3,6,4]
# n = len(prices)
# for i in range(n):
#     print("Rahul")

print(list(map(lambda x : x -1,prices)))