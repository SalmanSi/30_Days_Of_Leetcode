class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)

        processorTime.sort()
        tindex=0
        ans=0
        for i in range(len(processorTime)):
            bigger=tasks[tindex]
            tindex+=4

            ans=max(ans,processorTime[i]+bigger)

        return ans