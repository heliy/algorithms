# coding: UTF-8


'''
Arithmetic expression evaluation.
Functionality is same as `eval()` 

def twoStack(): Dijkstra's two-stack algorithm 

'''

Fundametal4 = ['+', '-', '*', '/']

Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

def twoStack(Stack, expression):
    '''
    Dijkstra's two-stack algorithm for evaluating expression.

    support operands: arithmetic number
    support operators: + - * / () 

    ---------------------
    val = twoStack(Stack, expression)
    input:
      Stack: Stack calss, see algo.basic.stack.*Stack
      expression: string
    output:
      val: float result, or `None` if expression is unvalid
    '''
    operands = Stack()
    operators = Stack()
    val = 0
    num = ''

    for s in expression:
        if s in Numbers:
            num += s
            continue
        else:
            operands.push(float(num))
            
        if s == ' ':
            continue
        elif s in Fundametal4:
            
            v = operanda.pop()
            if not v:
                
