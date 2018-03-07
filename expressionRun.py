from mainAbstractData import baseAbstractData as baseColl
valueStack = baseColl.Stack()
operandStack = baseColl.Stack()
expression = input()
while expression != "exit":
    if expression != "exit":
        expList = expression.split(" ")
        for element in expList:
            if element == "(":
                pass
            elif element == "*":
                operandStack.push(element)
            elif element == "+":
                operandStack.push(element)
            elif element == "/":
                operandStack.push(element)
            elif element == "-":
                operandStack.push(element)
            elif element == "sqrt":
                operandStack.push(element)
            elif element == ")":
                value = valueStack.pop()
                operand = operandStack.pop()
                if operand == "+":
                    value = float(valueStack.pop()) + value
                if operand == "-" :
                    value = float(valueStack.pop()) - value
                if operand == "*" :
                    value = float(valueStack.pop()) * value
                if operand == "/" :
                    value = float(valueStack.pop()) / value
                if operand == "sqrt":
                    value = value**(0.5)
                valueStack.push(value)
            else:
                valueStack.push(float(element))
    print("Вы ввели с клавиатуры ", expression)
    print(valueStack)
    print(operandStack)
    expression = input()