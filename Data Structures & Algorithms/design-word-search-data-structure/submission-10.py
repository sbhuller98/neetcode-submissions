class Node:
    def __init__(self, end = False):
        self.children = {}
        self.end = end
class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                curr.children[letter] = Node()
                curr = curr.children[letter]
        curr.end = True

    def search(self, word: str) -> bool:
        return self.searchInternal(word, self.root)

    def searchInternal(self, word: str, start) -> bool:
        if not word:
            return start.end
        if start is None:
            return False
        for i in range(len(word)):
            letter = word[i]
            if letter != ".":
                if letter not in start.children:
                    return False
                else:
                    start = start.children[letter]
            else:
                for lt in start.children.values():
                    if self.searchInternal(word[i + 1:], lt):
                        return True
                return False

        return start.end