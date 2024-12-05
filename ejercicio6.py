class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

# Ejemplo de uso
hash_table = HashTable(10)
hash_table.insert("Minas Tirith", "Vino")
hash_table.insert("Rivendel", "Joyas")
hash_table.insert("La Comarca", "Cerveza")
hash_table.insert("Isengard", "Hierro")

print(hash_table.search("Minas Tirith"))  # Salida: Vino
print(hash_table.search("Rivendel"))      # Salida: Joyas
print(hash_table.search("La Comarca"))    # Salida: Cerveza
print(hash_table.search("Isengard"))      # Salida: Hierro
print(hash_table.search("Moria"))         # Salida: None