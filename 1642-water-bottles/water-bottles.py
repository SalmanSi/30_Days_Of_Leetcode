class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty=0
        drunk=0
        full_bottles=numBottles

        while full_bottles>0:
            drunk+=full_bottles
            empty+=full_bottles
            full_bottles=empty//numExchange
            empty%=numExchange
        return drunk