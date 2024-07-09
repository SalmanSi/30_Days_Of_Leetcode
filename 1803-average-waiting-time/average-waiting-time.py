class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait_time=customers[0][1]
        previous_end_time=customers[0][0]+total_wait_time
        # print(f"total wait time={total_wait_time}")
        # print(f"prev_end_time={previous_end_time}")
        for customer in customers[1:]:
            arrival_time=customer[0]
            cook_time=customer[1]
            
            if arrival_time<previous_end_time:
                total_wait_time+=(previous_end_time - arrival_time)
                previous_end_time+=cook_time
            else:
                previous_end_time=arrival_time+cook_time
            total_wait_time+=cook_time


        total_wait_time=total_wait_time/len(customers)
        return total_wait_time