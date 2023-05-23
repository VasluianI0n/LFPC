from enum import Enum

class TokenType(Enum):
    INTEGER = r'\d+'   # Regular expression for integer
    FLOAT = r'\d+\.\d+'   # Regular expression for float
    OPERATOR = r'[\+\-\*/]'   # Regular expression for operators (+, -, *, /)
    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'   # Regular expression for identifiers (e.g., variable names)
    SEMICOLON = r';'   # Regular expression for semicolon (;)
    # Add more token types as needed