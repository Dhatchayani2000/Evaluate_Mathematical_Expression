# Evaluate_Mathematical_Expression
# Mathematical Expression Evaluator

## Table of Contents
- [Introduction](#introduction)
- [Function Signature](#function-signature)
- [Description](#description)
- [Supported Operations](#supported-operations)
- [Input Validation](#input-validation)
- [Example Usage](#example-usage)

## Introduction

This Python module provides a function for evaluating mathematical expressions with support for basic arithmetic operations and parentheses. It can handle expressions with parentheses, ensuring that the order of operations is followed correctly.

## Function Signature

```python
def evaluate_expression(expression: str) -> float:
    """
    Evaluate a mathematical expression represented as a string with support for +, -, *, /, (, and ).

    Args:
    expression (str): A mathematical expression to be evaluated.

    Returns:
    float: The result of the evaluated expression.

    Raises:
    ValueError: If there is an issue with the input expression, such as invalid characters or division by zero.

    Usage:
    expression = "(4-4)-(56)/34-((9.6-0)*33)*0"
    try:
        result = evaluate_expression(expression)
        print(result)
    except ValueError as e:
        print(e)
    ```
