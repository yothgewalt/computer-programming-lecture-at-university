heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
h2 = ['Dr. Strange', 'Cpt. America', 'Blank Panther', 'Ant Man']

heroes.insert(0, h2[0])
print(heroes.index('Thor'))
heroes.insert(heroes.index('Thor'), h2[1])
print(heroes)
heroes.remove('Superman')
heroes.append('Ant Man')
print(heroes)
heroes.sort()
print(heroes)
newheroes = heroes
newheroes[0] = 'Wonder Woman'
print(heroes)
copyheroes = [] + heroes
print(copyheroes)
copyheroes[0] = 'Hanuman'
print(heroes)
print(copyheroes)