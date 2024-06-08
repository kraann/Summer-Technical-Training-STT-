class solution:
    def laststone(self,stones: list[int]) -> int:
        while len(stones) > 1 and max(stones) !=0:
            stones.sort()
            chk = abs(stones.pop() - stones.pop())
            stones.append(chk)
        return stones[0]