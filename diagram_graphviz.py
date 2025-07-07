from graphviz import Digraph

def render_graphviz(classes: dict, output_file="uml_diagram", theme="light"):
    dot = Digraph(comment="UML Class Diagram", format="png")
    dot.attr(rankdir="LR")  # horizontal layout

    # 🎨 Theme styles
    if theme == "dark":
        node_attrs = {
            "shape": "record",
            "style": "filled",
            "fontname": "Helvetica",
            "fontsize": "10",
            "fillcolor": "#2b2b2b",
            "fontcolor": "white",
            "color": "#66d9ef"
        }
        edge_color = "#ffffff"
        comp_color = "#ff79c6"
    else:  # light
        node_attrs = {
            "shape": "record",
            "style": "filled",
            "fontname": "Helvetica",
            "fontsize": "10",
            "fillcolor": "#F0F8FF",
            "fontcolor": "black",
            "color": "#4682B4"
        }
        edge_color = "#2E8B57"
        comp_color = "#B22222"

    dot.attr("node", **node_attrs)

    # ✅ Class Boxes
    for cls in classes.values():
        label = f"{{{cls.name}|{'\\l'.join(cls.attributes)}|{'\\l'.join(cls.methods)}\\l}}"
        dot.node(cls.name, label=label)

    # ✅ Relationships
    for cls in classes.values():
        for base in cls.bases:
            if base in classes:
                dot.edge(base, cls.name,
                         arrowhead="onormal",
                         color=edge_color,
                         penwidth="2")

        for comp in cls.compositions:
            if comp in classes:
                dot.edge(cls.name, comp,
                         style="dashed",
                         color=comp_color,
                         label="uses",
                         fontname="Helvetica",
                         fontsize="9")

    dot.render(output_file, view=True)


