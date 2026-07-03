class CountSquares:

    def __init__(self):
        self.points= Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x,y =point
        ans=0

        for (x1,y1), cnt in self.points.items():
            if abs(x1-x) != abs(y1-y) or x1==x or y1==y:
                continue
            ans += cnt* self.points[(x1,y)]* self.points[(x,y1)]
        
        return ans