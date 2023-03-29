# Laboratory Work Nr.3 Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Vasluian ION

****
## Objectives
1. Understand what lexical analysis is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.
****
## Implementation
The code is divided into two files: tokenr.py and lexer.py. The tokenr.py file defines a Tokens class that contains a dictionary of all the different
types of tokens that the lexer can recognize. It also includes a lookup_ident() method that checks whether a given identifier is a keyword
or a user-defined identifier.

The tokenr.py module defines two classes: Token and Tokens.
The Token class defines an object that holds the type and value of a token. The constructor takes two arguments: Type and Value.
```class Token:
    def __init__(self, Type, Value):
        self.Type = Type
        self.Value = Value
 ```
The Type argument is the type of the token (e.g. 'IDENT', 'INT', 'PLUS', etc.), and the Value argument is the actual value of the token 
(e.g. the identifier name, the integer value, etc.).
The Tokens class defines a collection of token types and keywords used in the language. It defines two dictionaries: tokens and keywords. The tokens dictionary
maps the token types to their corresponding string representations (e.g. 'PLUS' maps to '+', 'IDENT' maps to 'IDENT', etc.). The keywords dictionary maps the
reserved words of the language to their corresponding token types (e.g. 'let' maps to 'LET', 'if' maps to 'IF', etc.).
```class Tokens:
    def __init__(self):
        self.tokens = {
            # {{ Main Tokens }}
            'ILLEGAL': 'ILLEGAL',
            'EOF'    : 'EOF',

            # {{ Ident and Values }}
            'IDENT'  : 'IDENT',
            'INT'    : 'INT',
            'DOUBLE' : 'DOUBLE',
            'STRING' : 'STRING',
            'CHAR'   : 'CHAR',

            # {{ Operators }}
            'ASSIGN'   : 'ASSIGN',
            'PLUS'     : 'PLUS',
            'MINUS'    : 'MINUS',
            'MULTIPLY' : 'MULTIPLY',
            'DIVIDE'   : 'DIVIDE',
            'LT'       : 'LT',
            'GT'       : 'GT',

            # {{ Delimiters }}
            'SEMICOLON' : 'SEMICOLON',
            'COMMA'     : 'COMMA',
            'LPAREN'    : 'LPAREN',
            'RPAREN'    : 'RPAREN',
            'LBRACE'    : 'LBRACE',
            'RBRACE'    : 'RBRACE',

            # {{ Boolean Operators }}
            'EQ'     : 'EQ',
            'NOT'    : 'NOT',
            'NOT_EQ' : 'NOT_EQ',
            'AND'    : 'AND',
            'OR'     : 'OR',
        }

        self.keywords = {
            'fn'    : 'FUNCTION',
            'let'   : 'LET',
            'true'  : 'TRUE',
            'false' : 'FALSE',
            'if'    : 'IF',
            'else'  : 'ELSE',
            'for'   : 'FOR',
            'while' : 'WHILE',
            'return': 'RETURN',
            'int'   : 'INT',
            'double': 'DOUBLE',
            'string': 'STRING',
            'char'  : 'CHAR',
        }
  ```
The lookup_ident method of the Tokens class takes an identifier name as an argument and returns its corresponding token type if it is a keyword, otherwise it
returns 'IDENT'.
```
def lookup_ident(self, ident):
        if ident in self.keywords:
            return self.keywords[ident]
        return 'IDENT'
```
The lexer.py file contains the implementation of a lexer, which is a program that reads input text and identifies the tokens (individual units of meaning)
in the text. The lexer implemented in this file uses regular expressions to define the patterns that correspond to each token. The file starts with several
import statements, including the re module for regular expressions and the Enum class from the enum module. The Token class is defined as an enumeration, where
each token is represented by a unique identifier (e.g., Token.NUMBER for numeric literals). The Lexer class is defined next, which takes a string of input text 
as its argument. The class has several methods, including lex() which performs the tokenization by iterating over the input string and applying regular expressions
to match the appropriate patterns for each token. The lex() method returns a list of tokens.The regular expressions for each token type are defined in the Lexer
class using the re.compile() function. For example, the regular expression for a numeric literal is defined as r'\d+(\.\d*)?', which matches one or more digits,
optionally followed by a decimal point and more digits.
The Lexer class also includes a dictionary mapping the regular expressions to the corresponding token types. This dictionary is used by the lex()
method to match each pattern to its corresponding token type.

