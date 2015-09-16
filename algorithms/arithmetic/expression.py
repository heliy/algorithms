# coding: UTF-8


'''
Arithmetic expression evaluation.
Functionality is same as `eval()` 

def twoStack(): Dijkstra's two-stack algorithm 

'''

from .arithConstants import Fundametal4, Numbers, OperLevel

from .. import exampleAPI as api
StackClass = api.EXA_STACK

inNumbers = Numbers.append('.')           # chars which will appear in numbers

def check(expression, Stack=StackClass):
    '''
    Check expression is valid.

    always return True
    TODO: support brackets

    -------------------
    isValid = check(expressiong, Stack)
    input:
      expression: string.
      Stack: Stack calss, see algo.basic.stack.*Stack, simpleStack defualt.
    output:
      isValid: True for valid, or False otherwise.
    '''
    return True

def twoStack(expression, Stack=StackClass):
    '''
    Dijkstra's two-stack algorithm for evaluating expression.

    support operands: arithmetic number
    support operators: + - * / () 

    ---------------------
    val = twoStack(expression, Stack)
    input:
      expression: string.
      Stack: Stack calss, see algo.basic.stack.*Stack, simpleStack defualt.
    output:
      val: float result, or `None` if expression is unvalid
    '''
    if not check(expression, Stack):
        return None
    
    operands = Stack()
    operators = Stack()
    num = ''

    for s in expression:
        if s in Numbers:
            num += s                      # this char is one part of number
            continue
            
        if s == ' ':
            continue
        # an operator
        if num != '':
            # save the operand
            operands.push(float(num))
            num = ''
            
        if s in Fundametal4:
            if s == '-':
                if operators.isEmpty() or operators.top() == '(':   # minus sign
                    num = '-'
                    continue

            if OperLevel[s] == 1:
                while not operators.isEmpty():   # Level 2
                    t = operators.top()
                    if t in '()' or OperLevel[t] == 1:
                        break
                    v1 = operands.top()
                    operands.pop()
                    v2 = operands.top()
                    operands.pop()
                    if t == '*':
                        operands.push(v1*v2)
                    else:
                        oprands.push(v2/v1)
                    operators.pop()
            operators.push(s)
            
        elif s == '(':
            operators.push('(')
        elif s == ')':
            while operators.top() != '(':   # Level 2
                t = operators.top()
                v1 = operands.top()
                operands.pop()
                v2 = operands.top()
                operands.pop()
                if t == '*':
                    operands.push(v1*v2)
                elif t == '+':
                    operands.push(v1+v2)
                elif t == '-':
                    operands.push(v2-v1)
                else:
                    operands.push(v2/v1)
                operators.pop()
            operators.pop()

    if num != '':
        operands.push(float(num))
    while not operators.isEmpty():
        t = operators.top()
        v1 = operands.top()
        operands.pop()
        v2 = operands.top()
        operands.pop()
        if t == '*':
            operands.push(v1*v2)
        elif t == '+':
            operands.push(v1+v2)
        elif t == '-':
            operands.push(v2-v1)
        else:
            operands.push(v2/v1)
        operators.pop()
        
    return operands.top()
                    
                
                
