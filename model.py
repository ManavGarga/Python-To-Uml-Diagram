class ClassInfo:
    def __init__(self, name):
        self.name = name
        self.attributes = set()
        self.methods = set()
        self.bases = []
        self.compositions = set()

    def add_attribute(self, name):
        self.attributes.add(name)

    def add_method(self, name):
        self.methods.add(name)
