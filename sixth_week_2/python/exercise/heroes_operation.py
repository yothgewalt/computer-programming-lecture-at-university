avenger_team = [
    'Ironman', 'Thor', 'Hulk', 
    'Superman', 'Spiderman'
]

def display_heroes():
    return avenger_team

def add_heroes(hero_name):
    avenger_team.append(hero_name)

def insert_heroes(hero_name):
    avenger_team.insert(0, hero_name)

def remove_heroes(hero_name):
    avenger_team.remove(hero_name)

def display_sorted_heroes(heroes, descending=False):
    if descending:
        return sorted(heroes, reverse=True)
    
    return sorted(heroes)

if __name__ == '__main__':
    print(display_heroes())
    add_heroes('Ant Man')
    print(display_heroes())
    insert_heroes('Cpt. America')
    print(display_heroes())
    remove_heroes('Ant Man')
    print(display_sorted_heroes(avenger_team))
    print(display_sorted_heroes(avenger_team, descending=False))