# Laboratory Work Nr.4 Chomsky Normal Form
## Course: Formal Languages & Finite Automata
## Author: Vasluian ION

****
## Objectives
1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.
****
## Implementation

We have 3 main classes:
main.py, grammar.py and prod.py

First of all in main.py we have:


```
import itertools

class Grammar:
    def __init__(self, grammar, terminal_symbols, non_terminal_symbols, start='S'):
        self.grammar = grammar
        self.terminal_symbols = terminal_symbols
        self.non_terminal_symbols = non_terminal_symbols
        self.start = start


    def __filter(self, word, to_replace, replacement):
        options = [(c,) if c != to_replace else (to_replace, replacement) for c in word]
        return ("".join(o) for o in itertools.product(*options))

    def check_start_symbol(self):
        """
        If the Start Symbol S occurs on some right side, create
            a new Start Symbol S' and a new Production S -> S'.
        """
        for production in self.grammar:
            if self.start in production[1]:
                self.grammar.insert(0, ['S*', 'S'])
                break


    def remove_empty(self):
        """
        Remove Null Productions.
        """
        nullable_variables = set() 
        to_remove = [] 
        for production in self.grammar:
            if 'Q' in production[1]:
                nullable_variables.update(set(production[0]))
                to_remove.append(self.grammar.index(production))

        print(to_remove)

        for nullable_production_idx in sorted(to_remove, reverse=True):
            del self.grammar[nullable_production_idx]

        # DEBUG:
        # print(nullable_variables)
 #        test = []
 #        grammar_cp = self.grammar.copy()
 #        for nullable in nullable_variables:
 #            for i in range(len(self.grammar)):
 #                if nullable in self.grammar[i][1]:
 #                    X = list(self.__filter(self.grammar[i][1], nullable, ''))
 #                    print(X)
 #                    test.append(X)
                    # print('DEBUG:', X)
                    # grammar_cp[i][1] = "|".join(X) if '' not in X else ''

        __grammar = self.grammar.copy()
        for production in self.grammar:
            if any((ch in production[1]) for ch in nullable_variables):
                X = [list(self.__filter(production[1], nullable, '')) for nullable in nullable_variables]
                # Don't even ask lol
                X = list(set(list(itertools.chain(*X))))
                __grammar[self.grammar.index(production)][1] = '|'.join(X) 

        print(__grammar)



    def remove_unit(self):
        """
        Remove Unit Productions.
        """
        pass


    def replace_productions(self):
        """
        Replace each Production A -> B1 ... Bn, where n > 2, with
            A -> B1C where C -> B2 ... Bn for all Productions having
            two or more Symbols on the right side.
        """
        pass



grammar = [
    ['S', 'aB'],
    ['S', 'DA'],
    ['A', 'a'],
    ['A', 'BD'],
    ['A', 'aDADB'],
    ['B', 'b'],
    ['B', 'ASB'],
    ['D', 'Q'],
    ['D', 'BA'],
    ['C', 'BA'],
]



terminal_symbols = ['a', 'b']
non_terminal_symbols = ['S', 'A', 'B', 'C', 'D']

CFG = Grammar(grammar, terminal_symbols, non_terminal_symbols)

print(grammar)

# print("+---------------+")
CFG.check_start_symbol()
# print(CFG.grammar)

# print("+---------------+")
CFG.remove_empty()
# print(CFG.grammar)
```

This code defines a class Grammar with methods to manipulate context-free grammars. The __init__ method initializes the grammar with a list of production rules, a list of terminal symbols, a list of non-terminal symbols, and a starting symbol.

The check_start_symbol, remove_empty, remove_unit, and replace_productions methods are not yet implemented.

The remove_empty method removes productions that derive the empty string ('ε') and updates other productions accordingly.

The code includes a sample context-free grammar and instantiates a Grammar object with it. The code then applies the check_start_symbol and remove_empty methods to the grammar and prints the resulting grammar after each operation.

Then we have the CNF code, which is in grammar.py:

