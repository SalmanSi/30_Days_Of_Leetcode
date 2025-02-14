class ProductOfNumbers:

    def __init__(self):
        self.nums=[]
        self.prefixProduct=[1]
        self.prefixZeros=[0]
        self.totalProduct=1


    def add(self, num: int) -> None:
        self.nums.append(num)
        if num==0:
            self.prefixProduct.append(self.prefixProduct[-1])
            self.prefixZeros.append(self.prefixZeros[-1]+1)
            return
        self.totalProduct*=num
        self.prefixProduct.append(self.prefixProduct[-1]*num)
        self.prefixZeros.append(self.prefixZeros[-1])
    
        


    def getProduct(self, k: int) -> int:
        zeros=self.prefixZeros[-1]-self.prefixZeros[-(k+1)]
        if zeros:
            return 0
        ans=self.totalProduct//self.prefixProduct[-(k+1)]
        return ans
        




# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)