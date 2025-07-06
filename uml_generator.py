import sys
from parser import UMLParser
from diagram_graphviz import render_graphviz

def main():
    if len(sys.argv) != 2:
        print("Usage: python uml_generator.py <your_script.py>")
        return

    parser = UMLParser()
    classes = parser.parse(sys.argv[1])
    render_graphviz(classes)

if __name__ == "__main__":
    main()
