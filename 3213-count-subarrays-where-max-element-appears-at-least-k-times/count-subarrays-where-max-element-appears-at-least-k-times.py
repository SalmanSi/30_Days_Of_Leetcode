class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # the problem asks to count subarrays GREATER than a condition
        # implementing this using sliding window becomes a bit complex
        # so we convert this problem to LESSER than a condition
        # count the sub arrays which follow these conditions and 
        # count the total possible sub arrays
        # subtract LESSER than count from total count to get the count of
        # GREATER than sub arrays. 

        
        max_element=max(nums) # need to count freq of this in our sub arrays
        i=0 # left pointer
        curr_count=0 # current number of max_element in our sub array
        total_subarrays=0 # total possible sub arrays
        complement_count=0 # count of sub arrays fulfilling the LESSER than condition

        # for loop to move the right pointer j
        # check if the current addtion to our window, nums[j]==max_element
        # compute total sub arrays
        # and then check if LESSER than condition fulfilled
        # if fullfilled, count the possible sub arrays (with the right endpoint (j) fixed) and add it into the complement
        # otherwise, increment the left pointer i while i<=j AND lesser than condition is not fulfilled
        # when we are outside of this loop, add the LESSER than subarrays in our complement count


        for j in range(len(nums)):
            if nums[j]==max_element:
                curr_count+=1
            total_subarrays+=(j+1)

            while i<=j and curr_count>=k:
                # reduce window size
                if nums[i]==max_element:
                    curr_count-=1
                i+=1
            
            complement_count+=j-i+1
        return total_subarrays-complement_count
                






