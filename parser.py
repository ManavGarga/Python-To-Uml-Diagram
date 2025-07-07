import ast
from model import ClassInfo

class UMLParser(ast.NodeVisitor):
    def __init__(self):
        self.classes = {}

    # ---------- public API ----------
    def parse(self, file_path):
        with open(file_path) as f:
            tree = ast.parse(f.read())
        self.visit(tree)
        return self.classes

    # ---------- AST visitors ----------
    def visit_ClassDef(self, node: ast.ClassDef):
        ci = ClassInfo(node.name)

        # 1. inheritance
        for base in node.bases:
            if isinstance(base, ast.Name):
                ci.bases.append(base.id)

        # 2. walk body
        for stmt in node.body:
            # ── methods ─────────────────────────────────────────────
            if isinstance(stmt, ast.FunctionDef):
                ci.add_method(stmt.name)

                # gather parameter names for aggregation detection
                param_names = {arg.arg for arg in stmt.args.args[1:]}  # skip self

                # look at every assignment inside this method
                for inner in ast.walk(stmt):
                    if isinstance(inner, ast.Assign):
                        for target in inner.targets:
                            # only handle   self.xxx = <value>
                            if (isinstance(target, ast.Attribute)
                                    and isinstance(target.value, ast.Name)
                                    and target.value.id == "self"):

                                attr_name = target.attr
                                ci.add_attribute(attr_name)

                                value = inner.value
                                # 2.a composition:  self.x = ClassName()
                                if (isinstance(value, ast.Call)
                                        and isinstance(value.func, ast.Name)):
                                    ci.add_composition(value.func.id)

                                # 2.b aggregation:  self.x = driver
                                elif isinstance(value, ast.Name) and value.id in param_names:
                                    ci.add_aggregation(value.id.capitalize())  # param → class name guess

        # save & recurse
        self.classes[node.name] = ci
        self.generic_visit(node)

