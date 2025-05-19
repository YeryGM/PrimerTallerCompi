from A_Lexico import tokenize
from A_Sintactico.Parser import Parser
from A_Sintactico.AST import print_ast
import A_Semantico
from Codigo_Intermedio import TACGenerator, print_tac

def main():
    # HERE GOES THE EXAMPLE INPUT
    code = "a = 3 + b;"
    print("Source code:", code)

    # Lexical analysis
    tokens = list(tokenize(code))
    print("Tokens:", tokens)

    # Syntactic analysis (parsing)
    parser = Parser(tokens)
    ast = parser.parse()
    print("AST:")
    print_ast(ast)  # Use the pretty printer

    # Semantic analysis
    try:
        A_Semantico.validate_semantics(ast)
        print("Semantic analysis: OK")
    except Exception as e:
        print("Semantic error:", e)
        return

    # Intermediate code generation (TAC)
    tacgen = TACGenerator()
    tacgen.generate(ast)
    tac = tacgen.get_tac()
    print("Three-Address Code:")
    print_tac(tac)

if __name__ == "__main__":
    main()
