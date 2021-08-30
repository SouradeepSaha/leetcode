class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.occupied = []

    def seat(self) -> int:
        if len(self.occupied) == 0:
            self.occupied.append(0)
            return 0
        else:
            max_int = -999
            left_end, right_end = 0, 0
            if self.occupied[0] > max_int:
                max_int = self.occupied[0]
                left_end = -1
                right_end = self.occupied[0]

            for i in range(1, len(self.occupied)):
                cur_int = int((self.occupied[i] + self.occupied[i-1])/2) - self.occupied[i-1]
                if cur_int > max_int:
                    max_int = cur_int
                    left_end = self.occupied[i-1]
                    right_end = self.occupied[i]

            if self.n-1 - self.occupied[-1] > max_int:
                max_int = self.n-1 - self.occupied[-1]
                left_end = self.occupied[-1]
                right_end = self.n

            if left_end == -1:
                self.occupied.insert(0, 0)
                return 0

            elif right_end == self.n:
                self.occupied.append(self.n-1)
                return self.n-1

            else:
                #print(f"H {int(right_end + left_end)/2}")
                self.occupied.insert(self.occupied.index(left_end)+1, int((right_end + left_end)/2))
                #print(self.occupied)
                return int((right_end + left_end)/2)


    def leave(self, p: int) -> None:
        self.occupied.remove(p)
        #print(self.occupied)



# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(10)
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
obj.leave(4)
print(obj.seat())

