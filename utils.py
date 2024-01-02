from character import Character

def load_characters():
    list = []

    list.append(Character('Heihachi Mishima', {
        "hp": 100,
        "moves": {
            "attack": "Dragon Uppercut",
            "defense": "Shockwaves",
            "special": "Rage Art"
        }
    }))

    list.append(Character('Jin Kazama', {
        "hp": 100,
        "moves": {
            "attack": "Avenger",
            "defense": "Regeneration",
            "special": "Penetrating Fist"
        }
    }))

    list.append(Character('Akuma', {
        "hp": 100,
        "moves": {
            "attack": "Gohadoken",
            "defense": "Rakan",
            "special": "Wrath of the Raging Demon"
        }
    }))

    list.append(Character('Ryu', {
        "hp": 100,
        "moves": {
            "attack": "Denjin Renki",
            "defense": "Mind's Eye",
            "special": "Shinku Tatsumaki Senpukyaku"
        }
    }))

    list.append(Character('Ken', {
        "hp": 100,
        "moves": {
            "attack": "Tatsumaki Senpukyaku",
            "defense": "Mind's Eye",
            "special": "Shinryureppa"
        }
    }))

    return list