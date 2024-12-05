class DecisionNode:
    def __init__(self, question, yes_branch=None, no_branch=None):
        self.question = question
        self.yes_branch = yes_branch
        self.no_branch = no_branch

def decide_member(mission_type: str) -> str:
    # Define the decision tree
    tree = DecisionNode(
        "¿Es una misión de combate?",
        yes_branch=DecisionNode(
            "¿Tiene experiencia en combate?",
            yes_branch=DecisionNode(
                "¿Tiene habilidades mágicas?",
                yes_branch="Gandalf",
                no_branch="Aragorn"
            ),
            no_branch=DecisionNode(
                "¿Es un espía?",
                yes_branch="Legolas",
                no_branch="Gimli"
            )
        ),
        no_branch=DecisionNode(
            "¿Es una misión de espionaje?",
            yes_branch=DecisionNode(
                "¿Tiene habilidades mágicas?",
                yes_branch="Galadriel",
                no_branch="Frodo"
            ),
            no_branch=DecisionNode(
                "¿Es una misión diplomática?",
                yes_branch="Elrond",
                no_branch="Sam"
            )
        )
    )

    # Traverse the tree based on the mission type
    current_node = tree
    while isinstance(current_node, DecisionNode):
        if mission_type == "combate":
            current_node = current_node.yes_branch
        elif mission_type == "espionaje":
            current_node = current_node.no_branch.yes_branch
        elif mission_type == "diplomacia":
            current_node = current_node.no_branch.no_branch.yes_branch
        else:
            current_node = current_node.no_branch.no_branch.no_branch

    return current_node

# Ejemplo de uso
print(decide_member("combate"))  # Output: Gandalf o Aragorn dependiendo de las preguntas
print(decide_member("espionaje"))  # Output: Galadriel o Frodo dependiendo de las preguntas
print(decide_member("diplomacia"))  # Output: Elrond
print(decide_member("otra"))  # Output: Sam