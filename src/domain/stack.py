class Stack():
    def __init__(self, items=None):
        self.items = []

        if items:
            for item in items:
                self.push(item)


    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            item = self.items.pop()
            return item
        except:
            print("Error: Stack vazia")


    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return f'Stack(items={self.items})'
        else:
            return None

    def size(self):
        return len(self.items)