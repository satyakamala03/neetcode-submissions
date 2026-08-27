class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
    def lcp(self, word, prefixLen):
        node = self.root
        for i in range(min(len(word), prefixLen)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        return min(len(word), prefixLen)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        trie = Trie()
        mini = 0

        for i in range(1, len(strs)):
            if len(strs[mini]) > len(strs[i]):
                mini = i
        
        trie.insert(strs[mini])
        prefixLen = len(strs[mini])

        for s in strs:
            prefixLen = trie.lcp(s, prefixLen)
        
        return strs[0][:prefixLen]


        


        