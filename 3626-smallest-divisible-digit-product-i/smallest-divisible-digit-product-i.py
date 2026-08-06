class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            #pro = 1
            # for digit in n:
            product = 1
            for digit in str(n):
                product *= int(digit)


            if product % t == 0:
                return n

            n += 1
        