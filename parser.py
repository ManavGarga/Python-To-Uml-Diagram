import ast
from model import ClassInfo

class UMLParser(ast.NodeVisitor):
    def __init__(self):
        self.classes = {}

    def visit_ClassDef(self, node):
        class_info = ClassInfo(node.name)

        # Inheritance
        for base in node.bases:
            if isinstance(base, ast.Name):
                class_info.bases.append(base.id)

        # Body
        for stmt in node.body:
            if isinstance(stmt, ast.FunctionDef):
                class_info.add_method(stmt.name)

                for inner in ast.walk(stmt):
                    if isinstance(inner, ast.Assign):
                        for target in inner.targets:
                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == 'self':
                                class_info.add_attribute(target.attr)

                            # Composition
                            elif isinstance(inner.value, ast.Call) and isinstance(inner.value.func, ast.Name):
                                class_info.compositions.add(inner.value.func.id)

        self.classes[node.name] = class_info
        self.generic_visit(node)

    def parse(self, file_path):
        with open(file_path) as f:
            tree = ast.parse(f.read())
        self.visit(tree)
        return self.classes
