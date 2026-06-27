class Solution:
    def calPoints(self, operations: List[str]) -> int:
        register = []

        for oper in operations:
            match oper:
                case "C":
                    register.pop()
                case "D":
                    register.append(register[-1] * 2)
                case "+":
                     register.append(register[-1] + register[-2])
                case _:
                    register.append(int(oper))
        
        return sum(register)