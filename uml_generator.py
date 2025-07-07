import os
from parser import UMLParser
from diagram_graphviz import render_graphviz

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python uml_generator.py <your_script.py>")
        return

    input_file = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(input_file))[0]  # e.g., "student_management_system"
    output_dir = "diagrams"
    os.makedirs(output_dir, exist_ok=True)  # create diagrams/ if it doesn't exist

    output_path = os.path.join(output_dir, base_name)

    parser = UMLParser()
    classes = parser.parse(input_file)

    render_graphviz(classes, output_file=output_path)  # creates diagrams/student_management_system.png

if __name__ == "__main__":
    main()

