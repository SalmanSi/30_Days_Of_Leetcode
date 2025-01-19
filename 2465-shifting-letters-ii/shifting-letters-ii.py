class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        final_shifts=[0]*len(s)

        for shift in shifts:
            start=shift[0]
            end=shift[1]
            forward=shift[2]

            if forward:
                final_shifts[start]+=1
                if end !=len(final_shifts)-1:
                    final_shifts[end+1]-=1
            else:
                final_shifts[start]-=1
                if end !=len(final_shifts)-1:
                    final_shifts[end+1]+=1
                

        ans=list(s)

        curr_shift=0
        for i in range(len(s)):
            curr_shift+=final_shifts[i]
            curr_shift%=26

            ans[i]=chr(
                (ord(s[i])-ord('a')+curr_shift)%26+ord('a')
                
                )

            # ans[i]=chr(ord(ans[i])+(final_shifts[i]%26))
            # if ans[i]>'z':
            #     ans[i]=chr(ord(ans[i])-26)
            # elif ans[i]<'a':
            #     ans[i]=chr(ord(ans[i])+26)
        ans=''.join(ans)
        return ans
        # n = len(s)
        # diff_array = [
        #     0
        # ] * n  # Initialize a difference array with all elements set to 0

        # # Process each shift operation
        # for shift in shifts:
        #     if shift[2] == 1:  # If direction is forward (1)
        #         diff_array[shift[0]] += 1  # Increment at the start index
        #         if shift[1] + 1 < n:
        #             diff_array[
        #                 shift[1] + 1
        #             ] -= 1  # Decrement at the end+1 index
        #     else:  # If direction is backward (0)
        #         diff_array[shift[0]] -= 1  # Decrement at the start index
        #         if shift[1] + 1 < n:
        #             diff_array[
        #                 shift[1] + 1
        #             ] += 1  # Increment at the end+1 index

        # result = list(s)
        # number_of_shifts = 0

        # # Apply the shifts to the string
        # for i in range(n):
        #     number_of_shifts = (
        #         number_of_shifts + diff_array[i]
        #     ) % 26  # Update cumulative shifts, keeping within the alphabet range

        #     # Calculate the new character by shifting `s[i]`
        #     shifted_char = chr(
        #         (ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a")
        #     )
        #     result[i] = shifted_char

        # return "".join(result)
