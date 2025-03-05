import sys
from antlr4 import *
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from EvalVisitor import EvalVisitor  # Asegúrate de tener esta clase implementada

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    input_stream = FileStream(input_file, encoding="utf-8") if input_file else StdinStream()
    
    lexer = LabeledExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = LabeledExprParser(tokens)
    tree = parser.prog()  # parse

    eval_visitor = EvalVisitor()
    eval_visitor.visit(tree)

if __name__ == "__main__":
    main()
