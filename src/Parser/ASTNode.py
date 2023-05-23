class ASTNode:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)