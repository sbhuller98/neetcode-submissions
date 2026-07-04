class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand = sorted(hand)

        taken = [0] * len(hand)
        total = 0

        while total < len(hand):
            currGroupSize = 0
            prev = None

            pTotal = total

            for i in range(len(hand)):
                if taken[i]:
                    continue
                if prev is None or prev + 1 == hand[i]:
                    prev = hand[i]
                    taken[i] = 1
                    currGroupSize += 1
                    total += 1
                if currGroupSize == groupSize:
                    break

            if pTotal == total:
                return False
        
        if currGroupSize == groupSize:
            return True
        return False
