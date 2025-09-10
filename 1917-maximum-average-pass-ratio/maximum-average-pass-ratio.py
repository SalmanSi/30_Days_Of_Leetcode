
class Solution:


    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def deltaRatio(cls: List):
            return (cls[0]+1)/(cls[1]+1) - (cls[0])/(cls[1]) 

        max_heap=[(-deltaRatio(cls), cls) for cls in classes]
        heapify(max_heap)

        for i in range(extraStudents):
            target=list(heappop(max_heap))
            target[1][0]+=1
            target[1][1]+=1
            target[0]=-deltaRatio(target[1])
            heappush(max_heap,tuple(target))
        ans=0
        for tups in max_heap:
            ans+=tups[1][0]/tups[1][1]
        return ans/len(classes)







    #   1- sort by denominator in ascnedingn order
    # cases:
    # increment the smaller denominator
    # if denominator same, incrermet the smaller numeraor
    # if numerator same, pick the 