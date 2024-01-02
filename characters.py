from utils import load_characters

class Characters:
    _characters = load_characters()

    def __init__(self, characters):
        self.characters = characters
    
    @classmethod
    def list_characters(cls):
        print('List of characters:\n')

        for i, character in enumerate(cls._characters, 1):
            print(f'{i}. {character.name}')

Characters.list_characters()