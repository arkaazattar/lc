# Last updated: 5/23/2026, 2:33:38 PM
class MinStack:

    def __init__(self):
        self._elems = []
        self._min_stack = []

    def push(self, val: int) -> None:
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)
        self._elems.append(val)

    def pop(self) -> None:
        if self._elems[-1] == self._min_stack[-1]:
            self._min_stack.pop()
        self._elems.pop()

    def top(self) -> int:
        if self._elems:
            return self._elems[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()