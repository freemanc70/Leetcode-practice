class solution(object):
    '''
    type f: str
    rtype: int
    '''
    def calculate(self, f):
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(f))):
            
            if f[i].isdigit():
                operand += f[i]
                if i == 0 or not f[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif f[i] == ')' or f[i] == '*' or f[i] == '/':
                operators.append(f[i])
            
            elif f[i] == '+' or f[i] == '-':
                while operators and (operators[-1] == '*' or operators[-1] == '/'):
                     self.compute(operands, operators)
                
                operators.append(f[i])
            
            elif f[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                
                operators.pop()
                
        while operators:
            self.compute(operands, operators)
            
        return operands[-1]
    
    
    def compute(self, operands, operators):
        
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)
        elif op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)



if __name__ == "__main__":
    
    result = solution().calculate("(5+(3*2)-7)*8")
    print result
