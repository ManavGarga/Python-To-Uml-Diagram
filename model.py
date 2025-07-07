class ClassInfo:
    def __init__(self, name):
        self.name = name
        self.attributes    = set()
        self.methods       = set()
        self.bases         = []      # inheritance
        self.compositions  = set()   # ♦ filled‑diamond
        self.aggregations  = set()   # ◊ hollow‑diamond  ← NEW

    def add_attribute(self, name):
        self.attributes.add(name)

    def add_method(self, name):
        self.methods.add(name)

    def add_composition(self, cls_name):
        self.compositions.add(cls_name)

    def add_aggregation(self, cls_name):
        self.aggregations.add(cls_name)