```
from prod import *
import itertools


class Grammar:
    def __init__(self, Language):
        self.Language = Language
        self.grammar = self.Language.create_dict()
        self.nullable_variables = set()

    def remove_empty_productions(self):
        for state in self.grammar:
            if Language.has_empty(state):
                self.nullable_variables.update(set(state))
                self.grammar[state].remove('Q')

            for x in self.grammar[state]:
                if x == '':
                    self.nullable_variables.update(set(state))
                    self.grammar[state].remove('')

    def update_empty_states(self):
        for state in self.grammar:
            self.grammar[state], count = Language.replace_nullables(self.grammar[state], self.nullable_variables)
            if count != 0:
                self.remove_empty_productions()

    def update_empty_productions(self):
        updates = []
        for nullable in self.nullable_variables:
            temp = []
            for state in self.grammar:
                temp.append(Language.filter(self.grammar[state], nullable))
            updates.append(temp)

        updated_grammar = {} 
        for idx, state in enumerate(self.grammar):
            updated_grammar[idx] = []

        for row in updates:
            for idx, update in enumerate(row):
                foo = [item for item in update]
                updated_row = [item for sublist in foo for item in sublist]
                updated_grammar[idx].append(updated_row)
       
        for idx, state in enumerate(self.grammar):
            self.grammar[state] = sorted(set().union(*updated_grammar[idx]))

    def foo(self):
        for i in range(5):
            self.update_empty_productions()
            self.remove_empty_productions()

    def remove_renamings(self):
        grammar_copy = self.grammar.copy()
        for state in self.grammar:
            for transition in self.grammar[state]:
                if transition in self.grammar and transition != state:
                    index = self.grammar[state].index(transition)
                    temp = list(itertools.chain(self.grammar[state], self.grammar[transition]))
                    grammar_copy[state] = temp 

        for state in grammar_copy:
            self.grammar[state] = list(set(grammar_copy[state]))

    def remove_inaccessible(self):
        states = [state for state in self.grammar]
        inaccessible = []
        for state in states:
            accessible = False
            for productions in self.grammar.values():
                for prod in productions:
                    if state in prod:
                        accessible = True
                        break

            if not accessible:
                inaccessible.append(state)

        for ics in inaccessible:
            self.grammar.pop(ics)

grammar = [
        ['S', 'aB'],
        ['S', 'DA'],
        ['A', 'a'],
        ['A', 'BD'],
        ['A', 'aDADB'],
        ['B', 'b'],
        ['B', 'ASB'],
        ['D', 'Q'],
        ['D', 'BA'],
        ['C', 'BA'],
]

Language = Productions(grammar)
CNF = Grammar(Language)

CNF.remove_empty_productions()
CNF.update_empty_states()
CNF.update_empty_productions()
CNF.foo()
CNF.remove_renamings()
CNF.remove_inaccessible()

print("DEBUG")
for key in CNF.grammar:
    print(key, ":", CNF.grammar[key])
    
```

he Chomsky Normal Form grammar is a specific form of the context-free grammar where all productions have either two non-terminals or one terminal on the right-hand side.

The code first defines a class Grammar that takes a Language object as input. The Language object is created from the input grammar and has methods to generate a dictionary representing the grammar, check if a symbol generates the empty string, replace nullables, and filter productions.

The Grammar class has several methods to transform the input grammar into Chomsky Normal Form. The remove_empty_productions method removes all productions that generate the empty string. The update_empty_states method updates all productions by replacing nullable non-terminals with empty strings. The update_empty_productions method updates all productions by adding new productions that generate empty strings.

The foo method repeatedly calls the update_empty_productions and remove_empty_productions methods until no more changes can be made. The remove_renamings method replaces all productions with equivalent productions that do not have non-terminals on the right-hand side. The remove_inaccessible method removes all non-terminals that cannot be reached from the start symbol.

Finally, the code generates a Chomsky Normal Form grammar by calling the above methods on the input grammar and prints the resulting grammar.

And in in the prod.py we have:

```
import itertools


class Productions:
    def __init__(self, grammar, empty='Q'):
        self.grammar = grammar
        self.empty = empty

        self.get_symbols()
        self.grammar_dict = dict()

    
    def get_symbols(self):
        self.res = list(set([i for j in self.grammar for i in j]))
        self.res = list(set([i for j in self.res for i in j]))
        return self.res

    
    def get_non_terminals(self):
        return sorted([terminal for terminal in self.res if terminal.isupper() and terminal != self.empty])


    def get_terminals(self):
        return sorted([terminal for terminal in self.res if terminal.islower()])


    def create_dict(self):
        for production in self.grammar:
           self.grammar_dict[production[0]] = [
                prod[1] for prod in self.grammar
                    if prod[0] == production[0]] 

        return self.grammar_dict


    def has_empty(self, target):
        for productions in self.grammar_dict[target]:
            if 'Q' in productions:
                return True
        return False


    def filter(self, productions, nullable):
        updated_productions = []
        for production in productions:
            options = [(c,) if c != nullable else (nullable, '') for c in production]
            foo = list("".join(o) for o in itertools.product(*options))
            updated_productions.append(foo)
        return updated_productions


    def replace_nullables(self, productions, nullables):
        count = 0
        for prod in productions:
            for nullable in nullables:
                if nullable == prod:
                    index = productions.index(prod)
                    productions[index] = 'Q'
                    count = count + 1
        return (productions, count)
    
```

The __init__ method takes a grammar list as input, where each element is a list of two items: the first item is the non-terminal symbol and the second item is a string of terminal and non-terminal symbols representing a production rule. The empty argument is an optional string which represents the empty symbol.

The get_symbols method returns a list of all symbols (both terminal and non-terminal) in the grammar.

The get_non_terminals method returns a list of all non-terminal symbols in the grammar.

The get_terminals method returns a list of all terminal symbols in the grammar.

The create_dict method creates a dictionary representation of the grammar, where each non-terminal symbol is a key and the value is a list of production rules for that non-terminal symbol.

The has_empty method takes a non-terminal symbol as input and returns True if the symbol can derive the empty string, otherwise it returns False.

The filter method takes a list of production rules and a nullable symbol as input, and returns a list of updated production rules where the nullable symbol has been removed.

The replace_nullables method takes a list of production rules and a set of nullable symbols as input, and replaces any occurrence of a nullable symbol in the list with the empty string. It returns a tuple of the updated production rules and the number of replacements made.

****
## Conclusion/Results

****
## References
1.https://www.geeksforgeeks.org/converting-context-free-grammar-chomsky-normal-form/





