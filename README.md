# 🧩 Python to UML Diagram 

This tool **automatically generates UML class diagrams** from Python source code using:

- 🧠 `ast` for static code analysis
- 🎨 `graphviz` for visual diagram rendering

Supports:
- Class detection
- Inheritance
- Composition (♦)
- Aggregation (◊)
- Visibility (`+`, `#`, `-`)

---

## 📸 Example Output

From this input:

```python
class Car(Vehicle):
    def __init__(self, driver):
        self.engine = Engine()     # composition
        self.driver = driver       # aggregation
```

Produces this diagram:

![UML Example](diagrams/car_system.png)

> The output diagram is saved in the `diagrams/` folder.

---

## 🚀 Features

- ✅ Detects classes, methods, attributes
- ✅ Inheritance arrows (`◁`)
- ✅ Composition (filled diamond) → `self.x = ClassName()`
- ✅ Aggregation (hollow diamond) → `self.x = param`
- ✅ UML visibility:
  - `+` public
  - `#` protected
  - `-` private
- ✅ Light and dark themes
- ✅ Output as PNG via `graphviz`

---

## 📦 Installation

```bash
pip install graphviz
```

> Also ensure [Graphviz is installed](https://graphviz.org/download/):

> - macOS: `brew install graphviz`
> - Windows: Use official installer

---

## 📁 Project Structure

```
python-to-uml-diagram/
│
├── examples/
│   └── car_system.py              # Sample input
├── model.py                       # ClassInfo model
├── parser.py                      # AST-based parser
├── diagram_graphviz.py            # Renders Graphviz UML
├── uml_generator.py               # CLI runner
├── diagrams/
│   └── car_system.png             # Output image
└── README.md
```

---

## ⚙️ Usage

```bash
python uml_generator.py examples/car_system.py light
```

### CLI Options

```bash
python uml_generator.py <input_file> [light|dark]
```

- `input_file`: Python file to parse
- `light|dark`: Optional theme for output (default is `light`)
- Output: `diagrams/<input_file_name>.png` (auto-opens)

---

## ✨ How It Works

1. `parser.py`: Parses Python code into a tree of `ClassInfo` objects
2. Detects:
   - Inheritance (`class B(A):`)
   - Composition (`self.x = ClassName()`)
   - Aggregation (`self.x = arg_name`)
3. `diagram_graphviz.py`: Uses `graphviz.Digraph` to generate UML

---

## 🔧 Future Enhancements

- [ ] Parse type hints for accurate aggregation
- [ ] Detect class/static methods (e.g., `@staticmethod`)
- [ ] Show constructor parameters (`__init__` args)
- [ ] Group classes by module or package
- [ ] Export diagrams as SVG or HTML
- [ ] Web-based UI with upload & preview

---

## 📝 License

MIT License.  
Author: Manav Garg

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Graphviz](https://img.shields.io/badge/graphviz-enabled-brightgreen)