And we have one more class that is the main class, which unites the other two classes in one, and reads from a file called ```script.txt``` everything in it and gives
back the lexer

```
from lexer import Lexer

def scan_file(file):
    f = open(file)

    my_lexer = Lexer(f.read())
    tokens = my_lexer.get_tokens()
    for tok in tokens:
        print(tok)

if __name__ == '__main__':
    scan_file('script.txt')
```

****
## Conclusion/Results

Conclusion:
In conclusion, lexers are essential components of compilers and interpreters as they break down the input code into smaller units known as tokens, which can be easily
processed by the compiler or interpreter. They make it easier to analyze the structure of the code, identify syntax errors, and perform various operations on the code.
Furthermore, lexers are also used in various text processing applications such as search engines, code editors, and syntax highlighters to recognize patterns in the
input text and extract relevant information from it. They are efficient and versatile tools that help in the development of robust and efficient software systems.

Results:

  script.txt file:
  ```
  let x = 5;
  let y = 10;
  let result = x + y;

  if (result > 10) {
      print("Reached");
  } else {
      print("Result is less than or equal to 10");
  }

  for (let i = 0; i < 5; i = i + 1) {
      print(i);
  }

  let greeting = "Hello, world!";
  print(greeting);
  ```
OUTPUT:
  ```
('LET', 'let')
('IDENT', 'x')
('ASSIGN', '=')
('INT', '5')
('SEMICOLON', ';')
('LET', 'let')
('IDENT', 'y')
('ASSIGN', '=')
('INT', '10')
('SEMICOLON', ';')
('LET', 'let')
('IDENT', 'result')
('ASSIGN', '=')
('IDENT', 'x')
('PLUS', '+')
('IDENT', 'y')
('SEMICOLON', ';')
('IF', 'if')
('LPAREN', '(')
('IDENT', 'result')
('GT', '>')
('INT', '10')
('RPAREN', ')')
('LBRACE', '{')
('IDENT', 'print')
('LPAREN', '(')
('STRING', 'Reached')
('RPAREN', ')')
('SEMICOLON', ';')
('RBRACE', '}')
('ELSE', 'else')
('LBRACE', '{')
('IDENT', 'print')
('LPAREN', '(')
('STRING', 'Result')
('IDENT', 'is')
('IDENT', 'less')
('IDENT', 'than')
('IDENT', 'or')
('IDENT', 'equal')
('IDENT', 'to')
('INT', '10')
('STRING', '')
('SEMICOLON', ';')
('RBRACE', '}')
('FOR', 'for')
('LPAREN', '(')
('LET', 'let')
('IDENT', 'i')
('ASSIGN', '=')
('INT', '0')
('SEMICOLON', ';')
('IDENT', 'i')
('LT', '<')
('INT', '5')
('SEMICOLON', ';')
('IDENT', 'i')
('ASSIGN', '=')
('IDENT', 'i')
('PLUS', '+')
('INT', '1')
('RPAREN', ')')
('LBRACE', '{')
('IDENT', 'print')
('LPAREN', '(')
('IDENT', 'i')
('RPAREN', ')')
('SEMICOLON', ';')
('RBRACE', '}')
('LET', 'let')
('IDENT', 'greeting')
('ASSIGN', '=')
('STRING', 'Hello')
('IDENT', 'world')
('NOT', '!')
('STRING', '')
('IDENT', 'print')
('LPAREN', '(')
('IDENT', 'greeting')
('RPAREN', ')')
('SEMICOLON', ';')
('EOF', '')
  ```
****
## References
1. https://www.youtube.com/watch?v=qF2O1pOxpv8
2. https://www.youtube.com/watch?v=HuVg1trQC64
3. https://replit.com/talk/learn/Make-a-Full-Lexer-in-Python/111397
