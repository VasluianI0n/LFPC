from ASTNode import ASTNode;
from TokenType import TokenType;

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        ast = self.parse_expression()
        return ast

    def parse_expression(self):
        ast = self.parse_term()
        while self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].token_type == TokenType.OPERATOR:
            operator = self.tokens[self.current_token_index]
            self.current_token_index += 1
            right_operand = self.parse_term()
            expression_node = ASTNode(operator.token_type, operator.value)
            expression_node.add_child(ast)
            expression_node.add_child(right_operand)
            ast = expression_node
        return ast

    def parse_term(self):
        if self.current_token_index < len(self.tokens):
            token = self.tokens[self.current_token_index]
            if token.token_type in (TokenType.INTEGER, TokenType.FLOAT, TokenType.IDENTIFIER):
                self.current_token_index += 1
                return ASTNode(token.token_type, token.value)
        raise SyntaxError('Unexpected token: {}'.format(self.tokens[self.current_token_index]))