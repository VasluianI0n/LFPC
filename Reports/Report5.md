# Laboratory Work Nr.4 Chomsky Normal Form
## Course: Formal Languages & Finite Automata
## Author: Vasluian ION

****
## Objectives
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
    i.In case you didn't have a type that denotes the possible types of tokens you need to:
      a.Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens.
      b.Please use regular expressions to identify the type of the token.
    ii.Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    iii.Implement a simple parser program that could extract the syntactic information from the input text.
****
## Implementation

Task 1: Defining TokenType using enum-like structure in Python:

```
from enum import Enum

class TokenType(Enum):
    INTEGER = r'\d+'   # Regular expression for integer
    FLOAT = r'\d+\.\d+'   # Regular expression for float
    OPERATOR = r'[\+\-\*/]'   # Regular expression for operators (+, -, *, /)
    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'   # Regular expression for identifiers (e.g., variable names)
    SEMICOLON = r';'   # Regular expression for semicolon (;)
    # Add more token types as needed
    
```

The TokenType enum is created using the enum module in Python.
Each token type is defined as a member of the enum, along with its corresponding regular expression pattern.
Token types are used to categorize different types of tokens in lexical analysis.

Task 2: Implementing necessary data structures for an Abstract Syntax Tree (AST):

```
class ASTNode:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
```


The ASTNode class represents a node in the Abstract Syntax Tree.
Each ASTNode has a token_type attribute representing the type of the token associated with the node.
The value attribute stores the value of the token.
The children attribute is a list that holds the child nodes of the current node.
The add_child() method is used to add child nodes to the current node.

Task 3: Implementing a simple parser to extract syntactic information from input text:

```
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
```

The Parser class is responsible for parsing the input text.
The parse() method initiates the parsing process and returns the root node of the AST.
The parse_expression() method is used to parse an expression in the input text.
It first calls parse_term() to parse the left-hand side of the expression.
It then checks if the next token is an operator.
If an operator is found, it creates an expression_node and adds the parsed term as the left child.
It then calls parse_term() again to parse the right-hand side of the expression and adds it as the right child.
The method continues this process as long as there are more operators in the input.
The parse_term() method is responsible for parsing a term in the input text.
It checks if the current token is a valid term (integer, float, or identifier) and returns an ASTNode with the corresponding token type and value.
If the current token is not a valid term, it raises a SyntaxError.
Overall, the code defines the necessary data structures (TokenType and ASTNode) and implements a simple parser that uses these structures to build an Abstract Syntax Tree (AST) based on the input text's syntax.



****
## Conclusion/Results

```
input_text = "2 + 3 * 4;"
tokens = lexer(input_text)
parser = Parser(tokens)
ast = parser.parse()
```

AST Visualization:

```
      +
     / \
    2   *
       / \
      3   4
```

****


