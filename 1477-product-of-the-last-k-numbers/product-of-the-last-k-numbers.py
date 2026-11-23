class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]

    def add(self, num: int) -> None:
       
        if num == 0:
            # Reset the array when encountering 0
            # Any product containing 0 will be 0
            self.prefix_products = [1]
            return
      
        # Append the cumulative product
        # New product = last cumulative product * current number
        self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        
        if len(self.prefix_products) <= k:
            return 0
      
        # Calculate product of last k elements using prefix products
        # Product = (product of all elements) / (product of elements before the last k)
        return self.prefix_products[-1] // self.prefix_products[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
