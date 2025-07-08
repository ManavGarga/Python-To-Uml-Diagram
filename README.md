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

![UML Example](uml_diagram.png)

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
├── uml_diagram.png                # Output image
└── README.md
```

---

## ⚙️ Usage

```bash
python uml_generator.py examples/car_system.py light
```

Options:
- `light` or `dark` — for theme
- Output: `uml_diagram.png` (opens automatically)

---

## ✨ How It Works

1. `parser.py`: Parses Python code into a tree of `ClassInfo` objects
2. Detects:
   - Inheritance (`class B(A):`)
   - Composition (`self.x = ClassName()`)
   - Aggregation (`self.x = arg_name`)
3. `diagram_graphviz.py`: Uses `graphviz.Digraph` to generate UML

---

## 🔧 TODO (optional extensions)

- [ ] Handle classmethod / staticmethod
- [ ] Show `__init__` parameters
- [ ] Support module/package-level grouping
- [ ] Export as `.svg` or embed in HTML
- [ ] Web UI

---

## 📝 License

MIT License.  
Author: Manav Garg


