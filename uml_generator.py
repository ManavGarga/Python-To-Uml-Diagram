from parser import UMLParser
from diagram_graphviz import render_graphviz
import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python uml_generator.py <your_script.py> [light|dark]")
        return

    input_file = sys.argv[1]
    theme = sys.argv[2] if len(sys.argv) > 2 else "light"

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_dir = "diagrams"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, base_name)

    parser = UMLParser()
    classes = parser.parse(input_file)
    render_graphviz(classes, output_file=output_path, theme=theme)

if __name__ == "__main__":
    main()


