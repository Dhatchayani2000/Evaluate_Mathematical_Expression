def evaluate_expression(expression):
    def precedence(operator):
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/'):
            return 2
        return 0

    def apply_operator(operators, values, operator):
        while (operators and operators[-1] in '+-*/' and
               precedence(operators[-1]) >= precedence(operator)):
            right = values.pop()
            left = values.pop()
            op = operators.pop()
            if op == '+':
                values.append(left + right)
            elif op == '-':
                values.append(left - right)
            elif op == '*':
                values.append(left * right)
            elif op == '/':
                if right == 0:
                    raise ValueError("Division by zero is not allowed.")
                values.append(left / right)

    expression = expression.replace(" ", "")
    i = 0
    values = []
    operators = []
    paren_count = 0  # To track unmatched parentheses

    while i < len(expression):
        if expression[i] in '0123456789':
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            values.append(float(expression[i:j]))
            i = j
        elif expression[i] in '+-*/':
            while (operators and operators[-1] in '+-*/' and
                   precedence(operators[-1]) >= precedence(expression[i])):
                apply_operator(operators, values, expression[i])
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
            paren_count += 1
        elif expression[i] == ')':
            if paren_count <= 0:
                raise ValueError("Mismatched closing parenthesis in the expression.")
            while operators[-1] != '(':
                apply_operator(operators, values, operators[-1])
            operators.pop()  # Remove the opening parenthesis
            i += 1
            paren_count -= 1
        else:
            raise ValueError("Invalid character in the expression: " + expression[i])

    if paren_count > 0:
        raise ValueError("Mismatched opening parenthesis in the expression.")

    while operators:
        apply_operator(operators, values, operators[-1])

    return values[0]

# Example usage:
expression = "(4-4)-(56)/34-((9.6-0)*33)*0"
try:
    result = evaluate_expression(expression)
    print(result)
except ValueError as e:
    print(e)
