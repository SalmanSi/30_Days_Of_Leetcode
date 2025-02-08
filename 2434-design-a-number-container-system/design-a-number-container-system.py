class NumberContainers:

    def __init__(self):
        self.number={}
        self.minIndex={}        

    def change(self, index: int, number: int) -> None:
        # case 1- nothing at that index so add number
        self.number[index]=number
        if number in self.minIndex:
            heapq.heappush(self.minIndex[number],index)
        else:
            self.minIndex[number]=[index]
        # case 3- new number so initlaze a list/heap to store its indices
        # case 4- old number, just push in heap

    def find(self, number: int) -> int:
        if number not in self.minIndex.keys():
            return -1
        
        heap=self.minIndex[number]
        while heap and self.number[heap[0]]!=number:
            heapq.heappop(heap)
        
        return heap[0] if heap else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)