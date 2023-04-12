class Solution:
    def mergeIntervals(self,intervals):

        #at first we have to sort the intervals
        intervals.sort(key=lambda x: x[0])
        merged=[]
        for interval in intervals:
            #if merged array is empty or merged array's last element is less than interval's first element
            if len(merged)==0 or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1], interval[1])
        return merged
    
sol=Solution()
array=[[1,3],[2,6],[15,18],[8,10]]
print(sol.mergeIntervals(array))