import ast

import sympy as sp


def calculate(tree):
    """recebe a arvore construida pelo ast e retorna a expressão pelo symnpy"""
    # se for uma constante
    if isinstance(tree, ast.Constant):
        return sp.sympify(tree.value)

    # se for um nome (variãvel, simbolo)
    if isinstance(tree, ast.Name):
        return sp.Symbol(tree.id)

    # se for uma operação
    if isinstance(tree, ast.BinOp):
        left = calculate(tree.left)
        right = calculate(tree.right)

        match tree.op:
            case ast.Add():
                return left + right
            case ast.Sub():
                return left - right
            case ast.Mult():
                return left * right
            case ast.Div():
                return left / right
            case ast.Pow():
                return left**right
            case ast.Mod():
                return left % right

    # se for operação unitária
    if isinstance(tree, ast.UnaryOp):
        value = calculate(tree.operand)

        match tree.op:
            case ast.UAdd():
                return value
            case ast.USub():
                return -value

