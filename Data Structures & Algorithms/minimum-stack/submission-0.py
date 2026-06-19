class MinStack:

    def __init__(self):
        # store [element, index]
        # index = len(stack1) + len(stack2); 1 based index
        self.stackMin = []
        self.stackMax = []
        self.index = 0

    def push(self, value: int) -> None:
        lenStack1, lenStack2 = len(self.stackMin), len(self.stackMax)
        if lenStack1 == 0 and lenStack2 == 0:
            self.stackMin.append([value,0])
        else:
            if value > self.stackMin[-1][0]:
                self.stackMax.append([value, lenStack1 + lenStack2])
            else:
                self.stackMin.append([value, lenStack1 + lenStack2])
            

    def pop(self) -> None:
        lenStack1, lenStack2 = len(self.stackMin), len(self.stackMax)
        
        top1 = self.stackMin[-1][1] if lenStack1 > 0 else -1
        top2 = self.stackMax[-1][1] if lenStack2 > 0 else -1

        if top1 > top2:
            self.stackMin = self.stackMin[:-1]
        elif top1 < top2:
            self.stackMax = self.stackMax[:-1]
        
    def top(self) -> int:
        lenStack1, lenStack2 = len(self.stackMin), len(self.stackMax)
        
        top1 = self.stackMin[-1][1] if lenStack1 > 0 else -1
        top2 = self.stackMax[-1][1] if lenStack2 > 0 else -1

        if top1 > top2:
            return self.stackMin[-1][0]
        elif top1 < top2:
            return self.stackMax[-1][0]

    def getMin(self) -> int:
        return self.stackMin[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# -2 0 -3 -4 5 6 7 -5
# increasing value comes -> put in other stack
# decreasing value comes -> put in first stack
# stack1 = -2 -3 -4 -5 -> this way min remains here
# stack2 = 0 5 6 7 

# what about push pop top, how will we know what came last?
# store with index
# index is size of stack1 + stack2 + 1
# whichever stack has max index on top is the latest val