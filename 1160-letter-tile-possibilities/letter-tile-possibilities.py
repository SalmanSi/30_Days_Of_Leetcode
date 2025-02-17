class Solution:

    def generateSequences(self,tiles,current,used,sequences):
        sequences.add(current)
        for i in range(len(tiles)):
            if not used[i]:
                used[i]=True
                self.generateSequences(tiles,current+tiles[i],used,sequences)
                used[i]=False
        return 


    def numTilePossibilities(self, tiles: str) -> int:
        sequences=set()

        used=[False]*len(tiles)
        self.generateSequences(tiles,"",used,sequences)
        return len(sequences)-1