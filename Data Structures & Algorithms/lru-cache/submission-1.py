class ListNode():
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.val = value
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mpp = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.nxt
        prevNode.nxt = nextNode
        nextNode.prev = prevNode

    def addNode(self, node):
        prevNode = self.tail.prev
        prevNode.nxt = node
        node.prev = prevNode
        node.nxt = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.mpp:
            currNode = self.mpp[key]
            self.removeNode(currNode)
            self.addNode(currNode)
            return currNode.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            self.removeNode(self.mpp[key])
            del self.mpp[key]
            self.mpp[key] = ListNode(key,value)
            self.addNode(self.mpp[key])
        else:
            self.mpp[key] = ListNode(key,value)
            # print(self.mpp[key])
            self.addNode(self.mpp[key])
            if len(self.mpp) > self.cap:
                del self.mpp[self.head.nxt.key]
                self.removeNode(self.head.nxt)
                
        
