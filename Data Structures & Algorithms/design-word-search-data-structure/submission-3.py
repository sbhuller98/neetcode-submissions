class Node:
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.terminal = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        currNode = self.root
        for letter in word:
            if letter not in currNode.children:
                currNode.children[letter] = Node(letter)
            currNode = currNode.children[letter]
        currNode.terminal = True

    def search(self, word: str) -> bool:
        return self.searchInternal(word)

    def searchInternal(self, word: str, currNode: Node = None) -> bool:
        if not currNode:
            currNode = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter == ".":
                for child in currNode.children.values():
                    if self.searchInternal(word[i + 1:], child):
                        return True
                return False
            elif letter not in currNode.children:
                return False
            currNode = currNode.children[letter]
        if currNode.terminal:
            print(currNode.terminal)
            print(word)
            print("here")
            return True
        return False
