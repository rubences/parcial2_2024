class Member:
    def __init__(self, name, combat_experience, magical_skills):
        self.name = name
        self.combat_experience = combat_experience
        self.magical_skills = magical_skills

# Define the members of the council
members = [
    Member("Aragorn", True, False),
    Member("Gandalf", True, True),
    Member("Legolas", True, False),
    Member("Gimli", True, False),
    Member("Frodo", False, False),
    Member("Sam", False, False),
    Member("Elrond", True, True),
]

def decide_member(mission_type: str) -> str:
    if mission_type == "combat":
        for member in members:
            if member.combat_experience:
                return member.name
    elif mission_type == "espionage":
        for member in members:
            if not member.combat_experience and not member.magical_skills:
                return member.name
    elif mission_type == "magic":
        for member in members:
            if member.magical_skills:
                return member.name
    return "No suitable member found"

# Example usage
print(decide_member("combat"))  # Output: Aragorn
print(decide_member("espionage"))  # Output: Frodo
print(decide_member("magic"))  # Output: Gandalf