from graphviz import Digraph

def render_graphviz(classes: dict, output_file="uml_diagram"):
    dot = Digraph(comment="UML Class Diagram", format="png")

    for cls in classes.values():
        label = f"{cls.name}|{'\\l'.join(cls.attributes)}|{'\\l'.join(cls.methods)}"
        dot.node(cls.name, label=label, shape="record")

    for cls in classes.values():
        for base in cls.bases:
            if base in classes:
                dot.edge(base, cls.name)
        for comp in cls.compositions:
            if comp in classes:
                dot.edge(cls.name, comp, style='dashed')

    dot.render(output_file, view=True)
