class TreeNode:
    def __init__(self, power, unit_type):
        self.power = power
        self.unit_type = unit_type
        self.left = None
        self.right = None

class BattleStrategy:
    def __init__(self):
        self.root = None

    def insert(self, power, unit_type):
        if not self.root:
            self.root = TreeNode(power, unit_type)
        else:
            self._insert(self.root, power, unit_type)

    def _insert(self, node, power, unit_type):
        if power < node.power:
            if node.left:
                self._insert(node.left, power, unit_type)
            else:
                node.left = TreeNode(power, unit_type)
        else:
            if node.right:
                self._insert(node.right, power, unit_type)
            else:
                node.right = TreeNode(power, unit_type)

    def find_counter_unit(self, enemy_unit):
        counter_units = {
            'orc': 'elf',
            'troll': 'human',
            'nazgul': 'wizard'
        }
        return counter_units.get(enemy_unit, 'unknown')

# Example usage
battle_strategy = BattleStrategy()
battle_strategy.insert(10, 'elf')
battle_strategy.insert(20, 'human')
battle_strategy.insert(30, 'wizard')

enemy_unit = 'orc'
print(f"The best counter unit for {enemy_unit} is {battle_strategy.find_counter_unit(enemy_unit)}")