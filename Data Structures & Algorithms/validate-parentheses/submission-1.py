class Solution:
    def isValid(self, s: str) -> bool:
        memory = []
        for character in s:
            if character in ["(", "{", "["]:
                memory.append(character)
            else:
                if len(memory) < 1:
                    return False
                match character:
                    case ")":
                        if memory.pop() != "(":
                            return False
                    case "}":
                        if memory.pop() != "{":
                            return False
                    case "]":
                        if memory.pop() != "[":
                            return False
        return len(memory) == 0