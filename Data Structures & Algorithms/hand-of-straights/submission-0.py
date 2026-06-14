class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        while count:
            start = min(count)

            for card in range(start, start+groupSize):
                if card not in count:
                    return False;
                count[card] -= 1
                if count[card] == 0:
                    del count[card]
        
        return True
        