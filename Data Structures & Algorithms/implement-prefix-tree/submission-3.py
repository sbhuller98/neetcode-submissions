from typing import Optional

class Node:
    def __init__(self, end = False):
        self.items = dict()
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.items:
                curr.items[word[i]] = Node()
            curr = curr.items[word[i]]
        curr.end = True


    def search(self, word: str) -> bool:
        val = self._search(word)
        if val is not None and val.end is True:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        if self._search(prefix) is not None:
            return True
        return False

    def _search(self, word) -> Optional[Node]:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.items:
                return None
            curr = curr.items[word[i]]
        return curr
        
        