import ast

import sympy as sp


def interpret(tree: ast.AST) -> sp.Expr:
    """recebe a arvore construida pelo ast e retorna a expressão pelo symnpy"""
    # se for uma constante
    if isinstance(tree, ast.Constant):
        val = sp.sympify(tree.value)
        assert isinstance(val, sp.Expr)
        return val

    # se for um nome (variãvel, simbolo)
    if isinstance(tree, ast.Name):
        return sp.Symbol(tree.id)

    # se for uma operação
    if isinstance(tree, ast.BinOp):
        left = interpret(tree.left)
        right = interpret(tree.right)

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
        value = interpret(tree.operand)

        match tree.op:
            case ast.UAdd():
                return value
            case ast.USub():
                return -value

    # operação inválida / desconhecida
    raise ValueError()


def parse_expression(query: str):
    """
    recebe a query bruta e envia ela pro parser, retorna um dicionário
    com um erro ou com a expressão resolvida
    """
    try:
        tree: ast.AST = ast.parse(query, mode="eval").body
        res: dict[str, str | bool] = {
            "resultado": str(interpret(tree)),
            "sucesso": True,
        }
        # divisão por zero manual
        if res["resultado"] == "nan":
            raise ZeroDivisionError
        return res
        # expressão com xintaxe inválida
    except SyntaxError:
        return {"resultado": "Syntax Error", "sucesso": False}
        # divisão por zero
    except ZeroDivisionError:
        return {"resultado": "Division by zero", "sucesso": False}
        # expressão nao permitida {ainda bb}
    except ValueError:
        return {"resultado": "Invalid expression", "sucesso": False}
