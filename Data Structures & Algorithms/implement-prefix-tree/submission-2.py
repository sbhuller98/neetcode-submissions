from typing import Optional

class Node:
    def __init__(self, letter, end = False):
        self.letter = letter
        self.items = dict()
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.items:
                curr = curr.items[word[i]]
            else:
                newN = Node(word[i])
                curr.items[word[i]] = newN
                curr = newN
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
        
        