class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def search(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                return x.keys[i]
            elif x.leaf:
                return None
            else:
                return self.search(k, x.children[i])
        else:
            return self.search(k, self.root)

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.children.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            z.children = y.children[t:2 * t]
            y.children = y.children[0:t - 1]

class Library:
    def __init__(self, t):
        self.categories = {}
        self.t = t

    def add_category(self, category):
        if category not in self.categories:
            self.categories[category] = BTree(self.t)

    def add_book(self, category, title):
        if category in self.categories:
            self.categories[category].insert(title)
        else:
            self.add_category(category)
            self.categories[category].insert(title)

    def search_book(self, category, title):
        if category in self.categories:
            result = self.categories[category].search(title)
            if result:
                return f"Book '{title}' found in category '{category}'."
            else:
                return f"Book '{title}' not found in category '{category}'."
        else:
            return f"Category '{category}' not found."

# Example usage:
library = Library(3)
library.add_book("History", "The Fall of Gondolin")
library.add_book("Magic", "The Art of Wizardry")
library.add_book("Science", "The Laws of Physics")

print(library.search_book("History", "The Fall of Gondolin"))
print(library.search_book("Magic", "The Art of Wizardry"))
print(library.search_book("Science", "The Laws of Physics"))
print(library.search_book("History", "The Rise of Sauron"))