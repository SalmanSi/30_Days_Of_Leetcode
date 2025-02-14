class ProductOfNumbers:

    def __init__(self):
        self.nums=[]
        self.prefixProduct=[1]
        self.size=0


    def add(self, num: int) -> None:
        if num==0:
            self.size=0
            self.prefixProduct=[1]
            return
        self.size+=1
        self.prefixProduct.append(self.prefixProduct[-1]*num)


    def getProduct(self, k: int) -> int:
        if k>self.size:
            return 0
        return self.prefixProduct[-1]//self.prefixProduct[-(k+1)]
        




# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)