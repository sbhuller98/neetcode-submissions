class Solution:
    def simplifyPath(self, path: str) -> str:
        splits = path.split('/')
        newVal = []
        for item in splits:
            if item == '..':
                if newVal:
                    newVal.pop()
            elif item != '' and item != '.':
                newVal.append(item)

        return '/' + ('/'.join(newVal))
                