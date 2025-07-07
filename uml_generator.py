from parser import UMLParser
from diagram_graphviz import render_graphviz

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python uml_generator.py <your_script.py>")
        return

    input_file = sys.argv[1]
    parser = UMLParser()
    classes = parser.parse(input_file)
    render_graphviz(classes)

if __name__ == "__main__":
    main()
